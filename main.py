def welcome_user(name):
    return(f"Hi{name}")

welcome_user(input("Enter Your Name : "))


def addition(x,y):
    return(x+y)
addition(16,12)

def even_or_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd' 
print(even_or_odd(40))

def ori_ricxvi(x,y):
    return x ** y
print(ori_ricxvi(10,12))

def stringis_sigrdze(sityva):
    return len(sityva)
print(stringis_sigrdze("ramdeni_saklasoa"))

def shebrunebuli_versia(sityva1):
    return sityva1[::-1]
print(shebrunebuli_versia("Gamarjoba"))

def sityvebis_sia(ricxvebi):
    return sum()

def check_cap(name):
    if name == name.capitalize():
        return 'Your name is capitalized'
    else:
        return 'Your name is not capitalized'
print(check_cap(input('Name : ')))