import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    transactions = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])
    cash_row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash_row[0]["cash"]
    portfolio = []
    total_portfolio_value = cash

    for transaction in transactions:
        stock = lookup(transaction["symbol"])
        if stock is not None:  # Asegúrate de que la acción exista para evitar errores
            stock_value = stock["price"] * transaction["total_shares"]
            total_portfolio_value += stock_value
            portfolio.append({
                "symbol": transaction["symbol"],
                "shares": transaction["total_shares"],
                "price": stock["price"],
                "total": stock_value
            })

    return render_template("index.html", cash=cash, portfolio=portfolio, total_portfolio_value=total_portfolio_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Valida que shares sea un número entero positivo
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("Numero negativo o cero")
        except ValueError:
            return apology("Invalid number of shares")

        if not symbol:
            return apology("Vacío")

        # El resto de tu código parece estar bien
        # Obtener información de la acción usando lookup()
        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid symbol")

        # Consultar el saldo del usuario
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]

        # Calcular el costo total de la compra
        total_cost = shares * stock["price"]

        # Verificar si el usuario tiene suficiente dinero
        if cash < total_cost:
            return apology("Not enough cash")

        # Procesar la compra: actualizar el saldo del usuario y registrar la transacción
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, shares, stock["price"])

        # Redirigir al usuario a la página principal con un mensaje de éxito
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute(
        "SELECT symbol, shares, price, transacted FROM transactions WHERE user_id = ? ORDER BY transacted DESC", user_id)

    return render_template("history.html", transactions=transactions)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Verificar que la contraseña actual es correcta
        user_info = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        if not check_password_hash(user_info[0]["hash"], current_password):
            return apology("Invalid current password", 403)

        # Verificar que la nueva contraseña y la confirmación coinciden
        if new_password != confirmation:
            return apology("Passwords do not match", 403)

        # Opcional: Añade aquí cualquier validación adicional para la nueva contraseña
        # como longitud mínima, caracteres especiales, etc.

        # Actualizar la contraseña en la base de datos
        new_hash = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])

        # Redirigir al usuario a la página principal con un mensaje de éxito
        return redirect("/")
    else:
        # Mostrar el formulario de cambio de contraseña
        return render_template("change_password.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        stock = lookup(symbol)

        if not stock:
            return apology("Invalid symbol", 400)

        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Asegúrate de que el nombre de usuario y la contraseña no estén vacíos
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif password != confirmation:
            return apology("passwords do not match", 400)

        # Verifica si el nombre de usuario ya existe en la base de datos
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            return apology("username already exists", 400)

        # Si pasa todas las comprobaciones, inserta el nuevo usuario en la base de datos
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Inicia sesión automáticamente al usuario después de registrarse
        user_id = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
        session["user_id"] = user_id

        # Redirige al usuario a la página principal
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()  # Asegúrate de obtener el símbolo en mayúsculas
        shares_to_sell = int(request.form.get("shares"))

        if not symbol or shares_to_sell <= 0:
            return apology("Invalid symbol or shares")

        # Verificar cuántas acciones del símbolo posee el usuario
        shares_owned = db.execute(
            "SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", session["user_id"], symbol)[0]["total_shares"]

        if shares_to_sell > shares_owned:
            return apology("Too many shares")

        # Obtener el precio actual del stock
        stock = lookup(symbol)

        # Calcular el valor de la venta
        sale_value = shares_to_sell * stock["price"]

        # Registrar la venta (como transacción negativa)
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, -shares_to_sell, stock["price"])

        # Actualizar el efectivo del usuario
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", sale_value, session["user_id"])

        # Redirigir a la página principal con un mensaje de éxito
        return redirect("/")
    else:
        # Obtener la lista de stocks que el usuario posee
        stocks = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", stocks=stocks)
