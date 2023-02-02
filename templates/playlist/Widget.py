import os
import random
from ctypes import windll
from tkinter import (BOTH, BOTTOM, LEFT, RIGHT, TOP, VERTICAL, Button, Frame,
                     Label, Listbox, PhotoImage, Scrollbar, StringVar, Tk,
                     Toplevel, X, Y, filedialog, ttk)

import _tkinter
from PyPlayer import PlayerMixer as p

from src.Json_Gerency import GerenciadorJson


class PlayListApp:
    
    def __init__(self, *args):
        self.list_audios = p.list_()
        self.icone_app_img = args[0]
        self.fechar_img = args[1]
        self.minimizar_img = args[2]
        self.json_ = GerenciadorJson()
        self.Cores()
        self.Janela_Principal()
        self.raíz.after(10, lambda:self.Configurador_da_Janela(self.raíz))
        self.json_.SetWindow('pl',True)
        self.raíz.mainloop()
    

    def Cores(self):
        self.cor_padrão = self.json_.CurrentColor()
        self.cor_menu = self.json_.CurrentColor()
        self.cor_branca = '#ffffff'


    def Variaveis_Dinamicas(self):
        self.PlayList_Var =  StringVar()
        _ = []
        for x in range(len(self.list_audios)):
            _.append(f"{x+1}-({self.list_audios[x]})")
        self.PlayList_Var.set(_)
        self.CORES = self.json_.CurrentColor()

        
    def Janela_Principal(self):
        self.raíz = Toplevel()
        self.raíz.title("Vínil_Player - PlayList")
        self.raíz.overrideredirect(True)
        self.Centralizador()
        self.Variaveis_Dinamicas()
        self.raíz.minimized = True;
        self.raíz.maximizar = False;
        self.raíz.config(bg=self.cor_menu)
        self.raíz.iconbitmap("static/img/icons/icone2.ico")
        #-------------------------------------------------------------
        #--> Barra de titulo da aplicação
        #--> Title-bar of application
        self.barra_de_titulo = Label(self.raíz,bg=self.cor_menu,relief='raised',bd=0,highlightthickness=0)
        #-------------------------------------------------------------
        self.btn_fechar = Button(self.barra_de_titulo,image=self.fechar_img,command=self.Closed,bg=self.cor_menu,padx=1,pady=1,font=("Calibri", 12),bd=0,fg=self.cor_branca,highlightthickness=0,cursor='hand2',activebackground=self.cor_menu)
        self.btn_minimizar = Button(self.barra_de_titulo,image=self.minimizar_img,command=self.Minimisar_Janela,bg=self.cor_menu,padx=1,pady=1,bd=0,fg=self.cor_branca,font=("Calibri", 12),highlightthickness=0,cursor='hand2',activebackground=self.cor_menu)
        self.icone_da_app_ = Label(self.barra_de_titulo,image=self.icone_app_img[self.json_.CurrentIcone()],bg=self.cor_menu)
        self.titulo_da_app = Label(self.barra_de_titulo,text='Vínil_Player - PlayList',font='Georgia 8',fg=self.cor_branca,bg=self.cor_menu)
        #-------------------------------------------------------------
        #--> Cria o corpo da aplicação
        #--> Create body of application
        self.janela = Frame(self.raíz,bg=self.cor_padrão,highlightthickness=0)
        #-------------------------------------------------------------
        #--> Cria as barras da aplicação
        #--> Create bars of application
        self.barra_do_software_R = Frame(self.janela,bg=self.cor_menu,cursor='sb_h_double_arrow')#--> Right bar
        self.barra_do_software_L = Frame(self.janela,bg=self.cor_menu,cursor='sb_h_double_arrow')#--> Left bar
        self.barra_do_software_B = Frame(self.janela,bg=self.cor_menu,cursor='sb_v_double_arrow')#--> Bottom bar
        #-------------------------------------------------------------
        #--> Definição do evento bind da aplicação
        #--> Definition of Tocador bin of window
        self.raíz.bind("<FocusIn>",self.Desminimisar_Janela)
        self.barra_de_titulo.bind('<Button-1>',self.Pegar_Posicao)
        self.titulo_da_app.bind('<Button-1>',self.Pegar_Posicao)
        #-------------------------------------------------------------
        #--> Definição das posições dos widgets na janela
        #--> Definition of positions of widgtes in window
        self.barra_de_titulo.pack(side=TOP,fill=X,pady=0)
        self.janela.pack(expand=1,fill=BOTH)
        self.btn_fechar.pack(side=RIGHT,ipadx=7,ipady=1)
        self.btn_minimizar.pack(side=RIGHT,ipadx=7,ipady=1)
        self.icone_da_app_.pack(side=LEFT)
        self.titulo_da_app.pack(side=LEFT)
        self.barra_do_software_R.pack(side=RIGHT,ipadx=2,ipady=2,fill=Y)
        self.barra_do_software_L.pack(side=LEFT,ipadx=2,ipady=2,fill=Y)
        self.barra_do_software_B.pack(side=BOTTOM,ipadx=2,ipady=2,fill=X)
        #-------------------------------------------------------------
        self.janela.after(1000,self.Actualizacoes)
        self.Estrutura_do_Software()

    
    def Centralizador(self): #Centraliza a janela no meio da tela
        spaceX = (self.raíz.winfo_screenwidth()/2)-(270/2)
        spaceY = (self.raíz.winfo_screenheight()/2)-(300/2)
        self.raíz.geometry('270x300+%i+%i'%(spaceX,spaceY))
    
    
    def Configurador_da_Janela(self,mainWindow): #Configura a janela para ter a aparência customizada
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080	   
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda:mainWindow.wm_deiconify())
    

    def Minimisar_Janela(self): #Minimiza a aplicação
        self.raíz.attributes("-alpha",0)
        self.raíz.minimized = True      


    def Desminimisar_Janela(self,event): #Torna a janela visivel
        self.raíz.attributes("-alpha",1)
        if self.raíz.minimized == True:
            self.raíz.minimized = False
            
    
    def Estrutura_do_Software(self): #Estrutura o software

        if len(self.list_audios) < 10:
            faixas = f"0{len(self.list_audios)}"
        else: faixas = len(self.list_audios)

        self.Titulo = Label(self.janela,bg=self.cor_padrão,fg=self.cor_branca,font=('Calibri 9'),
        text=f'PlayList: {faixas} Faixas')

        self.Titulo.place(x=5,y=3)
        
        self.body_list = Listbox(self.janela,bg=self.cor_menu,fg=self.cor_branca,border=0,
        borderwidth=0,highlightbackground="#f9f9f9",highlightcolor="#f9f9f9",highlightthickness=0.5,
        exportselection=1,selectbackground=self.cor_menu,selectborderwidth=0,selectforeground=self.cor_branca,
        listvariable=self.PlayList_Var,height=8,justify='left',activestyle='dotbox')

        self.ScrollBar_ = Scrollbar(self.janela,orient=VERTICAL,command=self.body_list.yview,border=0.5,
        bg=self.cor_padrão,jump=False,activebackground=self.cor_menu,elementborderwidth=0,highlightthickness=1,
        highlightbackground=self.cor_padrão,highlightcolor=self.cor_branca,troughcolor=self.cor_menu,
        width=15)
        
        self.body_list.bind('<<ListboxSelect>>',self.Carregar_Musica)
        self.body_list.config(yscrollcommand=self.ScrollBar_.set)
        self.body_list.place(x=5,relwidth=0.92,y=27,relheight=0.88)
        self.ScrollBar_.place(x=238,y=28,relheight=0.875)
    
    
    def Pegar_Posicao(self,event):
        if self.raíz.maximizar == False:
            xwin = self.raíz.winfo_x()
            ywin = self.raíz.winfo_y()
            Xinicial = event.x_root
            Yinicial = event.y_root
            ywin = ywin - Yinicial
            xwin = xwin - Xinicial

            def Movedor_da_Janela(event):
                self.raíz.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
            def Fixador_da_Janela(event):
                self.raíz.config(cursor="arrow")

            self.barra_de_titulo.bind('<B1-Motion>',Movedor_da_Janela)
            self.barra_de_titulo.bind('<ButtonRelease-1>',Fixador_da_Janela)
            self.titulo_da_app.bind('<B1-Motion>',Movedor_da_Janela)
            self.titulo_da_app.bind('<ButtonRelease-1>',Fixador_da_Janela)
        else:
            self.raíz.maximizar = not self.raíz.maximizar


    def Carregar_Musica(self,event):
        try:
            string = self.body_list.get(self.body_list.curselection())
            file_ = string[string.find('(')+1:string.rfind(')')]
            p.load(file=f"{p.getpath()}{file_}",loading=True)
            p.play()
        except _tkinter.TclError:
            pass


    def Actualizacoes(self):
        if len(self.list_audios) != len(p.list_()):
            self.list_audios = p.list_()
            self.Variaveis_Dinamicas()
            self.cor_menu = self.json_.CurrentColor()
            self.cor_padrão = self.json_.CurrentColor()
            self.Estrutura_do_Software()
        else:
            if self.CORES != self.json_.CurrentColor():
                self.Titulo['bg'] = self.json_.CurrentColor()
                self.body_list.configure(
                    bg=self.json_.CurrentColor(),
                    selectbackground=self.json_.CurrentColor()
                )
                self.janela['bg'] = self.json_.CurrentColor()
                self.barra_de_titulo['bg'] = self.json_.CurrentColor()
                self.btn_fechar['bg'] = self.json_.CurrentColor()
                self.btn_minimizar['bg'] = self.json_.CurrentColor()
                self.btn_fechar['activebackground'] = self.json_.CurrentColor()
                self.btn_minimizar['activebackground'] = self.json_.CurrentColor()
                self.icone_da_app_['bg'] = self.json_.CurrentColor()
                self.icone_da_app_['image'] = self.icone_app_img[self.json_.CurrentIcone()]
                self.barra_do_software_B['bg'] = self.json_.CurrentColor()
                self.barra_do_software_L['bg'] = self.json_.CurrentColor()
                self.barra_do_software_R['bg'] = self.json_.CurrentColor()
                self.titulo_da_app['bg'] = self.json_.CurrentColor()
                self.CORES = self.json_.CurrentColor()
        self.janela.after(100,self.Actualizacoes)


    def Closed(self):
        self.json_.SetWindow('pl',False)
        self.raíz.destroy()


if __name__ == '__main__':
    PlayListApp()