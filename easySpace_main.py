import tkinter as tk
import math 
from random import randint,choice

#Выход из программы
def window_deleted():
    print ('Окно закрыто')
    root.quit() # явное указание на выход из программы
    
#Подготовка окна
root = tk.Tk()
fr = tk.Frame(root, width=1366,height =758)#Создание слоя, на котором будет располагаться canvas
fr.pack(fill = 'both', expand = 1)
root.title("easySpace")
root.geometry("1366x768")
root.protocol('WM_DELETE_WINDOW', window_deleted)#Проверка на выход из программы

canv = tk.Canvas(fr, height = 710,bg='black')#Размещение слоя с графикой
canv.pack(fill = 'both', expand = 1)

fr2 =tk.Frame(root, width = 1366, height = 10, bg ='black')# Создание слоя для размещения кнопок
fr2.pack(fill = 'both', expand= 1)
root.resizable(False, False)#Запрет на изменение размера окна

for i in range(4000) :
    coord_x = randint(0,1366)# Выборка координаты x
    coord_y = randint(0,768)# Выборка координаты y
    r = randint(1,2)# Выборка радиуса звезды
    color = choice(['white','#AFDAFC','#FB607F'])
    canv.create_oval(coord_x-r,coord_y-r, coord_x+r, coord_y+r, fill = color ) #Рисует круг, в случайной позиции
        
#Интерфейс пользователя
class UI():
    def __init__(self):
        self
#""" Здесь описаны методы отрисовки планет  """    
    #Необходимо переделать расположение планет и метод задания координат планет, для их перемещения
    """
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
    """

#""" Здесь описаны методы отрисовки и логики при нажатии на клавиши  """ 
#
#
#Данный метод вызывает окно, с информацией о планете. На вход нужно подать название планеты, а далее программа выведет рисунок планеты и информацию о ней. 

    def NewWindow(event):
        #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height =600, bg ='black')
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
        #info.overrideredirect(True) Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Планета', font = 'Arial 25')

        Lab.pack(side = 'top')


       


# Далее кнопки можно заменить на планеты, т.е вывод окна с инфой о планете при нажатии на планету
    def Card_Mercury():#Кнопка Меркурия
        button_merc = tk.Button(fr2, width = 2, height = 2, bg ='black', fg = 'white',text = 'Меркурий')
        button_merc.bind("<Button-1>",   UI.NewWindow) 
        button_merc.pack(side = 'left',fill = 'x', expand = True)


    def Card_Venera():#Кнопка Венеры
        button_ven = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white',text = 'Венера')
        i = 2
        button_ven.bind("<Button-1>",  UI.NewWindow )
        button_ven.pack(side = 'left',fill = 'x', expand = True)

    def Card_Eath():#Кнопка Земли
        button_earth = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Земля')
        button_earth.bind("<Button-1>",  UI.NewWindow )
        button_earth.pack(side = 'left',fill = 'x', expand = True)

    def Card_Mars():#Кнопка Марса
        button_mars = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Марс')
        button_mars.bind("<Button-1>",  UI.NewWindow )
        button_mars.pack(side = 'left',fill = 'x', expand = True)   

    def Card_Yupiter():#Кнопка Юпитера
        button_yup = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Юпитер')
        button_yup.bind("<Button-1>",  UI.NewWindow )
        button_yup.pack(side = 'left',fill = 'x', expand = True) 

    def Card_Saturn():#Кнопка Юпитера
        button_sat = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Сатурн')
        button_sat.bind("<Button-1>",  UI.NewWindow )
        button_sat.pack(side = 'left',fill = 'x', expand = True)  

    def Card_Uran():#Кнопка Урана
        button_ur = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Уран')
        button_ur.bind("<Button-1>",  UI.NewWindow )
        button_ur.pack(side = 'left',fill = 'x', expand = True) 

    def Card_Neptun():#Кнопка Нептуна
        button_nep = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Нептун')
        button_nep.bind("<Button-1>", UI.NewWindow)
        button_nep.pack(side = 'left',fill = 'x', expand = True) 




# Здесь будет движение планет        
# Здесь будет вывод текста при нажатии на клавишу (может и не будет, не решил пока)
#Здесь хрень для улучшения графики(может тоже не будет, хз вообще)
       

#Вызов методов 
def Play():
   # UI.Sun() 
    UI.Card_Mercury()
    UI.Card_Venera()
    UI.Card_Eath()
    UI.Card_Mars()
    UI.Card_Yupiter()
    UI.Card_Saturn()
    UI.Card_Uran()
    UI.Card_Neptun()

#Запуск программы
Play()    
root.mainloop()
