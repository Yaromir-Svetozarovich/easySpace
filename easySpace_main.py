import tkinter as tk
import math 
from random import randint,choice

#Выход из программы
def window_deleted():
    print ('Окно закрыто')
    root.quit() # явное указание на выход из программы
    
#Подготовка окна
root = tk.Tk()
root.title("easySpace")
root.geometry("1366x768")


root.protocol('WM_DELETE_WINDOW', window_deleted)#Проверка на выход из программы

fr2 =tk.Frame(root, width = 1366, height = 50, bg ='black')# Создание слоя для размещения кнопок
fr2.pack(fill = 'both', expand= 1)

root.resizable(False, False)#Запрет на изменение размера окна

#Интерфейс пользователя

class UI:
    def __init__(self):
        pass
#""" Здесь описаны методы отрисовки планет  """    
    #Необходимо переделать расположение планет и метод задания координат планет, для их перемещения

    def Mercury(event):#Меркурий
        #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Меркурий', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'mercury.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Меркурий — ближайшая к Солнцу планета. Ни воды, ни воздуха на Меркурии нет. \nИз-за того что Меркурий так близок к светилу, дневная температура на этой планете почти +450°С.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 0,39 астр. ед.;\nПериод обращения - 88 дней;\nПериод вращения - 58,6 сут.;\nДиаметр - 4878 км;\nПлотность - 5,5 г/куб.см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')# Хитрость! Блокируем ввод пользователем. Т.о я н@@@@ал систему и вывел сложный текст!
        

    def Venera(event):#Венера
             #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Венера', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'venera.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Венера — планета, которую часто называют утренней или вечерней звездой. \nЭти названия не случайны: Венеру можно увидеть вечером, в лучах заходящего Солнца, или утром, перед самым восходом. \nПоверхность Венеры представляет собой равнину, усыпанную камнями и обломками скал. На Венере нет ни воды, ни жизни.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 0,72 астр. ед.; \nПериод обращения - 224,7 дней; \nПериод вращения - 243 сут.; \nДиаметр - 12100 км; \nПлотность - 5,2 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')

    def Earth(event):#Земля
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Земля', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'earth.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Земля — одна из планет, которые вращаются вокруг Солнца. Она почти в 110 раз меньше этого светила по диаметру. \nПопробуй представить, что Солнце превратилось в дыню. Земля тогда со своими огромными городами, деревнями, горами и морями стала бы размером с маленькую фруктовую косточку.')
        text.insert(5.1,'\nФизические характеристики: \nРасстояние от солнца - 1,00 астр. ед.; \nПериод обращения - 365,24 дней; \nПериод вращения - 24 часа; \nДиаметр - 12742 км; кол-во спутников - 1; \nПлотность - 5,5 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')

    

    def Mars(event):#Марс
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Марс', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'mars.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Марс называют красной планетой из-за ржаво-красного цвета его поверхности. Температура на Марсе очень низкая и в дневное время суток, и в ночное.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 1,52 астр. ед.; \nПериод обращения - 687 дней ; \nПериод вращения - 24,5 часа ; \nДиаметр - 6794 ; \nКол-во спутников - 2 ; \nПлотность - 3,9 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')



    def Yupiter(event):#Юпитер
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Юпитер', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'yupiter.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Юпитер — самая большая планета Солнечной системы. Она больше Земли в 1000 раз. Юпитер находится на огромном расстоянии от Солнца, отчего температура на этом газовом гиганте дошла -140°С.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 5,2 астр. ед.; \nПериод обращения - 11,9 лет; \nПериод вращения - 10 часов; \nДиаметр - 139800 км.; \nКол-во спутников - 16; \nПлотность - 1,3 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')


    def Saturn(event):#Сатурн
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Сатурн', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'saturn.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Сатурн — планета, которая по размерам чуть меньше Юпитера. Внешне Сатурн отличается от остальных планет тем, что окружен множеством светящихся колец. Каждое кольцо Сатурна состоит из еще более тонких колец. Это «украшение» представляет собой миллиарды каменных обломков, покрытых льдом.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца -9, 54; \nПериод обращения - 29,5 лет; \nПериод вращения - 10,2 часов; \nДиаметр - 116000 км; \nКол-во спутников - 30; \nПлотность - 0, 7 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')



    def Uran(event):#Уран
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Уран', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'uran.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Уран удален от Солнца на расстояние в 19 раз большее, чем Земля, поэтому получает очень мало тепла.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 19,19 астр. ед.; \nПериод обращения - 84 года; \nПериод вращения - 10,7 часов; \nДиаметр- 50800 км; \nКол-во спутников - 15; \nПлотность - 1,4 г/куб. см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')



    def Neptun(event):#Нептун
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Нептун', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'neptun.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Нептун по виду и размерам похож на Уран. Он сильно сжат и быстро вращается. Нептун удален от Солнца на 2,8 миллиардов километров.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 30,07 астр. ед.; \nПериод обращения - 164,8 лет; \nПериод вращения - 16 часов; \nДиаметр - 48600 км; \nКол-во спутников -6; \nПлотность - 1,6 г/куб.см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')



    def Pluton(event):
                     #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Плутон', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'pluton.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Плутон – это карликовая планета Солнечной системы, транснептуновый объект (крупнейший в поясе Койпера) и десятое по массе тело, обращающееся вокруг Солнца, после 8 планет (без учета их спутников) и, предположительно, Эриды.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 39,23 астр. ед.;\nПериод обращения - 245 лет;\nПериод вращения - -6,38 сут.;\nДиаметр - 2376 км;\nКол-во спутников -5; \nПлотность - 1,860 г/куб.см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')


    def Sun(event):
        #Подготовка окна с информацией о планете
        info = tk.Toplevel(root, width=800,height = 600, bg ='black')        
        info.title("Info about planet") 
        info.geometry('800x600')
        info.resizable(False,False) #Запрет на изменение размера окна 
       # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = tk.Label(info, bg = 'black',fg = 'white',text = 'Плутон', font = 'Arial 25')#Выводит имя планеты
        image1 = tk.PhotoImage(file = 'pluton.gif')#Задаем картинку для планеты
        Lab_img = tk.Label(info,image =image1,borderwidth =0)
        Lab_img.image_ref = image1
        text = tk.Text(info,bg = 'black',fg = 'white', borderwidth = 0 ,width = 700, height = 300 , font = 'Arial 10', wrap = 'word', state = 'normal')# Задаем текст  с инфой о планете
        text.insert(1.0,'Плутон – это карликовая планета Солнечной системы, транснептуновый объект (крупнейший в поясе Койпера) и десятое по массе тело, обращающееся вокруг Солнца, после 8 планет (без учета их спутников) и, предположительно, Эриды.')
        text.insert(5.1,'\nФизические характеристики:\nРасстояние от солнца - 39,23 астр. ед.;\nПериод обращения - 245 лет;\nПериод вращения - -6,38 сут.;\nДиаметр - 2376 км;\nКол-во спутников -5; \nПлотность - 1,860 г/куб.см.')
        Lab.pack()# Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side = 'bottom')
        text.configure(state = 'disabled')


        

    

