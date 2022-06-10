from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import color
from tkinter import ttk
from functools import partial



#------------------------------- JANELA IMC -------------------------------
master = Tk()
master.title("Boa forma")
master.geometry("490x560+610+153")
master.iconbitmap("icone.ico")
master.resizable(False, False)

#------------------------------- IMPORTAÇÃO DE IMAGENS -------------------------------
img_fundo = PhotoImage(file="Boa Forma.png")
img_botao = PhotoImage(file ="botao calc.png")


imgBotaoProx = PhotoImage(file ="proximo.png")
imgFundo = PhotoImage(file="Dados Caloria.png")
imgBotaoCal = PhotoImage(file ="botao calc.png")
imgCalculoCal = PhotoImage(file ="Boa Forma calculoCal.png")
imgBotaoProx = PhotoImage(file ="proximo.png")



#------------------------------- IMAGEM DE FUNDO -------------------------------
lab_fundo = Label(master, image = img_fundo)
lab_fundo.pack()





#------------------------------- ENTRADA DE DADOS -------------------------------
enPeso = Entry(master, bd = 2, font = ("Calibri", 15), justify = CENTER)
enPeso.pack()
enPeso.place(width = 320, height = 40, x=70, y=185)



enAltura = Entry(master, bd = 2, font = ("Calibri", 15), justify = CENTER)
enAltura.pack()
enAltura.place(width = 320, height = 40, x = 69, y = 285)

#------------------------------- CALCULO IMC -------------------------------
def calculoIMC():
    try: 
        global pesoDigitado
        global alturaDigitada
        pesoDigitado = enPeso.get()
        alturaDigitada= enAltura.get()
        pesoDigitado = int(float(pesoDigitado))
        alturaDigitada = int(float(pesoDigitado))

        calculo = pesoDigitado / (alturaDigitada**2)
        calculo = round(calculo,2)
        calculo = str(calculo)
        calculo = calculo

        
        mensagemIMC = Label(master, text= 'Seu IMC é: ', font = ('Open Sans Extra Bold',16), foreground='#ffbd59',background = '#004aad')
        mensagemIMC.pack()
        mensagemIMC.place(x=145, y= 420)



        mostraIMC = Label(master, text = calculo, font=('Open Sans Extra Bold',16), foreground='#ffbd59',background = '#004aad')
        mostraIMC.pack()
        mostraIMC.place(x=255, y= 420)


    except ValueError:
        messagebox.showerror(title = 'Erro de digitação!', message= 'Digite apenas números')




#===================================== CALORIAS =====================================





#------------------------------- COLETA DE DADOS -------------------------------

