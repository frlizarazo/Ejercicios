# -*- coding: utf-8 -*-

"""
Created on Sun Dec 26 12:36:41 2021

@author: Frank

"""

##============================== Importo las librerias

from random import randint
import tkinter as tk
import pandas as p
import os
import tkinter.filedialog as fd

##============================== Condiciones Iniciales

marcador=[0,0,0]
opciones=['piedra','papel','tijeras']
resultado=['Empate','Ganaste','Perdiste']

try:
    os.makedirs('Partidas/')
except FileExistsError:
    pass

##============================== Defino las funciones

def activate():
    if scoreOpt.get()==1:
        button.config(state=tk.NORMAL)
        button0.config(state=tk.DISABLED)
        button1.config(state=tk.DISABLED)
        
        lbe.config(text='-----------')
        lbg.config(text='-----------')
        lbp.config(text='-----------')
        
        name.config(state=tk.NORMAL)
        name.delete(0,'end')
        name.config(state=tk.DISABLED)
        
        select.config(state=tk.NORMAL)
        select.delete(0,'end')
        select.config(state=tk.DISABLED)
        
    elif scoreOpt.get()==0:
        button0.config(state=tk.NORMAL)
        button.config(state=tk.DISABLED)
        button1.config(state=tk.DISABLED)
        
        lbe.config(text='-----------')
        lbg.config(text='-----------')
        lbp.config(text='-----------')
        
        name.config(state=tk.NORMAL)
        name.delete(0,'end')
        name.config(state=tk.DISABLED)
        
        select.config(state=tk.NORMAL)
        select.delete(0,'end')
        select.config(state=tk.DISABLED)
        
        searchd.config(state=tk.NORMAL)
        searchd.delete(0,'end')
        searchd.config(state=tk.DISABLED)
        
def refresh():
    lbe.config(text=f'- Empates: {marcador[0]} ')
    lbg.config(text=f'- Victorias: {marcador[1]} ')
    lbp.config(text=f'- Derrotas: {marcador[2]} ')


def iniciar():
    marcador=[0,0,0]
    refresh()
    
    select.config(state=tk.NORMAL)
    button1.config(state=tk.NORMAL)
    
    name.config(state=tk.NORMAL)
    name.delete(0,'end')
    name.insert(tk.END,'Nueva Partida')
    name.config(state=tk.DISABLED)
    
    searchd.config(state=tk.DISABLED)

def exam():
    global marcador, archivo
    archivo=fd.askopenfile(parent=root, title='Seleccionar archivo',
                           filetypes=(('Archivo CSV', '*.csv'),),
                           initialdir=(os.getcwd(),'/Partidas/'))
    df=p.read_csv(archivo)
    marcador=list(df.Score)
    refresh()
    
    searchd.config(state=tk.NORMAL)
    searchd.insert(tk.END,archivo.name)
    searchd.config(state=tk.DISABLED)
    
    name.config(state=tk.NORMAL)
    name.delete(0,'end')
    name.insert(tk.END,archivo.name.rsplit('/',1)[1].replace('.csv',''))
    name.config(state=tk.DISABLED)    
    
    select.config(state=tk.NORMAL)
    button1.config(state=tk.NORMAL)

def jugar():
    
    idx      = randint(0,2)
    eleccion = choise.get()
    
    lb1.config(text=f'El computador escoge: {opciones[idx]}')
    
    try:
        num = opciones.index(eleccion)
        res = num-idx
        marcador[res] = marcador[res]+1
        
        lb2.config(text=(f'-----------{resultado[res]}-----------'))
        
    except:
        lb1.config(text='Opcion invalida')
        
    refresh()
    
    name.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)

def savefile():
    df=p.DataFrame(zip(resultado,marcador),columns=[' ','Score'])
    df.to_csv(f'Partidas\\{nick.get()}.csv',index=False)
    
def closew():
    root.destroy()
    
##============================== Creo la interfaz

## Creo la ventana
root = tk.Tk()
root.title('Juego')
root.iconbitmap(r'img.ico')

## Creo los Frames
score  = tk.LabelFrame(root, text='Cargar Datos')
show   = tk.LabelFrame(root, text='Score')
game   = tk.LabelFrame(root, text='Piedra, Papel o Tijeras?')
sscore = tk.LabelFrame(root, text='Guardar Partida')

score.grid( row=0, column=0, pady=(10,10), padx=(10,10))
show.grid(  row=1, column=0, pady=(10,10), padx=(10,10), sticky='ew')
game.grid(  row=2, column=0, pady=(10,10), padx=(10,10), sticky='ew')
sscore.grid(row=5, column=0, pady=(10,10), padx=(10,10), sticky='ew')

## Creo las Variables
scoreOpt = tk.IntVar()
choise   = tk.StringVar()
nick     = tk.StringVar()

## Creo las Labels
lbe = tk.Label( show, text='-----------')
lbg = tk.Label( show, text='-----------')
lbp = tk.Label( show, text='-----------')
lb1 = tk.Label( game, text='-----------')
lb2 = tk.Label( game, text='-----------')

lbe.grid( row=0, column=0, pady=(10,5), padx=(10,10))
lbg.grid( row=1, column=0,              padx=(10,10))
lbp.grid( row=2, column=0, pady=(5,10), padx=(10,10))
lb1.grid( row=3, column=0)
lb2.grid( row=4, column=0)

## Creo las Entradas
searchd = tk.Entry(score,state=tk.DISABLED)
select  = tk.Entry(game,textvariable=choise, state=tk.DISABLED)
name    = tk.Entry(sscore,textvariable=nick, state=tk.DISABLED)

searchd.grid( row=2,column=0, pady=(10,10), padx=(10,10))
select.grid(  row=2,column=0, pady=(10,10), padx=(10,10))
name.grid(    row=1,column=0, pady=(10,10), padx=(10,10))

## Creo los Botones Radio
opt1 = tk.Radiobutton( score, text='Nueva Partida', variable=scoreOpt, value=0, command=activate)
opt2 = tk.Radiobutton( score, text='Cargar Datos',  variable=scoreOpt, value=1, command=activate)

opt1.grid( row=0, column=0)
opt2.grid( row=1, column=0)

## Creo los Botones
button0 = tk.Button( score,  text='Iniciar',  command=iniciar)
button  = tk.Button( score,  text='Examinar', command=exam,     state=tk.DISABLED)
button1 = tk.Button( game,   text='Jugar',    command=jugar,    state=tk.DISABLED)
button2 = tk.Button( sscore, text='Guardar',  command=savefile, state=tk.DISABLED)
close   = tk.Button( root,   text='Salir',    command=closew)

button0.grid( row=0, column=1, padx=(0,10),sticky='ew')
button.grid(  row=2, column=1, padx=(0,10))
button1.grid( row=2, column=1, padx=(0,10))
button2.grid( row=1, column=1, padx=(0,10))
close.grid(   row=6, column=0, pady=(10,10), ipadx=20)

## Grafico
root.mainloop()