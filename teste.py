from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import color






#------------------------------- JANELA IMC -------------------------------
master = Tk()
master.title("Boa forma")
master.geometry("490x560+610+153")
master.iconbitmap("icone.ico")
master.resizable(False, False)

#------------------------------- IMPORTAÇÃO DE IMAGENS -------------------------------
img_fundo = PhotoImage(file="Boa Forma.png")
img_botao = PhotoImage(file ="botao calc.png")
#------------------------------- TROCA JANELA -------------------------------

def nova_janela():
    master1 = Toplevel()
    master1.title("Nova janela")
    master1.geometry("490x550+400+153")
    master.destroy()

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
    pesoDigitado = enPeso.get()
    alturaDigitada= enAltura.get()
    pesoDigitado = float(pesoDigitado)
    alturaDigitada = float(alturaDigitada)

    if type(alturaDigitada) and type(pesoDigitado) == str:    
        messagebox.showerror(title = 'Erro de digitação!', message= 'Digite apenas números')
        
    else:
        calculo = pesoDigitado / (alturaDigitada**2)
        calculo = round(calculo,2)
        calculo = str(calculo)
        calculo = calculo

        
        mensagemIMC = Label(master, text= 'Seu IMC é: ', font = ('Open Sans Extra Bold',16), foreground='#ffbd59',background = '#004aad')
        mensagemIMC.pack()
        mensagemIMC.place(x=140, y= 450)



        mostraIMC = Label(master, text = calculo, font=('Open Sans Extra Bold',16), foreground='#ffbd59',background = '#004aad')
        mostraIMC.pack()
        mostraIMC.place(x=250, y= 450)






#---------------------------- CRIAÇÃO BOTÃO -------------------------------

bt_entrar=Button(master, bd = 2, image = img_botao, command = calculoIMC)
bt_entrar.place(width = 180, height = 45, x=150, y=350)




master.mainloop()