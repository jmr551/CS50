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
    # Consultar las transacciones del usuario para calcular el portafolio
    transactions = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", session["user_id"])

    # Consultar el saldo de efectivo del usuario
    cash_row = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = cash_row[0]["cash"]

    # Inicializar la lista del portafolio y el total del valor del portafolio
    portfolio = []
    total_portfolio_value = cash

    # Obtener el precio actual y calcular el valor total para cada acción en el portafolio
    for transaction in transactions:
        stock = lookup(transaction["symbol"])
        stock_value = stock["price"] * transaction["total_shares"]
        total_portfolio_value += stock_value
        portfolio.append({
            "symbol": transaction["symbol"],
            "name": stock["name"],
            "shares": transaction["total_shares"],
            "price": stock["price"],
            "total": stock_value
        })

    # Renderizar la página del portafolio con la información del usuario y las acciones
    return render_template("index.html", cash=cash, portfolio=portfolio, total_portfolio_value=total_portfolio_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()  # Convertir el símbolo a mayúsculas para estandarización
        shares_str = request.form.get("shares")  # Mantén las acciones como string inicialmente para validación

        # Validar entrada del usuario
        if not symbol:
            return apology("Por favor, ingrese un símbolo.")

        try:
            shares = int(shares_str)
        except ValueError:
            return apology("Número de acciones debe ser un entero.")

        if shares <= 0:
            return apology("El número de acciones debe ser positivo.")

        # Obtener información de la acción usando lookup()
        stock = lookup(symbol)
        if stock is None:
            return apology("Símbolo inválido")

        # Consultar el saldo del usuario
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]

        # Calcular el costo total de la compra
        total_cost = shares * stock["price"]

        # Verificar si el usuario tiene suficiente dinero
        if cash < total_cost:
            return apology("Fondos insuficientes")

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
    return apology("TODO")


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
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        if stock is None:
            return apology("Symbol not found", 400)
        return render_template("quoted.html", stock=stock)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        username = request.form.get("username")
        password = request.form.get("password")
        hashed = generate_password_hash(password)
        if request.form.get("username") == "": # Falta verificar en la base de datos
            return apology("Invalid")
        elif len(rows) > 0:
            return apology("Usuario ya existente")
        elif request.form.get("password") == "":
            return apology("La contraseña no puede estar vacía")
        elif request.form.get("password")!=request.form.get("confirmation"):
            return apology("La contraseña y la confirmación son diferentes")
        else:
            db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed
            )

            redirect("/login")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
