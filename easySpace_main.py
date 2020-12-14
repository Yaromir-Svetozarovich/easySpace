from tkinter import * 




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
        canv.create_oval(600,40,700,140, fill = 'red', outline = 'yellow')
    def Card_Mercury():
        #Рисует карточку-кнопку с инфой по Меркурию 
        canv.create_rectangle(60, 600, 200, 700,
                   fill='grey',
                   outline='orange',
                   width=3,
                   activedash=(5, 4))
        button_merc =Button(root, width = 140, height = 100)
        #Нажатие на кнопку ЛКМ
        button_merc.bind("<Button-1>",  Mercury() )
        button_merc.pack()    
    def Card_Venera():
        canv.create_restangle()
    
        
        
        
  
UI.Card_Mercury()
root.mainloop()
