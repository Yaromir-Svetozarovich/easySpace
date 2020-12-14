from tkinter import * 
import math



root = Tk()
fr = Frame(root)
root.title("easySpace")
root.geometry("1366x768")
canv = Canvas(root,  bg='black')
canv.pack(fill = BOTH, expand = 1)

class UI():
    def __init__(self):
        self
    def Mercury(event):
        #Рисует овал(Меркурий)
        canv.create_oval(600,100,620,120, fill = 'red', outline = 'yellow')
    def Venera(event):
        canv.create_oval(640,120,680, 160, fill = 'orange', outline = 'yellow')
    def Card_Mercury():
        #Рисует карточку-кнопку с инфой по Меркурию 
        button_merc =Button(root, width = 10, height = 5, bg ='grey',text = 'Меркурий')
        #Нажатие на кнопку ЛКМ
        button_merc.bind("<Button-1>",  UI.Mercury )
        button_merc.pack(side = 'left')    
    def Card_Venera():
        button_ven = Button(root , width = 10, height = 5, bg ='grey', text = 'Венера')
        button_ven.bind("<Button-1>", UI.Venera )
        button_ven.pack(side = 'left')
    
        
        
        
  
UI.Card_Mercury()
UI.Card_Venera()
root.mainloop()
