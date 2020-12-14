from tkinter import * 
import math


#Подготовка окна
root = Tk()
fr = Frame(root)
root.title("easySpace")
root.geometry("1366x768")
canv = Canvas(root,  bg='black')
canv.pack(fill = BOTH, expand = 1)

#Интерфейс пользователя
class UI():
    def __init__(self):
        self
#""" Здесь описаны методы отрисовки планет  """    
    
    def Mercury(event):#Меркурий
        canv.create_oval(1000,400,1020,420, fill = 'red', outline = 'yellow')
    def Venera(event):#Венера
        canv.create_oval(1040,420,1080, 460, fill = 'orange', outline = 'yellow')
    def Earth(event):#Земля
        canv.create_oval(1050,430,1090,470, fill = 'blue', outline = 'green')
    def Mars(event):#Марс
        canv.create_oval(1050,430,1090,470, fill = 'red', outline = 'red')
    def Yupiter(event):#Юпитер
        canv.create_oval(1080,500,1090,470, fill = 'red', outline = 'white')
        canv.create_oval(1040,420,1080,460, fill = 'grey', outline = 'red')
    def Saturn(event):#Сатурн
        canv.create_oval(1050,430,1090,470, fill = 'red', outline = 'red')
    
#""" Здесь описаны методы отрисовки и логики при нажатии на клавиши  """        
    def Card_Mercury():#Кнопка Меркурия
        #Рисует карточку-кнопку с инфой по Меркурию 
        button_merc =Button(root, width = 10, height = 5, bg ='grey',text = 'Меркурий')
        #Нажатие на кнопку ЛКМ
        button_merc.bind("<Button-1>",  UI.Mercury )
        button_merc.pack(side = 'left')    
    def Card_Venera():#Кнопка Венеры
        button_ven = Button(root , width = 10, height = 5, bg ='grey', text = 'Венера')
        button_ven.bind("<Button-1>", UI.Venera )
        button_ven.pack(side = 'left')
    def Card_Eath():#Кнопка Земли
        button_earth = Button(root , width = 10, height = 5, bg ='grey', text = 'Земля')
        button_earth.bind("<Button-1>", UI.Earth )
        button_earth.pack(side = 'left')
        
        
# Здесь будет движение планет        
# Здесь будет вывод текста при нажатии на клавишу (модет и не будет, не решил пока)
#Здесь хрень для улучшения графики(может тоже не будет, хз вообще)
       
#Вызов методов   
UI.Card_Mercury()
UI.Card_Venera()
UI.Card_Eath()
root.mainloop()
