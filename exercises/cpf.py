import re

while True:
    cpf = re.sub(
        r'[^0-9]',
        '',
        input("Digite seu cpf\n")
        )
    try:
        int(cpf)
        if len(cpf) == 11:
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
                print("Cpf correto")
            else:
                print("Cpf inválido")
        else:
            print("Seu CPF deve conter 11 números")
    except:
        print("Digite apenas números")