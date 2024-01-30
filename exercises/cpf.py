import re
import os

'''def sair():
    decisao = input("Deseja [s]air ou [c]ontinuar?").lower()
    if decisao == 'c':
        programa()
    elif decisao == 's':
        teste = 's'
        return teste
    else:
        print("erro")'''


def programa():
    consultar_cpf = True
    while consultar_cpf:
        cpf = re.sub(
            r'[^0-9]',
            '',
            input("Digite seu cpf\n")
            )
        primeiro_char = cpf[0]
        primeiro_char_repetido = primeiro_char * len(cpf)
        try:
            int(cpf)
            
            if primeiro_char_repetido == cpf:
                os.system('clear')
                print(f'CPF: {cpf} inválido devido repetição de números.')
            
            elif len(cpf) == 11:
                primeiro_verificador = 0
                segundo_verificador = 0
                primeiros_digitos = cpf[:9]
                multiplicador = 10
                digitos_multiplicados = []
                digitos_verificador_multiplicados = []

                for i,digito in enumerate(primeiros_digitos):
                    digitos_multiplicados.append(int(digito)*multiplicador) 
                    multiplicador=multiplicador-1 
                else:
                    multiplicador = 11

                soma_digitos = sum(digitos_multiplicados)
                resto_divisao = soma_digitos%11

                if resto_divisao < 2:
                    primeiro_verificador = 0
                elif resto_divisao >= 2:
                    primeiro_verificador = 11 - resto_divisao

                primeiros_digitos_verificador = primeiros_digitos+str(primeiro_verificador)


                for i,digito in enumerate(primeiros_digitos_verificador):
                    digitos_verificador_multiplicados.append(int(digito)*multiplicador)
                    multiplicador = multiplicador-1

                digitos_verificador_multiplicados

                soma_digitos_verificador = sum(digitos_verificador_multiplicados)
                resto_divisao_verificador = soma_digitos_verificador%11

                if resto_divisao_verificador < 2:
                    segundo_verificador = 0
                elif resto_divisao_verificador >= 2:
                    segundo_verificador = 11 - resto_divisao_verificador

                segundo_verificador
                cpf_verificador = primeiros_digitos_verificador+str(segundo_verificador)
                cpf_verificador

                if cpf == cpf_verificador:
                    os.system('clear')
                    print(f"CPF: {cpf} está correto.")
                    
                else:
                    os.system('clear')
                    print(f"CPF: {cpf} inválido.")
                    
            else:
                tamanho_cpf_errado = len(cpf)
                os.system('clear')
                print(f"Você digitou {tamanho_cpf_errado} números, CPF deve ter 11.")
                
        except:
            os.system('clear')
            print("Digite apenas números")
            
programa()