def dec2bin(valor):
    """Convierte un valor en base 10 a binario"""
    return bin(valor)[2:]

def bin2dec(valor):
    """Convierte un valor binario a base 10"""
    return int(valor, 2)

def bas2bas(valor, base1, base2):
    """Convierte un valor de una base a otra"""
    if base1 == 10:
        # Convertir de base 10 a base2
        return dec2bas(valor, base2)
    elif base2 == 10:
        # Convertir de base1 a base 10
        return bas2dec(valor, base1)
    else:
        # Convertir de base1 a base 10 y luego a base2
        dec_value = bas2dec(valor, base1)
        return dec2bas(dec_value, base2)

def dec2bas(valor, base):
    """Convierte un valor en base 10 a cualquier otra base"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while valor > 0:
        remainder = valor % base
        result = digits[remainder] + result
        valor //= base
    return result if result else "0"

def bas2dec(valor, base):
    """Convierte un valor de cualquier base a base 10"""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    power = 0
    for digit in reversed(valor):
        result += digits.index(digit) * (base ** power)
        power += 1
    return result


print("Decimal a Binario: ", dec2bin(25))
print("Binario a Decimal: ", bin2dec("11001"))
print("Base 2 a Base 16: ", bas2bas("11001", 2, 16))