
nasc = False
while (nasc == False):
    print("..........CADASTRO..........")
    print("Digite seu nome completo: ")
    nome = (input)()
 
    try:

        print("Insira seu ano de nascimento: ")
        nasc = int(input()) 
    
        if  nasc > 1922 and nasc < 2022:
            resposta = 2022 - nasc
            print(nome,"sua idade é", resposta, "anos")
            nasc = True

        else:
            nasc < 1922 and nasc > 2022
            nasc = False
            print("Erro!!Ano inválido")

    except:
        print("Erro!Por favor refaça o cadastro")

    
   









    


