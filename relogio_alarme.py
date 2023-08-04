# Projeto Alarme


# Importação de bibliotecas
from tkinter import *
import time
import datetime
import winsound


# Criação do Alarme - Lógica de Funcionamento (Loop)
def alarme(alarme_programado):
    while True:
        time.sleep(1)
        tempo_atual = datetime.datetime.now()
        hora = tempo_atual.strftime("%H:%M:%S")
        data = tempo_atual.strftime("%d/%m/%y")
        print(f"A data Programada é: {data}")
        print(hora)
        if hora == alarme_programado:
            Alarme = Label(relogio,text = "ALARME !!!",fg="red", bg="black" ,relief = "solid",font=("Helevetica",7,"bold")).place(x=300, y=29)
            print("ALARME !!!")
            winsound.PlaySound("sound.nav", winsound.SND_ASYNC)
            break


def hora_atual():
    alarme_programado = f"{hora.get()}:{min.get()}:{seg.get()}"
    alarme(alarme_programado)


# Inicialização da janela
relogio = Tk()
relogio.title("Relógio de Alarme")
relogio.iconbitmap("")
relogio.geometry("450x200")
formato_tempo = Label(relogio,text= "Inserir horário em formato 24h", fg="blue",relief = "solid",font=("Arial")).place(x=60, y=120)
adicaoTempo = Label(relogio,text= "Hora / Min / Seg", font= 60).place(x = 110)
configAlarme = Label(relogio,text= "Horário para tocar:", fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


# Variáveis que requisitam o funcionamento do alarme (Inicialização):
hora = StringVar()
min = StringVar()
seg = StringVar()

# Tempo requerido para modificar horário de alarme
hora_tempo= Entry(relogio,textvariable= hora,bg='pink',width=15).place(x=110,y=30)
min_tempo= Entry(relogio,textvariable= min,bg='pink',width=15).place(x=150,y=30)
seg_tempo= Entry(relogio,textvariable= seg,bg='pink',width=15).place(x=200,y=30)

# Ler o tempo inserido pelo usuário:
submit = Button(relogio,text = "Set Alarm",fg="red",width = 10,command = hora_atual).place(x =110,y=70)


# Execução da janela
relogio.mainloop()