def janelaDados():
    master1 = Toplevel()
    master1.title("Boa forma")
    master1.geometry("490x550+400+153")
    master1.resizable(False, False)
    labFundo2 = Label(master1, image = imgFundo)
    labFundo2.pack()
    
    
    enIdade = Entry(master1, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enIdade.pack()
    enIdade.place(width = 320, height = 40, x=70, y=175)
    global idade
    idade = enIdade.get()
    

    
    vlist = ['Masculino', 'Feminino']
    combo = ttk.Combobox(master1, values = vlist)
    combo.set("Escolha uma opção")
    combo.pack()
    combo.place(x = 90, y = 270 )

    def selecionar():
        global sexo
        sexo = combo.get()
        
#------------------------------- COLETA DE ATIVIDADE DO USUÁRIO -------------------------------

    vlist2 = [0,1,3,4,5,6,7]
    combo2 = ttk.Combobox(master1, values = vlist2)
    combo2.current(0)
    combo2.pack()
    combo2.place(x = 90, y = 410 )

    def selecionar_02():
        global valor_02
        valor_02 = combo2.get()
        valor_02 = int(valor_02) 
    selecionar_02()

    global freq
    if valor_02 == 0:
        freq = 1.725
    elif valor_02 == 1 or 2 or 3:
        freq = 1.550
    elif valor_02 == 4 or 5: 
        freq = 1.375
    elif valor_02 == 6 or 7:
        freq = 1.2
    
                    

    btSelecionar = Button(master1,text='Selecionar', bd=2, command = selecionar)
    btSelecionar.place(width = 70, height = 20, x = 250, y = 270)

    btSelecionar_02 = Button(master1, text='selecionar', bd=2, command = selecionar_02)
    btSelecionar_02.place(width = 70, height = 20, x= 250, y = 408)

    btDadosCal=Button(master1, bd = 2, image = imgBotaoProx, command = janelaCal)
    btDadosCal.place(width = 180, height = 45, x = 150, y = 460)


#------------------------------- CALCULO CALORIA IDEAL -------------------------------







#------------------------------- COLETA DE DADOS -------------------------------

def janelaCal():
    global master2
    master2 = Toplevel()
    master2.title("Boa forma")
    master2.geometry("490x550+400+153")
    master2.resizable(False, False)
    # master2.destroy()
    labFundo3 = Label(master2, image = imgCalculoCal)
    labFundo3.pack()

#------------------------------- ALIMENTOS -------------------------------
    global enPForma
    enPForma = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enPForma.pack()
    enPForma.place(width = 50, height = 20, x=220, y=130)
    global PFormaS
    PFormaS = enPForma.get()
    
    global enQueijo
    enQueijo = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enQueijo.pack()
    enQueijo.place(width = 50, height = 20, x=220, y=170)
    global QueijoS
    QueijoS = enQueijo.get()

    global enPres
    enPres = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enPres.pack()
    enPres.place(width = 50, height = 20, x=220, y=210)
    global PresuntoS
    PresuntoS = enPres.get()

    global enReq
    enReq = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enReq.pack()
    enReq.place(width = 50, height = 20, x=220, y=250)
    global RequeijaoS
    RequeijaoS = enReq.get()

    global enBan
    enBan = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enBan.pack()
    enBan.place(width = 50, height = 20, x=220, y=290)
    global BananaS
    BananaS = enBan.get()

    global enOvo
    enOvo = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enOvo.pack()
    enOvo.place(width = 50, height = 20, x=220, y=330)
    global OvoS
    OvoS = enOvo.get()

    global enPf
    enPf = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enPf.pack()
    enPf.place(width = 50, height = 20, x=227, y=360)
    global PfS
    PfS = enPf.get()

    global enCb
    enCb = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enCb.pack()
    enCb.place(width = 50, height = 20, x=220, y=400)
    global CbS
    CbS = enCb.get()

    global enCs
    enCs = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enCs.pack()
    enCs.place(width = 50, height = 20, x=420, y=130)
    global CsS
    CsS = enCs.get()

    global enArroz
    enArroz = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enArroz.pack()
    enArroz.place(width = 50, height = 20, x=420, y=170)
    global ArrozS
    ArrozS = enArroz.get()

    global enFeijao
    enFeijao = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enFeijao.pack()
    enFeijao.place(width = 50, height = 20, x=420, y=210)
    global FeijaoS
    FeijaoS = enFeijao.get()

    global enBat
    enBat = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enBat.pack()
    enBat.place(width = 50, height = 20, x=420, y=250)
    global BatS
    BatS = enBat.get()

    global enMac
    enMac = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enMac.pack()
    enMac.place(width = 50, height = 20, x=420, y=290)
    global MacS
    MacS = enMac.get()

    global enPi
    enPi = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enPi.pack()
    enPi.place(width = 50, height = 20, x=420, y=330)
    global PiS
    PiS = enPi.get()

    global enSu
    enSu = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enSu.pack()
    enSu.place(width = 50, height = 20, x=420, y=370)
    global SuS
    SuS = enSu.get()

    global enXb
    enXb = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enXb.pack()
    enXb.place(width = 50, height = 20, x=420, y=400)
    global XbS
    XbS = enXb.get()


    
 #------------------------------- SOMA ALIMENTOS -------------------------------   
    # def transEmNumero():
    #     global PForma
    #     global Queijo
    #     global Presunto
    #     global Requeijao
    #     global Banana
    #     global Ovo
    #     global Pf
    #     global Cb
    #     global Cs
    #     global Arroz
    #     global Feijao
    #     global Bat
    #     global Mac
    #     global Pi
    #     global Su
    #     global Xb
    #     PForma = enPForma.get()
    #     Queijo = enQueijo.get()
    #     Presunto = enPres.get()
    #     Requeijao = enReq.get()
    #     Banana = enBan.get()
    #     Ovo = enOvo.get()
    #     Pf = enPf.get()
    #     Cb = enCb.get()
    #     Cs = enCs.get()
    #     Arroz = enArroz.get()
    #     Feijao = enFeijao.get()
    #     Bat = enBat.get()
    #     Mac = enMac.get()
    #     Pi = enPi.get()
    #     Su = enSu.get()
    #     Xb = enXb.get()

    # def caloriaIngerida():
    #     global ingestao
    #     ingestao = (Ovo * (155/100)) + (Banana * (89/100)) + (Arroz * (130/100)) + (PForma * (122/100)) + (Queijo * (280/100)) + (Presunto * (145/100)) + (Requeijao * (174/100)) + (Xb * (303/100)) +  (Bat * (86/100)) + (Mac * (371/100)) + (Su * (372/100)) + (Cb * (244/100)) + (Cs * (242/100)) + (Pf * (165/100)) + (Pi * (291/100)) + (Feijao * (347/100))
    # global caloriaIngeridaI
    # caloriaIngeridaI = caloriaIngerida


   
    def calculoTaxa():
        idade = int(float(idade))
        if sexo == 'Masculino':
            tbmM = 66.5 + (13.8 * pesoDigitado) + (5 * alturaDigitada) -(6.8 * idade)
            caloriaIdeal = tbmM * freq
            caloriaIdeal = round(caloriaIdeal, 2)
        else:
            tbF = 655.1 + (9.5 * pesoDigitado) +(1.8 * alturaDigitada) - (4.7 * idade)
            
            caloriaIdeal = tbF * freq
            caloriaIdeal = round(caloriaIdeal,2)
    
    



     
    def metaDiaria(caloriaDesejada):
        Xb = float(XbS)
        Su = float(SuS)
        Pi = float(PiS)
        Mac = float(MacS)
        Bat = float(BatS)
        Feijao = float(FeijaoS)
        Arroz = float(ArrozS)
        Cs = float(CsS)
        Cb = float(CbS)
        Pf = float(PfS)
        Ovo = float(OvoS)
        Banana = float(BananaS)
        Requeijao = float(RequeijaoS)
        Presunto = float(PresuntoS)
        Queijo = float(QueijoS)
        PForma = float(PFormaS)
        ingestao = (Ovo * (155/100)) + (Banana * (89/100)) + (Arroz * (130/100)) + (PForma * (122/100)) + (Queijo * (280/100)) + (Presunto * (145/100)) + (Requeijao * (174/100)) + (Xb * (303/100)) +  (Bat * (86/100)) + (Mac * (371/100)) + (Su * (372/100)) + (Cb * (244/100)) + (Cs * (242/100)) + (Pf * (165/100)) + (Pi * (291/100)) + (Feijao * (347/100))
        meta = ingestao - caloriaDesejada
        meta = round(meta,2)
        return meta
    

    btCalcular=Button(master2, bd = 2, image = img_botao, command = metaDiaria(calculoTaxa))
    btCalcular.place(width = 180, height = 45, x = 150, y = 350)
    

    # metaDiaria(calculoTaxa,caloriaIngerida)   
#---------------------------- CRIAÇÃO BOTÃO -------------------------------

btCalcular=Button(master, bd = 2, image = img_botao, command = calculoIMC)
btCalcular.place(width = 180, height = 45, x = 150, y = 350)

btDadosCal=Button(master, bd = 2, image = imgBotaoProx, command = janelaDados)
btDadosCal.place(width = 180, height = 45, x = 150, y = 490)








master.mainloop()