import random
print("Bem vindo ao jogo da adivinhação")
choice_number = input("Digite o numero teto do desafio: ")

if  choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numerico")
    quit()

random_nunber = random.randint(0, choice_number )
n_choices = 0
while True:
    answer_user = input("Advinhe o numero: ")


    if  answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numerico. Favor informe um numero!")
        continue
    n_choices = n_choices + 1
    if  answer_user == random_nunber:
        print("Acertou!")
        break
    elif answer_user > random_nunber:
        print("Chutou alto, o numero randomico é menor que isso...")
    else:
        print("Chutou baixo, o numero randomico é maior que isso..")
print("N° de tentativas: " + str(n_choices))