#""" Здесь описаны методы отрисовки и логики при нажатии на клавиши  """ 
#
#
#Данный метод вызывает окно, с информацией о планете. На вход нужно подать название планеты, а далее программа выведет рисунок планеты и информацию о ней. 

    
# Далее кнопки можно заменить на планеты, т.е вывод окна с инфой о планете при нажатии на планету
    def Card_Mercury():#Кнопка Меркурия
        button_merc = tk.Button(fr2, width = 2, height = 2, bg ='black', fg = 'white',text = 'Меркурий')
        button_merc.bind("<Button-1>",   UI.Mercury) 
        button_merc.pack(side = 'left',fill = 'x', expand = True)


    def Card_Venera():#Кнопка Венеры
        button_ven = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white',text = 'Венера')
        button_ven.bind("<Button-1>",  UI.Venera )
        button_ven.pack(side = 'left',fill = 'x', expand = True)

    def Card_Eath():#Кнопка Земли
        button_earth = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Земля')
        button_earth.bind("<Button-1>",  UI.Earth )
        button_earth.pack(side = 'left',fill = 'x', expand = True)

    def Card_Mars():#Кнопка Марса
        button_mars = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Марс')
        button_mars.bind("<Button-1>",  UI.Mars )
        button_mars.pack(side = 'left',fill = 'x', expand = True)   

    def Card_Yupiter():#Кнопка Юпитера
        button_yup = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Юпитер')
        button_yup.bind("<Button-1>",  UI.Yupiter )
        button_yup.pack(side = 'left',fill = 'x', expand = True) 

    def Card_Saturn():#Кнопка Юпитера
        button_sat = tk.Button(fr2 , width = 2, height = 2, bg ='black', fg = 'white', text = 'Сатурн')
        button_sat.bind("<Button-1>",  UI.Saturn )
        button_sat.pack(side = 'left',fill = 'x', expand = True)  

    def Card_Uran():#Кнопка Урана
        button_ur = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Уран')
        button_ur.bind("<Button-1>",  UI.Uran )
        button_ur.pack(side = 'left',fill = 'x', expand = True) 

    def Card_Neptun():#Кнопка Нептуна
        button_nep = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Нептун')
        button_nep.bind("<Button-1>", UI.Neptun)
        button_nep.pack(side = 'left',fill = 'x', expand = True) 

    def Card_Pluton():#Кнопка Нептуна
        button_nep = tk.Button(fr2 , width = 2, height = 2, bg ='black',  fg = 'white',text = 'Плутон')
        button_nep.bind("<Button-1>", UI.Pluton)
        button_nep.pack(side = 'left',fill = 'x', expand = True) 



# Здесь будет движение планет        
# Здесь будет вывод текста при нажатии на клавишу (может и не будет, не решил пока)
#Здесь хрень для улучшения графики(может тоже не будет, хз вообще)
       

#Вызов методов 
def Play():
   #UI.Sun() 
    UI.Card_Mercury()
    UI.Card_Venera()
    UI.Card_Eath()
    UI.Card_Mars()
    UI.Card_Yupiter()
    UI.Card_Saturn()
    UI.Card_Uran()
    UI.Card_Neptun()
    UI.Card_Pluton()

#Запуск программы
Play()    
root.mainloop()
