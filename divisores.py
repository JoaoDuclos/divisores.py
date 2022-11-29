n = input('Digite um númeoro: ')
if n.isdigit():
    n_digit = int(n)
    x = 1
    divisores = 0
    while x<=n_digit:
        resto = n_digit % x
        x+=1
        if resto == 0:
            divisores+=1
    print(divisores)
else:
    print('\nPor favor digite um número.')