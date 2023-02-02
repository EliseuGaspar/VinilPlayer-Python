import random
import webbrowser as web
from ctypes import windll
from time import sleep
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from PyPlayer import PlayerMixer as p

from src.Json_Gerency import GerenciadorJson
from templates.abrir import LabelAbrir
from templates.info_tags import LabelInfo
from templates.playlist import PlayListApp


class MainApplication():

    def __init__(self , ):
        self.json = GerenciadorJson()
        self.Cores()
        self.Janela()
        self.json.ChangeCurrentColor(self.cor_padrao)
        self.json.ChangeCurrentIcone(0)
        self.json.SetWindow('la',False)
        self.json.SetWindow('li',False)
        self.json.SetWindow('pl',False)
        self.REPEAT = self.json.Window('re')
        self.raiz.after(10, lambda:self.Configurador_da_Janela(self.raiz))
        self.raiz.mainloop()
    
    def Cores(self ,):
        self.cor_padrao = '#0b0b0d'
        self.cor_padrao2 = '#1b2431'
        self.cor_padrao3 = '#22272e'
        self.cor_menu = '#1c1d22'
        self.cor_texto = '#f0e9ee'
        self.cor_texto_hover = '#2f005f'
        self.cor_laranga = '#ffa600'
        self.cor_aqua = '#10213a'
        self.cor_violeta = '#791f71'
        self.cor_branca = '#ffffff'
        self.cor_branca2 = '#eeeeeee'
        self.cor_sinza = '#dddddd'
        self.cor_preta = '#000000'
        self.cor_preta2 = '#111111'
        self.cor_castanha_preta = '#444444'

    def Variaveis_Dinamicas(self ,):
        self.boolean_volume = False
        self.boolean_stop = False
        self.titulo_rotacao = False
        self._X = 250
        self.boolean_corpo_da_app = False
        self.recentes_diretorios = StringVar()
        self.active_file = None
        self.playlist = None
        self.REPEAT = 0
        self.COR = self.cor_padrao
        self.ABRIR = False

    def Imagens(self ,):
        self.DIR_ICONES = "static/img/icons/"
        self.DIR_MODELS = "static/img/models/"
        self.DIR_FUNDOS = "static/img/fundos/"

        self.img_icone_app = [PhotoImage(file=f"{self.DIR_ICONES}%i.png"%(i)) for i in range(1,5)]
        self.img_fechar = PhotoImage(file=f"{self.DIR_ICONES}fechar.png")
        self.img_minimizar = PhotoImage(file=f"{self.DIR_ICONES}minimizar.png")
        self.img_sem_musicas = [PhotoImage(file=f"{self.DIR_MODELS}sem_musica%i.png"%(i)) for i in range(2)]
        self.img_capas = [PhotoImage(file=f"{self.DIR_FUNDOS}img%i.png"%(i)) for i in range(1,5)]
        self.icone_bar = PhotoImage(file=f"{self.DIR_ICONES}bar.png")
        self.icone_tocar = PhotoImage(file=f"{self.DIR_ICONES}play2.png")
        self.icone_proximo = PhotoImage(file=f"{self.DIR_ICONES}prox.png")
        self.icone_pausar = PhotoImage(file=f"{self.DIR_ICONES}pause.png")
        self.icone_anterior = PhotoImage(file=f"{self.DIR_ICONES}ant.png")
        self.icone_volume = PhotoImage(file=f"{self.DIR_ICONES}volumee.png")
        self.icone_repetir = PhotoImage(file=f"{self.DIR_ICONES}loop.png")
        self.icone_repetir2 = PhotoImage(file=f"{self.DIR_ICONES}loop2.png")
        self.icone_repetir3 = PhotoImage(file=f"{self.DIR_ICONES}loop3.png")
        self.icone_parar = PhotoImage(file=f"{self.DIR_ICONES}parar.png")
        self.icone_sobre = PhotoImage(file=f"{self.DIR_ICONES}sobre.png")
        self.icone_bar_down = PhotoImage(file=f"{self.DIR_ICONES}bar.png")
        self.icone_bar_up = PhotoImage(file=f"{self.DIR_ICONES}bar2.png")
        #-------------------------- Imagens Hover ---------------------------#
        self.icone_volume_fechado = PhotoImage(file=f"{self.DIR_ICONES}volumee2.png")

        if self.json.Window('re') == 0:
            self.icone_repetir_ = self.icone_repetir
        elif self.json.Window('re') == 1:
            self.icone_repetir_ = self.icone_repetir2
            self.REPEAT = 1
        else:
            self.icone_repetir_ = self.icone_repetir3
            self.REPEAT = 2

    def Janela(self ,):
        # ... Estruturação da janela Tk()
        self.raiz = Tk()
        self.Imagens()
        self.raiz.configure(bg=self.cor_padrao)
        self.raiz.title('Vínil Player 1.0.0')
        self.raiz.iconbitmap(f"{self.DIR_ICONES}icone2.ico")
        self.raiz.overrideredirect(True)
        self.raiz.minimized = True
        self.raiz.maximizar = False
        self.Centralizador()
        self.Variaveis_Dinamicas()
        #-------------------------------------------------------------
        #--> Barra de titulo da aplicação
        #--> Title-bar of application
        self.barra_de_titulo = Label(self.raiz,bg=self.cor_menu,relief='raised',bd=0,highlightthickness=0)
        #-------------------------------------------------------------
        self.btn_fechar = Button(self.barra_de_titulo,image=self.img_fechar,command=self.Evento_Exit,bg=self.cor_menu,padx=1,pady=1,font=("Calibri", 12),bd=0,fg=self.cor_branca,highlightthickness=0,cursor='hand2',activebackground=self.cor_menu)
        self.btn_minimizar = Button(self.barra_de_titulo,image=self.img_minimizar,command=self.Minimisar_Janela,bg=self.cor_menu,padx=1,pady=1,bd=0,fg=self.cor_branca,font=("Calibri", 12),highlightthickness=0,cursor='hand2',activebackground=self.cor_menu)
        self.icone_da_app_ = Label(self.barra_de_titulo,image=self.img_icone_app[0],bg=self.cor_menu)
        self.titulo_da_app = Label(self.barra_de_titulo,text='Vínil_Player',font='Georgia 8',fg=self.cor_branca,bg=self.cor_menu)
        #-------------------------------------------------------------
        #--> Cria o corpo da aplicação
        #--> Create body of application
        self.janela = Frame(self.raiz,bg=self.cor_padrao,highlightthickness=0)
        #-------------------------------------------------------------
        #--> Cria as barras da aplicação
        #--> Create bars of application
        self.barra_do_software_R = Frame(self.janela,bg=self.cor_menu,cursor='sb_h_double_arrow')#--> Right bar
        self.barra_do_software_L = Frame(self.janela,bg=self.cor_menu,cursor='sb_h_double_arrow')#--> Left bar
        self.barra_do_software_B = Frame(self.janela,bg=self.cor_menu,cursor='sb_v_double_arrow')#--> Bottom bar
        #-------------------------------------------------------------
        #--> Definição do evento bind da aplicação
        #--> Definition of Tocador bin of window
        self.raiz.bind("<FocusIn>",self.Desminimisar_Janela)
        self.barra_de_titulo.bind('<Button-1>',self.Pegar_Posicao)
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
        self.Inicializador()

    def Centralizador(self ,):
        self.X = (self.raiz.winfo_screenwidth()/2) - (600/2)
        self.Y = (self.raiz.winfo_screenheight()/2) - (300/2)
        self.raiz.geometry("600x300+%d+%d"%(self.X,self.Y))

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
        self.raiz.attributes("-alpha",0)
        self.raiz.minimized = True      

    def Desminimisar_Janela(self,event): #Torna a janela visivel
        self.raiz.attributes("-alpha",1)
        if self.raiz.minimized == True:
            self.raiz.minimized = False

    def Pegar_Posicao(self,event):
        if self.raiz.maximizar == False:
            xwin = self.raiz.winfo_x()
            ywin = self.raiz.winfo_y()
            Xinicial = event.x_root
            Yinicial = event.y_root
            ywin = ywin - Yinicial
            xwin = xwin - Xinicial

            def Movedor_da_Janela(event):
                self.raiz.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
            def Fixador_da_Janela(event):
                self.raiz.config(cursor="arrow")

            self.barra_de_titulo.bind('<B1-Motion>',Movedor_da_Janela)
            self.barra_de_titulo.bind('<ButtonRelease-1>',Fixador_da_Janela)
        else:
            self.raiz.maximizar = not self.raiz.maximizar

    def Inicializador(self ,): 
        if self.json.UltimaLista() == []:
            self.Sem_Musicas()
        else:
            self.Caminhos_Recentes()
    
    def Sem_Musicas(self): #Apresentada quando não há dados dos caminhos recentes
    
        self.label_sem_musicas = Label(self.janela,bg=self.cor_padrao,image=self.img_sem_musicas[0],cursor='hand2')
        self.label_sem_musicas.bind('<Leave>',self.Evento_Sem_Musica_hover)
        self.label_sem_musicas.bind('<Enter>',self.Evento_Sem_Musica_)
        self.label_sem_musicas.bind('<Button-1>',self.Evento_Pegar_Musicas)
        self.label_sem_musicas.place(relx=0.3,rely=0.25)
    
    def Caminhos_Recentes(self): #Apresentada quando há dados dos caminhos recentes
        Diretorios = self.json.UltimaLista()
        self.recentes_diretorios.set(Diretorios)
        self.caixa_de_lista_label = Label(self.janela,bg=self.cor_padrao,fg=self.cor_sinza,font='Georgia 13',text='Caminhos Recentes')
        self.caixa_de_lista_label.place(relx=0.37,rely=0.17)
        self.caixa_de_lista = Listbox(self.janela,bg=self.cor_padrao,fg=self.cor_sinza,border=0,
        borderwidth=0,highlightbackground=self.cor_padrao,highlightcolor=self.cor_padrao,highlightthickness=0.5,
        exportselection=1,selectbackground=self.cor_castanha_preta,selectborderwidth=0,selectforeground=self.cor_sinza,
        listvariable=self.recentes_diretorios,height=8,justify='left',activestyle='dotbox')
        self.caixa_de_lista.bind('<<ListboxSelect>>',self.Evento_Colocar_Diretorio)
        self.caixa_de_lista.place(relx=0.06,rely=0.3,relheight=0.45,relwidth=0.87)

        self.botao = Button(master=self.janela,bg=self.cor_preta,fg=self.cor_sinza,text='Buscar Músicas',
        border=0,font='Georgia 9',activebackground=self.cor_preta,cursor='hand2')
        self.botao2 = Button(master=self.janela,bg=self.cor_preta,fg=self.cor_sinza,text='Buscar Música',
        border=0,font='Georgia 9',activebackground=self.cor_preta,command=self.Evento_Pegar_Musica,cursor='hand2')
        self.botao3 = Button(master=self.janela,bg=self.cor_preta,fg=self.cor_sinza,text='Limpar Lista',
        border=0,font='Georgia 9',activebackground=self.cor_preta,command=self.Evento_Limpar_Cache,cursor='hand2')
        self.botao.bind('<Button-1>',self.Evento_Pegar_Musicas)
        self.botao.place(relx=0.15,rely=0.8,relwidth=0.2,relheight=0.11)
        self.botao2.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.11)
        self.botao3.place(relx=0.65,rely=0.8,relwidth=0.2,relheight=0.11)

    def Estrutura(self ,):
        self.First_PlaceForget()

        self.barra_de_titulo.config(bg=self.cor_padrao)
        self.barra_do_software_B.config(bg=self.cor_padrao)
        self.barra_do_software_L.config(bg=self.cor_padrao)
        self.barra_do_software_R.config(bg=self.cor_padrao)
        self.icone_da_app_.config(bg=self.cor_padrao)
        self.btn_fechar.config(bg=self.cor_padrao)
        self.btn_minimizar.config(bg=self.cor_padrao)
        
        """ Menu do Player de Áudio """
        
        self.btn_abrir = Button(self.barra_de_titulo,bg=self.cor_padrao,text='Abrir',fg=self.cor_texto,activebackground=self.cor_padrao,activeforeground=self.cor_texto,font='Calibri 9',cursor='hand2',border=0,command=lambda:self.Evento_Templates('abrir'))
        self.btn_playlist = Button(self.barra_de_titulo,bg=self.cor_padrao,text='Playlist',fg=self.cor_texto,activebackground=self.cor_padrao,activeforeground=self.cor_texto,font='Calibri 9',cursor='hand2',border=0,command=lambda:self.Evento_Templates('playlist'))
        self.btn_ajuda = Button(self.barra_de_titulo,bg=self.cor_padrao,text='Ajuda',fg=self.cor_texto,activebackground=self.cor_padrao,activeforeground=self.cor_texto,font='Calibri 9',cursor='hand2',border=0,command=lambda:web.open('https://df-elsu.tk/softwares/vinilplayer/suport'))
        self.btn_sair = Button(self.barra_de_titulo,bg=self.cor_padrao,text='Sair',fg=self.cor_texto,activebackground=self.cor_padrao,activeforeground=self.cor_texto,font='Calibri 9',cursor='hand2',border=0,command=self.Evento_Exit)
        self.btn_abrir.place(rely=0.19,relx=0.08)
        self.btn_playlist.place(rely=0.19,relx=0.16)
        self.btn_ajuda.place(rely=0.19,relx=0.26)
        self.btn_sair.place(rely=0.19,relx=0.35)

        """ Zona esquerda do Player """

        self.Label_Capa = Label(self.janela,bg=self.cor_padrao,border=0.5,cursor='hand2',image=self.img_capas[2])#-->   Label que exibe as imagens do player
        self.Label_Capa.after(10000,self.Evento_Troca_De_Capa)
        self.Label_Capa.place(relx=0.05,rely=0.18)

        #--> Este bloco contém o botão do volume e o slider também
        #---------------------------------------------------------
        #--> Botão que muda o estado do audio activado/desactivado
        self.btn_volume = Button(self.janela,bg=self.cor_padrao,activebackground=self.cor_padrao,border=0,cursor='hand2',image=self.icone_volume)
        self.btn_volume.bind('<Enter>',self.Evento_BarSom_Visivel)
        self.btn_volume.bind('<Leave>',self.Evento_BarSom_Invisivel)
        self.btn_volume.bind('<Button-1>',self.Evento_Mudanca_de_Volume)
        self.btn_volume.place(relx=-0.02,rely=0.88,relwidth=0.089)
        #--> Botão que muda o estado do slider visivel/invisivel
        self.btn_volume_bar = Button(self.btn_volume,bg=self.cor_padrao,activebackground=self.cor_padrao,border=0,cursor='hand2',command=lambda:self.Evento_Transparencia_SlideVolume(True))
        self.btn_volume_bar.place(relx=0.65,rely=0)
        #--> Slider de controle do volume do player
        self.slider_do_volume = ttk.Scale(self.janela,to=100,from_=0,cursor='hand2',length=100,value=self.json.Window('vol'),command=self.Volume,orient='vertical')
        self.slider_do_volume.place(relx=-0.05,rely=-0.15)

        """ Zona direita do Player """

        #--> Este bloco contém os widgets para controle do player
        #---------------------------------------------------------
        #--> Label que mostra a faixa atual
        #--> Label display current audio title
        self.Label_Faixa_atual = Label(self.janela,bg=self.cor_padrao)
        self.Label_Faixa_atual.place(relx=0.44,rely=0.17,relheight=0.09,relwidth=0.41)
        self.Faixa_atual = Label(self.Label_Faixa_atual,bg=self.cor_padrao,fg=self.cor_branca,font='Calibri 10',justify=CENTER,padx=15)
        self.Faixa_atual.place(x=250,width=470)
        #---------------------------------------------------------
        #--> Slider de controle do tempo do audio
        #--> Slider of audio time controler
        self.slider_do_audio = ttk.Scale(self.janela,cursor='hand2',from_=0,to=99.9,length=250,command=self.Evento_TempoAtual_do_Audio)
        self.slider_do_audio.after(990,self.Evento_Atualizacoes)
        self.slider_do_audio.place(relx=0.44,rely=0.35,relheight=0.09)
        self.style = ttk.Style(self.janela)
        self.style.configure('TScale',background=self.cor_padrao,)
        #---------------------------------------------------------
        #--> Botão de Tocar & Pausar
        #--> Button Play and Pause
        self.btn_tocar = Button(self.janela,bg=self.cor_padrao,activebackground=self.cor_padrao,border=0,cursor='hand2',image=self.icone_pausar)
        self.btn_tocar.bind('<Button-1>',self.Evento_Mudanca_de_Play)
        self.btn_tocar.place(relx=0.62,rely=0.55)
        #---------------------------------------------------------
        #--> Botão próxima música
        #--> Button next music
        self.btn_proximo = Button(self.janela,bg=self.cor_padrao,border=0,activebackground=self.cor_padrao,cursor='hand2',image=self.icone_proximo,command=lambda:self.Evento_de_Mudanca_Faixa('pro'))
        self.btn_proximo.place(relx=0.77,rely=0.55)
        #---------------------------------------------------------
        #--> Botão música anterior
        #--> Button Faixa_Anterior music
        self.btn_anterior = Button(self.janela,bg=self.cor_padrao,border=0,activebackground=self.cor_padrao,cursor='hand2',image=self.icone_anterior,command=lambda:self.Evento_de_Mudanca_Faixa('ant'))
        self.btn_anterior.place(relx=0.47,rely=0.55)
        #---------------------------------------------------------
        #--> Botão Sobre o Software
        #--> Button About Software
        self.btn_sobre = Button(self.janela,bg=self.cor_padrao,border=0,activebackground=self.cor_padrao,cursor='hand2',image=self.icone_sobre,command=lambda:self.Evento_Templates('sobre'))
        self.btn_sobre.place(relx=0.93,rely=0.27)
        #---------------------------------------------------------
        #--> Botão repetir música
        #--> Button repeat music
        self.btn_repetir = Button(self.janela,bg=self.cor_padrao,border=0,activebackground=self.cor_padrao,cursor='hand2',image=self.icone_repetir_,command=self.Evento_Repetir)
        self.btn_repetir.place(relx=0.93,rely=0.47)
        #---------------------------------------------------------
        #--> Botão reiniciar música
        #--> Button stop player
        self.btn_parar = Button(self.janela,bg=self.cor_padrao,border=0,activebackground=self.cor_padrao,cursor='hand2',image=self.icone_parar,command=self.Evento_Parar_)
        self.btn_parar.place(relx=0.93,rely=0.64)
        #---------------------------------------------------------
        #--> Placar com número da faixa atual e o número total de músicas
        #--> Placar with current audio number and full number audios
        self.label_placar = Label(self.janela,text=None,bg=self.cor_padrao,fg=self.cor_texto,font='Calibri 10')
        self.label_placar.place(relx=0.07,rely=0.875)
        self.boolean_corpo_da_app = True
        #---------------------------------------------------------
        #--> Placar com o estado do audio pausado/tocando
        #--> Placar with state player paused/playing
        self.label_estado = Label(self.janela,text='Estado: ?',bg=self.cor_padrao,fg=self.cor_texto,font='Calibri 10',)
        self.label_estado.place(relx=0.17,rely=0.875)
        #---------------------------------------------------------
        #--> Placar com a percentagem atual do volume do audio
        #--> Placar with current percent of volume player
        self.label_volume = Label(self.janela,text=f'Volume: {self.json.Window("vol")}%',bg=self.cor_padrao,fg=self.cor_texto,font='Calibri 10',)
        self.label_volume.place(relx=0.37,rely=0.875)
        #---------------------------------------------------------
        #--> Placar com o estado de tempo da audio [corrente/total]
        #--> Placar with state of time of audio [current/size_full]
        self.label_tempo = Label(self.janela,text='Tempo: 00:00 / 00:00',bg=self.cor_padrao,fg=self.cor_texto,font='Calibri 10',)
        self.label_tempo.place(relx=0.54,rely=0.875)

        self.barra_de_titulo.after(50,self.Evento_Atualizar_Barra_de_Titulo)
    
    def First_PlaceForget(self ,): #Destroi os widgets dos methods Sem_Musicas e Caminhos_Recentes
        try:
            self.label_sem_musicas.place_forget()
        except: pass
        try:
            self.titulo_da_app.pack_forget()
        except: pass
        try:
            self.caixa_de_lista.place_forget()
            self.caixa_de_lista_label.place_forget()
            self.botao.place_forget()
            self.botao2.place_forget()
            self.botao3.place_forget()
        except: pass


    #------------------------> Zona de Eventos <---------------------------------

    
    def Evento_Sem_Musica_(self,event):
        self.label_sem_musicas.config(
            image=self.img_sem_musicas[1]
        )
    
    def Evento_Sem_Musica_hover(self,event):
        self.label_sem_musicas.config(
            image=self.img_sem_musicas[0]
        )
    
    def Evento_Pegar_Musicas(self,event):
        self.diretorio = filedialog.askdirectory(initialdir='Music',title='Buscar Músicas')
        if self.diretorio:
            resultado = p.load(dir=self.diretorio)
            if resultado == False:
                messagebox.showinfo(
                    title='Falha ao pegar arquivos',
                    message='O diretório introduzido não possui nenhum arquivo .mp3'
                )
            else:
                if self.json.AdicionarLista(self.diretorio):
                    self.Estrutura()
                else:
                    messagebox.showinfo(
                            "Erro ao registrar diretório!",
                            f"Houve um erro ao registrar o diretório {self.diretorio}\nTentando de Novo!"
                        )
                    self.Evento_Pegar_Musicas(event)
                try: 
                    p.play()
                    p.setvolume((self.json.Window('vol')/100))
                except: pass
        else:
            pass

    def Evento_Pegar_Musica(self):
        self.diretorio = filedialog.askopenfilename(initialdir='Music',title='Buscar Música')
        if self.diretorio:
            p.load(file=self.diretorio)
            self.Estrutura()
            p.play()
            p.setvolume((self.json.Window('vol')/100))
        else:
            pass

    def Evento_Colocar_Diretorio(self,event):
        indice = self.caixa_de_lista.curselection()
        try: 
            string = self.caixa_de_lista.get(indice)
            diretorio = string
            resultado = p.load(dir=diretorio)
            if resultado == False:
                messagebox.showinfo(
                    title='Falha ao pegar arquivos',
                    message='O diretório introduzido não possui nenhum arquivo .mp3'
                )
            else:
                self.Estrutura()
                try: 
                    p.play()
                    p.setvolume((self.json.Window('vol')/100))
                except: pass
        except: pass

    def Evento_Atualizar_Barra_de_Titulo(self):
        self.icone_da_app_['fg'] = '#ddd'
        self.btn_abrir.config(text='Abrir');
        self.btn_playlist.config(text='Playlist')
        self.btn_ajuda.config(text='Ajuda')
        self.btn_sair.config(text='Sair')
        self.btn_fechar.config(image=self.img_fechar)
        self.btn_minimizar.config(image=self.img_minimizar)
        self.Label_Faixa_atual['justify'] = CENTER
        self.Faixa_atual['justify'] = CENTER
        if(len(p.current_file()) > 36):
            self.titulo_rotacao = True
            self.Faixa_atual['text'] = p.current_file()
        else:
            self.titulo_rotacao = False
            self._X = 250
            self.Faixa_atual.place(x=-70,width=400)

        self.barra_de_titulo.after(50,self.Evento_Atualizar_Barra_de_Titulo)

    def Evento_Mudanca_de_Play(self,event):
        if self.btn_tocar['image'] == 'pyimage16':
            self.btn_tocar['image'] = self.icone_tocar
            p.pause()
            self.label_estado['text'] = 'Estado: Pausado.'
        else:
            self.btn_tocar['image'] = self.icone_pausar
            p.unpause()
            self.label_estado['text'] = 'Estado: Tocando.'
        if self.boolean_stop == True:
            p.play()
            self.btn_tocar['image'] = self.icone_pausar
            self.boolean_stop = False
            self.label_estado['text'] = 'Estado: Tocando.'
 
    def Evento_Parar_(self):
        self.boolean_stop = True
        p.stop()
        self.btn_tocar['image'] = self.icone_tocar
        self.label_estado['text'] = 'Estado: Parado.'
   
    def Evento_de_Mudanca_Faixa(self,valor):
        if valor == 'pro':
            if p.playing():
                self.label_estado['text'] = 'Estado: Tocando.'
                p.next_()
                self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
                self.Faixa_atual['text'] = p.current_file()
            else:
                self.btn_tocar['image'] = self.icone_pausar
                self.label_estado['text'] = 'Estado: Pausado.'
                p.next_()
                self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
                self.Faixa_atual['text'] = p.current_file()
        elif valor == 'ant':
            if p.playing():
                self.label_estado['text'] = 'Estado: Tocando.'
                p.back()
                self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
                self.Faixa_atual['text'] = p.current_file()
            else:
                self.btn_tocar['image'] = self.icone_pausar
                self.label_estado['text'] = 'Estado: Pausado.'
                p.back()
                self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
                self.Faixa_atual['text'] = p.current_file()
        else:
            self.placar = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
            self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
            self.Faixa_atual['text'] = p.current_file()
    
    def Evento_BarSom_Visivel(self,event):
        self.btn_volume_bar['image'] = self.icone_bar
    
    def Evento_BarSom_Invisivel(self,event):
        self.btn_volume_bar['image'] = None
    
    def Evento_Mudanca_de_Volume(self,event):
        if self.btn_volume['image'] == 'pyimage18':
            self.btn_volume['image'] = self.icone_volume_fechado
            self.label_estado['text'] = 'Estado: Silenciado.'
            p.setvolume(0.0)
        else:
            self.btn_volume['image'] = self.icone_volume
            p.setvolume(self.slider_do_volume['value']/100)
            if p.playing():
                self.label_estado['text'] = 'Estado: Tocando.'
            else:
                self.label_estado['text'] = 'Estado: Pausado.'
    
    def Evento_Transparencia_SlideVolume(self,bool):
        if self.boolean_volume != bool:
            self.slider_do_volume.place(relx=0.01,rely=0.22,relheight=0.5,relwidth=0.03)
            self.boolean_volume = True
        else:
            self.slider_do_volume.place(relx=-0.05,rely=-0.15)
            self.boolean_volume = False
    
    def Volume(self,event):
        valor = int(self.slider_do_volume.get())
        self.label_volume['text'] = f'Volume: {valor}%'
        p.setvolume((valor/100))
        self.btn_volume['image'] = self.icone_volume
    
    def Evento_Atualizacoes(self):
        position = 0
        if(p.duration('size')):
            position = (p.current_time('size',controler=True) * (100 / p.duration('size')))
        self.slider_do_audio['value'] = position
        current_time = p.current_time(type_='time',controler=True,repeat=True)
        if current_time == True: current_time = '00:00'
        self.label_tempo['text'] = f"Tempo: {current_time} / {p.duration(type_='time')}"
        if p.playing():
            self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
            self.Label_Faixa_atual['justify'] = CENTER
            self.Faixa_atual['text'] = p.current_file()
            self.label_estado['text'] = 'Estado: Tocando.'
            self.btn_tocar['image'] = self.icone_pausar
            if(self.titulo_rotacao):
                self._X -= 10
                if(self._X <= -400):
                    self._X = 250
                self.Faixa_atual.place(x=self._X)
                self.Faixa_atual['text'] = p.current_file()
        else:
            self.label_placar['text'] = f"{self.Evento_Current_File()}/{str(len(p.list_()))}"
            self.Label_Faixa_atual['justify'] = CENTER
            self.Faixa_atual['text'] = p.current_file()
            self.label_estado['text'] = 'Estado: Pausado.'
        if p.current_time(controler=True,repeat=True) == True:
            if self.REPEAT == 0:
                self.Evento_de_Mudanca_Faixa('pro')
            elif self.REPEAT  == 1:
                if self.Evento_Current_File() != len(p.list_()):
                    self.Evento_de_Mudanca_Faixa('pro')
            else:
                p.load(file=f"{p.getpath()}{p.current_file()}",loading=True)
            sleep(0.3)
            if not p.playing():
                self.Evento_Parar_()
        self.slider_do_audio.after(980,self.Evento_Atualizacoes)
     
    def Evento_Current_File(self):
        current_file = p.current_file()
        for x in range(len(p.list_())):
            if current_file == p.list_()[x]:
                return x+1
    
    def Evento_TempoAtual_do_Audio(self,event):
        value = int(self.slider_do_audio.get())
        current_time = (p.duration(type_ = 'size') * (value / 100))
        p.settime(current_time)
        position = 0
        if(p.duration('size')):
            position = (p.current_time('size',controler=True) * (100 / p.duration('size')))

    def Evento_Troca_De_Capa(self):
        if p.playing():
            self.index = random.randint(0,3)
            self.img_capas2 = self.img_capas[self.index]
            self.Label_Capa['image'] = self.img_capas2
            self.icone_da_app_['image'] = self.img_icone_app[self.index]
            
            if self.index == 0:
                self.COR = self.cor_menu
                #---------------------------------------------------
                self.raiz.config(bg=self.cor_menu)
                self.janela.config(bg=self.cor_menu,
                highlightbackground=self.cor_menu)
                self.barra_de_titulo.config(bg=self.cor_menu)
                self.barra_de_titulo.config(bg=self.cor_menu)
                self.barra_de_titulo.config(bg=self.cor_menu)
                self.barra_de_titulo.config(bg=self.cor_menu)
                self.barra_do_software_B['bg'] = self.cor_menu
                self.barra_do_software_L['bg'] = self.cor_menu
                self.barra_do_software_R['bg'] = self.cor_menu
                self.Label_Faixa_atual['bg'] = self.cor_menu
                self.Faixa_atual['bg'] = self.cor_menu
                self.btn_fechar['bg'] = self.cor_menu
                self.btn_minimizar['bg'] = self.cor_menu
                self.icone_da_app_['bg'] = self.cor_menu
                self.titulo_da_app['bg'] = self.cor_menu
                self.label_estado['bg'] = self.cor_menu
                self.label_volume['bg'] = self.cor_menu
                self.btn_anterior['bg'] = self.cor_menu
                self.btn_repetir['bg'] = self.cor_menu
                self.btn_proximo['bg'] = self.cor_menu
                self.btn_volume_bar['bg'] = self.cor_menu
                self.btn_volume['bg'] = self.cor_menu
                self.btn_sobre['bg'] = self.cor_menu
                self.btn_tocar['bg'] = self.cor_menu
                self.btn_parar['bg'] = self.cor_menu
                self.btn_abrir['bg'] = self.cor_menu
                self.btn_ajuda['bg'] = self.cor_menu
                self.btn_sair['bg'] = self.cor_menu
                self.btn_playlist['bg'] = self.cor_menu
                #----------------------------------------------------
                self.btn_fechar['activebackground'] = self.cor_menu
                self.btn_minimizar['activebackground'] = self.cor_menu
                self.icone_da_app_['activebackground'] = self.cor_menu
                self.titulo_da_app['activebackground'] = self.cor_menu
                self.btn_anterior['activebackground'] = self.cor_menu
                self.btn_repetir['activebackground'] = self.cor_menu
                self.btn_proximo['activebackground'] = self.cor_menu
                self.btn_sobre['activebackground'] = self.cor_menu
                self.btn_tocar['activebackground'] = self.cor_menu
                self.btn_volume['activebackground'] = self.cor_menu
                self.btn_volume_bar['activebackground'] = self.cor_menu
                self.btn_parar['activebackground'] = self.cor_menu
                self.btn_abrir['activebackground'] = self.cor_menu
                self.btn_ajuda['activebackground'] = self.cor_menu
                self.btn_sair['activebackground'] = self.cor_menu
                self.btn_playlist['activebackground'] = self.cor_menu
                #-----------------------------------------------------
                self.label_placar['bg'] = self.cor_menu
                self.Label_Capa['bg'] = self.cor_menu
                self.label_tempo['bg'] = self.cor_menu
                self.style.configure(
                    'TScale',
                    background=self.cor_menu,
                )
                #-----------------------------------------------------
            elif self.index == 3:
                self.COR = self.cor_violeta
                #---------------------------------------------------
                self.raiz.config(bg=self.cor_violeta)
                self.janela.config(bg=self.cor_violeta,
                highlightbackground=self.cor_violeta)
                self.barra_de_titulo.config(bg=self.cor_violeta)
                self.barra_de_titulo.config(bg=self.cor_violeta)
                self.barra_de_titulo.config(bg=self.cor_violeta)
                self.barra_de_titulo.config(bg=self.cor_violeta)
                self.barra_do_software_B['bg'] = self.cor_violeta
                self.barra_do_software_L['bg'] = self.cor_violeta
                self.barra_do_software_R['bg'] = self.cor_violeta
                self.Label_Faixa_atual['bg'] = self.cor_violeta
                self.Faixa_atual['bg'] = self.cor_violeta
                self.btn_fechar['bg'] = self.cor_violeta
                self.btn_minimizar['bg'] = self.cor_violeta
                self.icone_da_app_['bg'] = self.cor_violeta
                self.titulo_da_app['bg'] = self.cor_violeta
                self.label_estado['bg'] = self.cor_violeta
                self.label_volume['bg'] = self.cor_violeta
                self.btn_anterior['bg'] = self.cor_violeta
                self.btn_repetir['bg'] = self.cor_violeta
                self.btn_proximo['bg'] = self.cor_violeta
                self.btn_volume_bar['bg'] = self.cor_violeta
                self.btn_volume['bg'] = self.cor_violeta
                self.btn_sobre['bg'] = self.cor_violeta
                self.btn_tocar['bg'] = self.cor_violeta
                self.btn_parar['bg'] = self.cor_violeta
                self.btn_abrir['bg'] = self.cor_violeta
                self.btn_ajuda['bg'] = self.cor_violeta
                self.btn_sair['bg'] = self.cor_violeta
                self.btn_playlist['bg'] = self.cor_violeta
                #----------------------------------------------------
                self.btn_fechar['activebackground'] = self.cor_violeta
                self.btn_minimizar['activebackground'] = self.cor_violeta
                self.icone_da_app_['activebackground'] = self.cor_violeta
                self.titulo_da_app['activebackground'] = self.cor_violeta
                self.btn_anterior['activebackground'] = self.cor_violeta
                self.btn_repetir['activebackground'] = self.cor_violeta
                self.btn_proximo['activebackground'] = self.cor_violeta
                self.btn_sobre['activebackground'] = self.cor_violeta
                self.btn_tocar['activebackground'] = self.cor_violeta
                self.btn_volume['activebackground'] = self.cor_violeta
                self.btn_volume_bar['activebackground'] = self.cor_violeta
                self.btn_parar['activebackground'] = self.cor_violeta
                self.btn_abrir['activebackground'] = self.cor_violeta
                self.btn_ajuda['activebackground'] = self.cor_violeta
                self.btn_sair['activebackground'] = self.cor_violeta
                self.btn_playlist['activebackground'] = self.cor_violeta
                #-----------------------------------------------------
                self.label_placar['bg'] = self.cor_violeta
                self.Label_Capa['bg'] = self.cor_violeta
                self.label_tempo['bg'] = self.cor_violeta
                self.style.configure(
                    'TScale',
                    background=self.cor_violeta,
                )
                #-----------------------------------------------------
            elif self.index == 1:
                self.COR = self.cor_padrao
                #---------------------------------------------------
                self.raiz.config(bg=self.cor_padrao)
                self.janela.config(bg=self.cor_padrao,
                highlightbackground=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_do_software_B['bg'] = self.cor_padrao
                self.barra_do_software_L['bg'] = self.cor_padrao
                self.barra_do_software_R['bg'] = self.cor_padrao
                self.Label_Faixa_atual['bg'] = self.cor_padrao
                self.Faixa_atual['bg'] = self.cor_padrao
                self.btn_fechar['bg'] = self.cor_padrao
                self.btn_minimizar['bg'] = self.cor_padrao
                self.icone_da_app_['bg'] = self.cor_padrao
                self.titulo_da_app['bg'] = self.cor_padrao
                self.label_estado['bg'] = self.cor_padrao
                self.label_volume['bg'] = self.cor_padrao
                self.btn_anterior['bg'] = self.cor_padrao
                self.btn_repetir['bg'] = self.cor_padrao
                self.btn_proximo['bg'] = self.cor_padrao
                self.btn_volume_bar['bg'] = self.cor_padrao
                self.btn_volume['bg'] = self.cor_padrao
                self.btn_sobre['bg'] = self.cor_padrao
                self.btn_tocar['bg'] = self.cor_padrao
                self.btn_parar['bg'] = self.cor_padrao
                self.btn_abrir['bg'] = self.cor_padrao
                self.btn_ajuda['bg'] = self.cor_padrao
                self.btn_sair['bg'] = self.cor_padrao
                self.btn_playlist['bg'] = self.cor_padrao
                #----------------------------------------------------
                self.btn_fechar['activebackground'] = self.cor_padrao
                self.btn_minimizar['activebackground'] = self.cor_padrao
                self.icone_da_app_['activebackground'] = self.cor_padrao
                self.titulo_da_app['activebackground'] = self.cor_padrao
                self.btn_anterior['activebackground'] = self.cor_padrao
                self.btn_repetir['activebackground'] = self.cor_padrao
                self.btn_proximo['activebackground'] = self.cor_padrao
                self.btn_sobre['activebackground'] = self.cor_padrao
                self.btn_tocar['activebackground'] = self.cor_padrao
                self.btn_volume['activebackground'] = self.cor_padrao
                self.btn_volume_bar['activebackground'] = self.cor_padrao
                self.btn_parar['activebackground'] = self.cor_padrao
                self.btn_abrir['activebackground'] = self.cor_padrao
                self.btn_ajuda['activebackground'] = self.cor_padrao
                self.btn_sair['activebackground'] = self.cor_padrao
                self.btn_playlist['activebackground'] = self.cor_padrao
                #-----------------------------------------------------
                self.label_placar['bg'] = self.cor_padrao
                self.Label_Capa['bg'] = self.cor_padrao
                self.label_tempo['bg'] = self.cor_padrao
                self.style.configure(
                    'TScale',
                    background=self.cor_padrao,
                )
                #-----------------------------------------------------
            elif self.index == 2:
                self.COR = self.cor_aqua
                #---------------------------------------------------
                self.raiz.config(bg=self.cor_aqua)
                self.janela.config(bg=self.cor_aqua,
                highlightbackground=self.cor_aqua)
                self.barra_de_titulo.config(bg=self.cor_aqua)
                self.barra_de_titulo.config(bg=self.cor_aqua)
                self.barra_de_titulo.config(bg=self.cor_aqua)
                self.barra_de_titulo.config(bg=self.cor_aqua)
                self.barra_do_software_B['bg'] = self.cor_aqua
                self.barra_do_software_L['bg'] = self.cor_aqua
                self.barra_do_software_R['bg'] = self.cor_aqua
                self.barra_do_software_B['bg'] = self.cor_aqua
                self.barra_do_software_L['bg'] = self.cor_aqua
                self.barra_do_software_R['bg'] = self.cor_aqua
                self.Label_Faixa_atual['bg'] = self.cor_aqua
                self.Faixa_atual['bg'] = self.cor_aqua
                self.btn_fechar['bg'] = self.cor_aqua
                self.btn_minimizar['bg'] = self.cor_aqua
                self.icone_da_app_['bg'] = self.cor_aqua
                self.titulo_da_app['bg'] = self.cor_aqua
                self.label_estado['bg'] = self.cor_aqua
                self.label_volume['bg'] = self.cor_aqua
                self.btn_anterior['bg'] = self.cor_aqua
                self.btn_repetir['bg'] = self.cor_aqua
                self.btn_proximo['bg'] = self.cor_aqua
                self.btn_volume_bar['bg'] = self.cor_aqua
                self.btn_volume['bg'] = self.cor_aqua
                self.btn_sobre['bg'] = self.cor_aqua
                self.btn_tocar['bg'] = self.cor_aqua
                self.btn_parar['bg'] = self.cor_aqua
                self.btn_abrir['bg'] = self.cor_aqua
                self.btn_ajuda['bg'] = self.cor_aqua
                self.btn_sair['bg'] = self.cor_aqua
                self.btn_playlist['bg'] = self.cor_aqua
                #----------------------------------------------------
                self.btn_fechar['activebackground'] = self.cor_aqua
                self.btn_minimizar['activebackground'] = self.cor_aqua
                self.icone_da_app_['activebackground'] = self.cor_aqua
                self.titulo_da_app['activebackground'] = self.cor_aqua
                self.btn_anterior['activebackground'] = self.cor_aqua
                self.btn_repetir['activebackground'] = self.cor_aqua
                self.btn_proximo['activebackground'] = self.cor_aqua
                self.btn_sobre['activebackground'] = self.cor_aqua
                self.btn_tocar['activebackground'] = self.cor_aqua
                self.btn_volume['activebackground'] = self.cor_aqua
                self.btn_volume_bar['activebackground'] = self.cor_aqua
                self.btn_parar['activebackground'] = self.cor_aqua
                self.btn_abrir['activebackground'] = self.cor_aqua
                self.btn_ajuda['activebackground'] = self.cor_aqua
                self.btn_sair['activebackground'] = self.cor_aqua
                self.btn_playlist['activebackground'] = self.cor_aqua
                #-----------------------------------------------------
                self.label_placar['bg'] = self.cor_aqua
                self.Label_Capa['bg'] = self.cor_aqua
                self.label_tempo['bg'] = self.cor_aqua
                self.style.configure(
                    'TScale',
                    background=self.cor_aqua,
                )
                #-----------------------------------------------------
            else:
                self.COR = self.cor_padrao
                #---------------------------------------------------
                self.raiz.config(bg=self.cor_padrao)
                self.janela.config(bg=self.cor_padrao,
                highlightbackground=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_de_titulo.config(bg=self.cor_padrao)
                self.barra_do_software_B['bg'] = self.cor_padrao
                self.barra_do_software_L['bg'] = self.cor_padrao
                self.barra_do_software_R['bg'] = self.cor_padrao
                self.Label_Faixa_atual['bg'] = self.cor_padrao
                self.Faixa_atual['bg'] = self.cor_padrao
                self.btn_fechar['bg'] = self.cor_padrao
                self.btn_minimizar['bg'] = self.cor_padrao
                self.icone_da_app_['bg'] = self.cor_padrao
                self.titulo_da_app['bg'] = self.cor_padrao
                self.label_estado['bg'] = self.cor_padrao
                self.label_volume['bg'] = self.cor_padrao
                self.btn_anterior['bg'] = self.cor_padrao
                self.btn_repetir['bg'] = self.cor_padrao
                self.btn_proximo['bg'] = self.cor_padrao
                self.btn_volume_bar['bg'] = self.cor_padrao
                self.btn_volume['bg'] = self.cor_padrao
                self.btn_sobre['bg'] = self.cor_padrao
                self.btn_tocar['bg'] = self.cor_padrao
                self.btn_parar['bg'] = self.cor_padrao
                self.btn_abrir['bg'] = self.cor_padrao
                self.btn_ajuda['bg'] = self.cor_padrao
                self.btn_sair['bg'] = self.cor_padrao
                self.btn_playlist['bg'] = self.cor_padrao
                #----------------------------------------------------
                self.btn_fechar['activebackground'] = self.cor_padrao
                self.btn_minimizar['activebackground'] = self.cor_padrao
                self.icone_da_app_['activebackground'] = self.cor_padrao
                self.titulo_da_app['activebackground'] = self.cor_padrao
                self.btn_anterior['activebackground'] = self.cor_padrao
                self.btn_repetir['activebackground'] = self.cor_padrao
                self.btn_proximo['activebackground'] = self.cor_padrao
                self.btn_sobre['activebackground'] = self.cor_padrao
                self.btn_tocar['activebackground'] = self.cor_padrao
                self.btn_volume['activebackground'] = self.cor_padrao
                self.btn_volume_bar['activebackground'] = self.cor_padrao
                self.btn_parar['activebackground'] = self.cor_padrao
                self.btn_abrir['activebackground'] = self.cor_padrao
                self.btn_ajuda['activebackground'] = self.cor_padrao
                self.btn_sair['activebackground'] = self.cor_padrao
                #-----------------------------------------------------
                self.label_placar['bg'] = self.cor_padrao
                self.Label_Capa['bg'] = self.cor_padrao
                self.label_tempo['bg'] = self.cor_padrao
                self.style.configure(
                    'TScale',
                    background=self.cor_padrao,
                )
                #-----------------------------------------------------
            self.json.ChangeCurrentColor(self.COR)
            self.json.ChangeCurrentIcone(self.index)
        else:
            pass
        self.Label_Capa.after(10000,self.Evento_Troca_De_Capa)

    def Evento_Repetir(self):
        if self.REPEAT == 0:
            self.btn_repetir['image'] = self.icone_repetir2
            self.REPEAT = 1
        elif self.REPEAT == 1:
            self.btn_repetir['image'] = self.icone_repetir3
            self.REPEAT = 2
        else:
            self.btn_repetir['image'] = self.icone_repetir
            self.REPEAT = 0

    def Evento_Exit(self):
        try:
            self.json.ChangeCurrentColor(self.cor_padrao)
            self.json.ChangeCurrentIcone(0)
            self.json.SetWindow('re',self.REPEAT)
            self.json.SetWindow('vol',int(self.slider_do_volume['value']))
            self.json.SetWindow('la',False)
            self.json.SetWindow('li',False)
            self.json.SetWindow('pl',False)
        except: pass
        self.raiz.destroy()

    def Evento_Templates(self , type : str):
        if type == 'abrir':
            if not self.json.Window('la'):
                LabelAbrir(self.janela,self.COR)
        elif type == 'playlist':
            if not self.json.Window('pl'):
                PlayListApp(self.img_icone_app,self.img_fechar,self.img_minimizar)
        else:
            if not self.json.Window('li'):
                LabelInfo(self.janela)

    def Evento_Limpar_Cache(self):
        self.json.AdicionarLista([])
        self.recentes_diretorios.set([])
        self.caixa_de_lista.configure(
            listvariable=self.recentes_diretorios
        )




MainApplication()