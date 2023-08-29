import random
print("Bem vindo ao jogo da adivinhação!")

def obter_numero_real():
    while True:
        numero_str = input("Vamos jogar! me diga um numero: ")
        try:
            numero_real = int(numero_str)
            return numero_real
        except ValueError:
            print("Entrada inválida. Digite um número real válido.")

def obter_n_tentativas():
    while True:
        n_tentativas = input("Certo! Agora me diga, quantas tentativas você quer? ")
        try:
            n_tentativas = int(n_tentativas)
            return n_tentativas
        except ValueError:
            print("Entrada inválida. Digite um número real válido.")


numero_real =  obter_numero_real()
n_tentativas = obter_n_tentativas()

numero_aleatorio = random.randrange(1,numero_real )
contador = 1


while True:
    chute = int(input(f"estou pensando em um numero de 1 a {numero_real}  qual é?"))
    if chute == numero_aleatorio:
        print(f"Parabéns! A resposta era {numero_aleatorio}! \nAcertou em {contador} tentativas de {n_tentativas}")
        break
    elif contador == n_tentativas:
        print(f"acabaram suas tentativas! :( o numero era: {numero_aleatorio}")
        break
    else:
        contador = contador + 1
        if chute > numero_aleatorio:
            print("Chutou alto, o numero que pensei é menor")
        else:
            print("chutou baixo, o numero que pensei é maior")
        continue
print("fim")

