from tkinter import * 
import math 
from random import randint,choice

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
    #Необходимо переделать расположение планет и метод задания координат планет, для их перемещения

    def SKY():# Генератор звездного неба
        for i in range(2000) :
            coord_x = randint(0,1366)# Выборка координаты x
            coord_y = randint(0,768)# Выборка координаты y
            r = randint(1,3)# Выборка радиуса звезды
            color = choice(['white','#AFDAFC','#FB607F'])
            canv.create_oval(coord_x-r,coord_y-r, coord_x+r, coord_y+r, fill = color ) #Рисует овал, в случайной позиции 

    def Sun():#Солнце
        canv.create_oval(583,200,783,400, fill = 'orange', outline = 'red' )

    def Mercury(event):#Меркурий
        canv.create_oval(1000,400,1020,420, fill = 'red', outline = 'yellow')

    def Venera(event):#Венера
        canv.create_oval(1040,420,1080, 460, fill = 'orange', outline = 'yellow')

    def Earth(event):#Земля
        canv.create_oval(1050,430,1090,470, fill = 'blue', outline = 'green')

    def Mars(event):#Марс
        canv.create_oval(1050,430,1090,470, fill = 'red', outline = 'red')

    def Yupiter(event):#Юпитер
        canv.create_oval(10,100,30,120, fill = 'red', outline = 'white')
        canv.create_oval(11,101,16,106, fill = 'grey', outline = 'red')

    def Saturn(event):#Сатурн
        canv.create_oval(100,100,200,200,  fill = '#F0D698', outline = 'grey')

    def Uran(event):#Уран
        canv.create_oval(100,100,200,200,  fill = '#87CEEB', outline = 'blue')

    def Neptun(event):#Нептун
        canv.create_oval(400,100,500,200,  fill = '#4169E1', outline = 'grey')
    

#""" Здесь описаны методы отрисовки и логики при нажатии на клавиши  """        
    def Card_Mercury():#Кнопка Меркурия
        #Рисует карточку-кнопку с инфой по Меркурию 
        button_merc =Button(root, width = 10, height = 2, bg ='grey',text = 'Меркурий')
        #Нажатие на кнопку ЛКМ
        button_merc.bind("<Button-1>",  UI.Mercury )
        button_merc.pack(side = 'left',fill = 'both', expand = True)    
    def Card_Venera():#Кнопка Венеры
        button_ven = Button(root , width = 10, height = 2, bg ='grey', text = 'Венера')
        button_ven.bind("<Button-1>", UI.Venera )
        button_ven.pack(side = 'left',fill = 'both', expand = True)
    def Card_Eath():#Кнопка Земли
        button_earth = Button(root , width = 10, height = 2, bg ='grey', text = 'Земля')
        button_earth.bind("<Button-1>", UI.Earth )
        button_earth.pack(side = 'left',fill = 'both', expand = True)
    def Card_Mars():#Кнопка Марса
        button_mars = Button(root , width = 10, height = 2, bg ='grey', text = 'Марс')
        button_mars.bind("<Button-1>", UI.Mars )
        button_mars.pack(side = 'left',fill = 'both', expand = True)   
    def Card_Yupiter():#Кнопка Юпитера
        button_yup = Button(root , width = 10, height = 2, bg ='grey', text = 'Юпитер')
        button_yup.bind("<Button-1>", UI.Yupiter )
        button_yup.pack(side = 'left',fill = 'both', expand = True)  
    def Card_Saturn():#Кнопка Юпитера
        button_sat = Button(root , width = 10, height = 2, bg ='grey', text = 'Сатурн')
        button_sat.bind("<Button-1>", UI.Saturn )
        button_sat.pack(side = 'left',fill = 'both', expand = True)     
    def Card_Uran():#Кнопка Урана
        button_ur = Button(root , width = 10, height = 2, bg ='grey', text = 'Уран')
        button_ur.bind("<Button-1>", UI.Uran )
        button_ur.pack(side = 'left',fill = 'both', expand = True) 
    def Card_Neptun():#Кнопка Нептуна
        button_nep = Button(root , width = 10, height = 2, bg ='grey', text = 'Нептун')
        button_nep.bind("<Button-1>", UI.Neptun )
        button_nep.pack(side = 'left',fill = 'both', expand = True) 



# Здесь будет движение планет        
# Здесь будет вывод текста при нажатии на клавишу (модет и не будет, не решил пока)
#Здесь хрень для улучшения графики(может тоже не будет, хз вообще)
       
#Вызов методов 

UI.SKY() 
UI.Sun() 
UI.Card_Mercury()
UI.Card_Venera()
UI.Card_Eath()
UI.Card_Mars()
UI.Card_Yupiter()
UI.Card_Saturn()
UI.Card_Uran()
UI.Card_Neptun()
root.mainloop()
