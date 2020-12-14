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
        canv.create_oval(600,100,700,200, fill = 'red', outline = 'yellow')
    def Card_Mercury():
        #Рисует карточку-кнопку с инфой по Меркурию 
        button_merc =Button(root, width = 20, height = 10, bg ='grey',text = 'Меркурий')
        #Нажатие на кнопку ЛКМ
        button_merc.bind("<Button-1>",  UI.Mercury )
        button_merc.pack()    
    def Card_Venera():
        canv.create_restangle()
    
        
        
        
  
UI.Card_Mercury()
root.mainloop()
