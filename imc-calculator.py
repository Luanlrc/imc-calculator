def imc ():
    altura = input("Sua altura :")
    peso = input("Seu peso :")
    print(type(altura))
    try:
        altura=float(altura)
        peso=float(peso)
    except ValueError:
        print("valor incorreto, digite os valores novamente")
        imc()
    totalaltura = altura*altura
    resultado = peso/totalaltura
    print(f"Resultado IMC :{resultado:4.2f} sendo altura {altura}")
    if resultado < 18:
        print("abaixo do peso normal")
    elif resultado>18 and resultado < 25:
        print("peso normal")
    elif resultado>25 and resultado < 30:
        print("Excesso de peso")
    else:
        print("Obsidade")
    def op ():
        comando = int(input("voce quer cotinuar? Digite 1 para continuar ou 2 para sair:"))
        if comando == 1 :
             imc()
        elif comando == 2:
            print("obrigado por usar IMC ")
        elif comando not in [1,2] :
            print("op invalida")
            op()
    op()
imc ()
print("Fim do programa ")