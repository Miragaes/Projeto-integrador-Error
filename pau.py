from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import color
from tkinter import ttk



#------------------------------- JANELA IMC -------------------------------
master = Tk()
master.title("Boa forma")
master.geometry("490x560+610+153")
master.resizable(False, False)

#------------------------------- IMPORTAÇÃO DE IMAGENS -------------------------------
img_fundo = PhotoImage(file="Boa Forma.png")
img_botao = PhotoImage(file ="botao calc.png")

imgBotaoProx = PhotoImage(file ="proximo.png")

imgFundo = PhotoImage(file="Dados Caloria.png")
imgBotaoCal = PhotoImage(file ="botao calc.png")
imgCalculoCal = PhotoImage(file ="Boa Forma calculoCal.png")
imgBotaoProx = PhotoImage(file ="proximo.png")

#================================Calorias=======================================



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
        pesoDigitado = enPeso.get()
        alturaDigitada= enAltura.get()
        pesoDigitado = float(pesoDigitado)
        alturaDigitada = float(alturaDigitada)

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
    # master1.destroy()
    labFundo2 = Label(master1, image = imgFundo)
    labFundo2.pack()
    

    enIdade = Entry(master1, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enIdade.pack()
    enIdade.place(width = 320, height = 40, x=70, y=175)

    
    vlist = ['Masculino', 'Feminino']
    combo = ttk.Combobox(master1, values = vlist)
    combo.current(0)
    combo.pack()
    combo.place(x = 90, y = 270 )
    opcao_01 = combo.get()
    print(type(opcao_01))
    print(opcao_01)
    
    def selecionar():
        valor = combo.get()
        print(valor)
        
    

    vlist2 = [0,1,3,4,5,6,7]
    combo2 = ttk.Combobox(master1, values = vlist2)
    combo2.current(0)
    combo2.pack()
    combo2.place(x = 90, y = 410 )
    opcao_02 = combo2.get()
    print(type(opcao_02))
    print(opcao_02)

    def selecionar_02():
        valor_02 = combo2.get()
        print(valor_02)
        print(type(valor_02))
        
    
    
    btDadosCal=Button(master1, bd = 2, image = imgBotaoProx, command =  janelaCal)
    btDadosCal.place(width = 180, height = 45, x = 150, y = 460)

    btSelecionar = Button(master1,text='Selecionar', bd=2, command = selecionar)
    btSelecionar.place(width = 70, height = 20, x = 250, y = 270)

    btSelecionar_02 = Button(master1, text='selecionar', bd=2, command = selecionar_02)
    btSelecionar_02.place(width = 70, height = 20, x= 250, y = 408)
    
    '''btCalcularTBM=Button(master1, bd = 2, image = imgBotaoProx, command = calculoTBM )
    btCalcularTBM.place(width = 180, height = 45, x = 150, y = 460)'''
#------------------------------- COLETA DE DADOS -------------------------------

def janelaCal():
    master2 = Toplevel()
    master2.title("Boa forma")
    master2.geometry("490x550+400+153")
    master2.resizable(False, False)
    labFundo3 = Label(master2, image = imgCalculoCal)
    labFundo3.pack()
#------------------------------- ALIMENTOS -------------------------------
    enPForma = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enPForma.pack()
    enPForma.place(width = 50, height = 20, x=220, y=130)
    PForma = enPForma.get()
    

    enQueijo = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enQueijo.pack()
    enQueijo.place(width = 50, height = 20, x=220, y=170)
    Queijo = enQueijo.get()
    

    enPres = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enPres.pack()
    enPres.place(width = 50, height = 20, x=220, y=210)
    Presunto = enPres.get()
    
    
    enReq = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enReq.pack()
    enReq.place(width = 50, height = 20, x=220, y=250)
    Requeijao = enReq.get()

    enBan = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enBan.pack()
    enBan.place(width = 50, height = 20, x=220, y=290)
    Banana = enBan.get()

    enOvo = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enOvo.pack()
    enOvo.place(width = 50, height = 20, x=220, y=330)
    Ovo = enOvo.get()

    enPf = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enPf.pack()
    enPf.place(width = 50, height = 20, x=227, y=360)
    Pf = enPf.get()

    enCb = Entry(master2, bd = 2, font = ("Calibri", 13), justify = CENTER)
    enCb.pack()
    enCb.place(width = 50, height = 20, x=220, y=400)
    Cb = enCb.get()

    enCs = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enCs.pack()
    enCs.place(width = 50, height = 20, x=420, y=130)
    Cs = enCs.get()
    

    enArroz = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enArroz.pack()
    enArroz.place(width = 50, height = 20, x=420, y=170)

    enArroz = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enArroz.pack()
    enArroz.place(width = 50, height = 20, x=420, y=210)

    enBat = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enBat.pack()
    enBat.place(width = 50, height = 20, x=420, y=250)
    Bat = enBat.get()

    enMac = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enMac.pack()
    enMac.place(width = 50, height = 20, x=420, y=290)
    Mac = enMac.get()

    enPi = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enPi.pack()
    enPi.place(width = 50, height = 20, x=420, y=330)
    Pi = enPi.get()

    enSu = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enSu.pack()
    enSu.place(width = 50, height = 20, x=420, y=370)
    Su = enSu.get()

    enXb = Entry(master2, bd = 2, font = ("Calibri", 15), justify = CENTER)
    enXb.pack()
    enXb.place(width = 50, height = 20, x=420, y=400)
    Xb = enXb.get()
    
    # btCalcularCal=Button(master2, bd = 2, image = imgBotaoProx, command = calculoTBM )
    # btCalcularCal.place(width = 180, height = 45, x = 150, y = 460)


#---------------------------- CRIAÇÃO BOTÃO -------------------------------

btCalcular=Button(master, bd = 2, image = img_botao, command = calculoIMC)
btCalcular.place(width = 180, height = 45, x = 150, y = 350)

btDadosCal=Button(master, bd = 2, image = imgBotaoProx, command = janelaDados)
btDadosCal.place(width = 180, height = 45, x = 150, y = 490)





master.mainloop()