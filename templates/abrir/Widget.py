from tkinter import Label , Button , filedialog , messagebox
from PyPlayer import PlayerMixer as p
from src.Json_Gerency import GerenciadorJson

class LabelAbrir:
    def __init__(self,root,bg_color):
        self.json_ = GerenciadorJson()
        self.COR = self.json_.CurrentColor()
        self.LabelAbrir = Label(
            root,bg=bg_color,border=0.5,highlightbackground="#ffffff",
            highlightthickness=1,highlightcolor="#ffffff")
        self.LabelAbrir_File = Button(
            self.LabelAbrir,bg=bg_color,fg="#ffffff",font='Calibri 9',border=0,
            activebackground=bg_color,activeforeground="#ffffff",text='Arquivo',
            cursor='hand2',command=self.OpenFile
        )
        self.LabelAbrir_Folder = Button(
            self.LabelAbrir,bg=bg_color,fg="#ffffff",font='Calibri 9',border=0,
            activebackground=bg_color,activeforeground="#ffffff",text='Pasta',
            cursor='hand2',command=self.OpenFolder
        )
        self.LabelAbrir_Close = Button(
            self.LabelAbrir,bg=bg_color,fg="#ffffff",font='Calibri 9',border=0,
            activebackground=bg_color,activeforeground="#ffffff",text='Fechar',
            cursor='hand2',command=self.ForgetWidgets
        )

        self.LabelAbrir.after(1000,self.ChangeColor)
        self.LabelAbrir.place(
            rely=0,relx=0.08
        )
        self.LabelAbrir_File.grid(
            row=0,
            column=0
        )
        self.LabelAbrir_Folder.grid(
            row=1,
            column=0
        )
        self.LabelAbrir_Close.grid(
            row=2,
            column=0
        )
        self.json_.SetWindow('la',True)

    def OpenFile(self):
        self.ForgetWidgets()
        dir_file = filedialog.askopenfilename(
            filetypes=[('MP3 Files','.mp3')],
            initialdir=f'{p.getpath()}',
            defaultextension='.mp3',
            title='Pegar Audios'
        )
        if dir_file:
            p.load(file=dir_file)
            p.stop()
            p.play()
    
    def OpenFolder(self):
        self.ForgetWidgets()
        dir_ = filedialog.askdirectory(
            initialdir=f'{p.getpath()}',
            title='Pegar Audios'
        )
        if dir_:
            resultado = p.load(dir=dir_)
            if resultado == False:
                messagebox.showinfo(
                    title='Falha ao pegar arquivos',
                    message='O diretório introduzido não possui nenhum arquivo .mp3'
                )
            else:
                p.stop()
                p.play()
    
    def ForgetWidgets(self):
        self.LabelAbrir.place_forget()
        self.json_.SetWindow('la',False)

    def ChangeColor(self):
        if self.COR != self.json_.CurrentColor():
            self.LabelAbrir['bg'] = self.json_.CurrentColor()
            self.LabelAbrir_Close['bg'] = self.json_.CurrentColor()
            self.LabelAbrir_File['bg'] = self.json_.CurrentColor()
            self.LabelAbrir_Folder['bg'] = self.json_.CurrentColor()
            self.COR = self.json_.CurrentColor()

        self.LabelAbrir.after(100,self.ChangeColor)

