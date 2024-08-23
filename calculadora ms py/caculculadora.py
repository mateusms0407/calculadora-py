vr = "1"
while vr == "1":
    print(''' --calculador--
    escolha a operaçao
    1-soma
    2-subtração
    3-divisão
    4-multiplicação
    5-elevar ao qudrado 
    6-sair''')
    operaçao=input("qual tipo de operação voce deseja: ")
    
    if operaçao == "1":
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite outro numero: "))
        print(f"o resultado é {numero1 + numero2}")
    elif operaçao == '2':
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite outro numero: "))
        print(f"o resultado é {numero1 - numero2}")
    elif operaçao == 3:
        numero1 = int(input("digite um numero: "))
        numero2 = int(input("digite outro numero: "))
        print(f"o resultado é {numero1 / numero2}")
    elif operaçao == 4:
        numero1 = int(input("digite um numero: "))
        numero = int(input("digite outro numero: "))
        print(f"o resultado é {numero1 * numero2}")
    elif operaçao == 5:
        numero1 = int(input("digite um numero: "))
        print(f"o resultado é {numero1 * numero1}")
    elif operaçao == 6:
        vr = 0
    else:
        print('tente novamente')
    print()
    