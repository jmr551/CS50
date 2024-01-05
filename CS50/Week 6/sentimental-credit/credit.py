import cs50


def tarjeta(num):
    '''
    Empresa     Inicio              Digits:
    AmEx:       34, 37              15
    MasterCard: 51, 52, 53, 54, 55  16
    Visa:       4                   13, 16
    '''
    digits = len(num)
    if (num[:2] == '34' or num[:2] == '37') and digits == 15:
        return "AMEX"

    elif (50 < int(num[:2]) < 56) and digits == 16:
        return 'MASTERCARD'

    elif (num[0] == '4' and (digits == 13 or digits == 16)):
        return 'VISA'

    else:
        return 'INVALID'


def valido(num):
    num_inv = num[::-1]
    par = 0
    impar = 0
    for i in range(len(num)):
        if i % 2 == 0:
            par += int(num_inv[i])
            print("Par:", num_inv[i])
        else:
            tmp = 2 * int(num_inv[i])
            if tmp >= 10:
                tmp = tmp % 10 + int(tmp/10)
            impar += tmp
            print("Impar * 2:", num_inv[i], " y se sumó", tmp)
    print("Total par:", par)
    print("Total impar:", impar)
    print("la suma sale: ", par+impar)
    if (par + impar) % 10 == 0:
        return True
    else:
        return False


num = cs50.get_string("Number: ")

if valido(num):
    print(tarjeta(num))
else:
    print("INVALID")
