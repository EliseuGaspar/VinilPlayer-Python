from tkinter import Button, Frame, Label, EW
from PyPlayer import PlayerMixer as p

from src.Json_Gerency import GerenciadorJson


class LabelInfo():
    def __init__(self, root):
        self.json =  GerenciadorJson()
        self.tags = p.tags()
        self.COR = self.json.CurrentColor()
        self.File = p.current_file()

        self.body = Frame(root,bg=self.COR,highlightbackground="#f9f9f9",border=0.5,
        highlightcolor='#f9f9f9',highlightthickness=1)
        self.btn_closed = Button(self.body,bg=self.COR,font='Calibri 9',
        justify='left',text='✖\t\t\t\t',fg='#f9f9f9',activebackground=self.COR,
        activeforeground='#f9f9f9',border=0,command=self.Closed,cursor='hand2')
        self.label_artist = Label(self.body,bg=self.COR,fg='#f9f9f9',
        font='Calibri 9',text=f'Artista: \n{self.tags.artist()}')
        self.label_title = Label(self.body,bg=self.COR,fg='#f9f9f9',
        font='Calibri 9',text=f'Titulo: \n{self.tags.title()}')
        self.label_album = Label(self.body,bg=self.COR,fg='#f9f9f9',
        font='Calibri 9',text=f'Album: \n{self.tags.album()}')

        self.body.after(800,self.ChangeColor)
        self.body.place(width=210,height=140,x=335,y=55)
        self.btn_closed.place(rely=0,relheight=0.15,relwidth=1)
        self.label_artist.place(rely=0.15,relheight=0.25,relwidth=1)
        self.label_title.place(rely=0.40,relheight=0.25,relwidth=1)
        self.label_album.place(rely=0.65,relheight=0.25,relwidth=1)
        self.json.SetWindow('li',True)
    
    def ChangeColor(self):
        if self.COR != self.json.CurrentColor():
            self.body['bg'] = self.json.CurrentColor()
            self.btn_closed['bg'] = self.json.CurrentColor()
            self.btn_closed['activebackground'] = self.json.CurrentColor()
            self.label_artist['bg'] = self.json.CurrentColor()
            self.label_title['bg'] = self.json.CurrentColor()
            self.label_album['bg'] = self.json.CurrentColor()
            self.COR = self.json.CurrentColor()
        if self.File != p.current_file():
            self.label_artist['text'] = f"Artista: \n{self.tags.artist()}"
            self.label_title['text'] = f"Titulo: \n{self.tags.title()}"
            self.label_album['text'] = f"Album: \n{self.tags.album()}"
            self.File = p.current_file()
        self.body.after(100,self.ChangeColor)
    
    def Closed(self):
        self.body.place_forget()
        self.json.SetWindow('li',False)