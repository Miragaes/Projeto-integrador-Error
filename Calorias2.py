# calorias

# ------------VERFICAÇÃO DE DADOS------------

def idadeUsuario():
    digitouIdadeDireito = False
    while not digitouIdadeDireito:
        try:
            idade = int(input('Digite sua idade: '))
            if idade <= 0:
                print('A idade deve ser um número maior que 0.')
            elif idade < 18 or idade > 60:
                print('\n CUIDADO: O programa é indicado para pessoas com idade entre 18 e 60 anos, os resultados podem ser afetados!')
            else: 
                digitouIdadeDireito = True
        except ValueError:
            print('\nDigite apenas números!')
        return (int(idade))
idade = idadeUsuario()

def alturaUsuario ():
    digitoudireito = False
    while not digitoudireito:
        try:
            altura = float(input("Digite a sua altura em metros :"))
            if altura <= 0:
                print("Erro, digite numero positivo")
            else: digitoudireito = True
        except ValueError:
            print("Apenas numeros serão aceitos. Tente novamente")
    return (float(altura))
altura = alturaUsuario()
    
def pesoUsuario():
    digitoucerto = False
    while not digitoucerto:
        try:
            peso = float(input("Digite seu peso em quilogramas (KG): "))
            if peso <= 0:
                print("Digite numeros positivos e diferentes de 0 (zero). Tente novamente")

            else:
                digitoucerto = True
        except ValueError:
            print("Digite apenas algarismos. Tente novamente")
    return (float(peso))
peso = pesoUsuario()
                        

                 
def sexoUsuario():    
    digitouSexoDireito = False
    while not digitouSexoDireito:
        print('[1] Masculino')
        print('[2] Feminino')
        try:
            sexo = int(input('Escolha uma opção para seu sexo (BIOLOGICO): '))
            if sexo == 1:
                digitouSexoDireito = True
            elif sexo == 2: 
                digitouSexoDireito = True
            else:
                print('\n Opção inválida.')
        except ValueError:
            print('\n Digite uma das opções!')
    return (int(sexo))
sexo = sexoUsuario()

freq = 0
def atividadeUsuario():
    digitouAtividadeDireito = False
    while not digitouAtividadeDireito:
        print('\n[1] De 6 à 7 dias por semana')
        print('[2] De 4 à 5 dias por semana')
        print('[3] De 1 à 3 dias por semana')
        print('[4] Nenhuma')
        try:
            atividade = int(input('Digite a opçao que corresponda ao seu nível de atividade física: '))
            global freq
            if atividade == 1:
                freq = 1.2
                digitouAtividadeDireito = True
            elif atividade == 2:
                freq = 1.375
                digitouAtividadeDireito = True
            elif atividade == 3:
                freq = 1.550
                digitouAtividadeDireito = True
            elif atividade == 4:
                freq = 1.725
                digitouAtividadeDireito = True
            else:
                print ("\n Opção inválida.")
                digitouErradoFreq = False
        except ValueError:
            print('Digite uma das opções!')
    return (atividade)
atividade = atividadeUsuario()

digitouCaloriaDireto = False
while not digitouCaloriaDireto:
    try:
        caloriaIngerida = int(input('Quantas calorias você ingeriu aproximadamente? '))
        digitouCaloriaDireto = True
    except ValueError:
            print('Digite apenas números inteiros!')


# ------------CALCULO DE TAXA BASAL------------
tbM = 0
def calculoTBM(sexoDigitado, pesoDigitado, alturaDigitada, idadeDigitada, atividadeDigitada):
    if sexoDigitado == 1:
        global tbM
        tbmM = 66.5 + (13.8 * pesoDigitado) + (5 * alturaDigitada) -(6.8 * idadeDigitada)
        
        caloriaIdeal = tbmM * freq
        caloriaIdeal = round(caloriaIdeal, 2)
        
    else:
        tbF = 655.1 + (9.5 * pesoDigitado) +(1.8 * alturaDigitada) - (4.7 * idadeDigitada)
        
        caloriaIdeal = tbM * freq
        caloriaIdeal = round(caloriaIdeal,2)
    return caloriaIdeal
caloriaIdeal = calculoTBM(sexo,peso,altura,idade,atividade)
print("A sua quantidade de calorias ideal é de ",caloriaIdeal)

# ------------CALCULO META DE CALORIAS------------

def metaCaloria(caloriaDesejada,caloriaDigitada):
    meta = caloriaDigitada - caloriaDesejada
    meta = round(meta,2)
    if meta == 0:
        print('\nParabéns, você atingiu a quantidade ideal')
    elif meta > 1:
        print('\nVocê ingeriu', meta, "calorias a mais do que o ideal.")
    else:
        print("Voce ingeriou", meta*(-1), "calorias a menos do que o ideal.")
    return meta
meta = metaCaloria(caloriaIdeal,caloriaIngerida)



