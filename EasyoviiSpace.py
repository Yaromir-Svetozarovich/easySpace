from tkinter import *
import math
from random import randint, choice, random


# Выход из программы
def window_deleted():
    print('Окно закрыто')
    root.quit()  # явное указание на выход из программы


delay_mercury = 10
delay_venus = 80
delay_earth = 100
delay_mars = 120
delay_jupiter = 160
delay_saturn = 180
delay_uranium = 220
delay_neptune = 260
delay_pluto = 1000
CIRCULAR_PATH_INCR = 0.5

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

root = Tk()
root.title("easySpace")
root.geometry("1270x720")

root.protocol('WM_DELETE_WINDOW', window_deleted)  # Проверка на выход из программы

root.resizable(False, False)  # Запрет на изменение размера окна

canvas = Canvas(root, width=1270, height=720, bg='black')
canvas.pack(fill=BOTH, expand=1)


# Интерфейс пользователя
class UI:
    def __init__(self):
        pass

    def Mercury(event):  # Меркурий
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Меркурий', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='mercury.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0, 'Меркурий — ближайшая к Солнцу планета. Ни воды, ни воздуха на Меркурии нет.'
                    '\nИз-за того что Меркурий так близок к светилу, дневная температура на этой планете почти +450°С.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 0,39 астр. ед.;\nПериод обращения - 88 дней;'
                    '\nПериод вращения - 58,6 сут.;\nДиаметр - 4878 км;\nПлотность - 5,5 г/куб.см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')  # Хитрость! Блокируем ввод пользователем

    def Venera(event):  # Венера
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Венера', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='venera.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0, 'Венера — планета, которую часто называют утренней или вечерней звездой.'
                    '\nЭти названия не случайны: Венеру можно увидеть вечером,'
                    'в лучах заходящего Солнца, или утром, перед самым восходом.'
                    '\nПоверхность Венеры представляет собой равнину, усыпанную камнями и обломками скал.'
                    'На Венере нет ни воды, ни жизни.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 0,72 астр. ед.;'
                    '\nПериод обращения - 224,7 дней; \nПериод вращения - 243 сут.; \nДиаметр - 12100 км;'
                    '\nПлотность - 5,2 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Earth(event):  # Земля
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Земля', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='earth.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Земля — одна из планет, которые вращаются вокруг Солнца.'
                    'Она почти в 110 раз меньше этого светила по диаметру.'
                    '\nПопробуй представить, что Солнце превратилось в дыню. Земля тогда со своими огромными городами,'
                    'деревнями, горами и морями стала бы размером с маленькую фруктовую косточку.')
        text.insert(5.1,
                    '\nФизические характеристики: \nРасстояние от солнца - 1,00 астр. ед.;'
                    '\nПериод обращения - 365,24 дней; \nПериод вращения - 24 часа;'
                    '\nДиаметр - 12742 км; кол-во спутников - 1; \nПлотность - 5,5 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Mars(event):  # Марс
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Марс', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='mars.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Марс называют красной планетой из-за ржаво-красного цвета его поверхности.'
                    'Температура на Марсе очень низкая и в дневное время суток, и в ночное.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 1,52 астр. ед.; \nПериод обращения - 687 дней ;'
                    '\nПериод вращения - 24,5 часа ; \nДиаметр - 6794 ; \nКол-во спутников - 2 ;'
                    '\nПлотность - 3,9 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Yupiter(event):  # Юпитер
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать, но хрень
        Lab = Label(info, bg='black', fg='white', text='Юпитер', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='yupiter.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Юпитер — самая большая планета Солнечной системы. Она больше Земли в 1000 раз.'
                    'Юпитер находится на огромном расстоянии от Солнца,'
                    'отчего температура на этом газовом гиганте дошла -140°С.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 5,2 астр. ед.; \nПериод обращения - 11,9 лет;'
                    '\nПериод вращения - 10 часов; \nДиаметр - 139800 км.; \nКол-во спутников - 16;'
                    '\nПлотность - 1,3 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Saturn(event):  # Сатурн
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Сатурн', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='saturn.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Сатурн — планета, которая по размерам чуть меньше Юпитера. '
                    'нешне Сатурн отличается от остальных планет тем, что окружен множеством светящихся колец.'
                    'Каждое кольцо Сатурна состоит из еще более тонких колец.'
                    'Это «украшение» представляет собой миллиарды каменных обломков, покрытых льдом.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца -9, 54; \nПериод обращения - 29,5 лет;'
                    '\nПериод вращения - 10,2 часов; \nДиаметр - 116000 км; \nКол-во спутников - 30;'
                    '\nПлотность - 0, 7 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Uran(event):  # Уран
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Уран', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='uran.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Уран удален от Солнца на расстояние в 19 раз большее, чем Земля, поэтому получает очень мало тепла.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 19,19 астр. ед.; \nПериод обращения - 84 года;'
                    '\nПериод вращения - 10,7 часов; \nДиаметр- 50800 км; \nКол-во спутников - 15;'
                    '\nПлотность - 1,4 г/куб. см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Neptun(event):  # Нептун
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Нептун', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='neptun.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Нептун по виду и размерам похож на Уран. Он сильно сжат и быстро вращается.'
                    'Нептун удален от Солнца на 2,8 миллиардов километров.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 30,07 астр. ед.; \nПериод обращения - 164,8 лет;'
                    '\nПериод вращения - 16 часов; \nДиаметр - 48600 км; \nКол-во спутников -6;'
                    '\nПлотность - 1,6 г/куб.см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Pluton(event):
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Плутон', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='pluton.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 10', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Плутон – это карликовая планета Солнечной системы,'
                    'транснептуновый объект (крупнейший в поясе Койпера) и десятое по массе тело,'
                    'обращающееся вокруг Солнца, после 8 планет (без учета их спутников) и, предположительно, Эриды.')
        text.insert(5.1,
                    '\nФизические характеристики:\nРасстояние от солнца - 39,23 астр. ед.;\nПериод обращения - 245 лет;'
                    '\nПериод вращения - -6,38 сут.;\nДиаметр - 2376 км;\nКол-во спутников -5;'
                    '\nПлотность - 1,860 г/куб.см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')

    def Sun(event):
        # Подготовка окна с информацией о планете
        info = Toplevel(root, width=800, height=600, bg='black')
        info.title("Info about planet")
        info.geometry('800x600')
        info.resizable(False, False)  # Запрет на изменение размера окна
        info.grab_set()
        # info.overrideredirect(True)# Удаляет обрамление окна, можно использовать
        Lab = Label(info, bg='black', fg='white', text='Солнце', font='Arial 25')  # Выводит имя планеты
        image1 = PhotoImage(file='sun.gif')  # Задаем картинку для планеты
        Lab_img = Label(info, image=image1, borderwidth=0)
        Lab_img.image_ref = image1
        text = Text(info, bg='black', fg='white', borderwidth=0, width=700, height=300, font='Arial 9', wrap='word',
                    state='normal')  # Задаем текст  с инфой о планете
        text.insert(1.0,
                    'Со́лнце — одна из звёзд нашей Галактики (Млечный Путь) и единственная звезда Солнечной системы. \nВокруг Солнца обращаются другие объекты этой системы: планеты и их спутники, карликовые планеты и их спутники, астероиды, метеороиды, кометы и космическая пыль.\nПо спектральной классификации Солнце относится к типу G2V (жёлтый карлик) ')
        text.insert(5.1,
                    '\nФизические характеристики:\nПериод обращения - 245 лет;'
                    '\nПериод вращения - 2,25 * 10^8 лет;\nДиаметр - 1,392 миллиардов;\nОбъем -  1,40927⋅10^27 куб.метр '
                    '\nПлотность - 1,860 г/куб.см.')
        Lab.pack()  # Пакуйте его, ребята!
        Lab_img.pack()
        text.pack(side='bottom')
        text.configure(state='disabled')


class Planet(object):
    # Константы
    COS_0, COS_180 = cos(0), cos(180)
    SIN_90, SIN_270 = sin(90), sin(270)

    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius

    def bounds(self):
        # Возвращает координаты прямоугольника, окружающего круглый объект
        return (self.x + self.radius*self.COS_0,   self.y + self.radius*self.SIN_270,
                self.x + self.radius*self.COS_180, self.y + self.radius*self.SIN_90)


def SKY():  # Генератор звездного неба
    for i in range(2000):
        coord_x = randint(0, 1270)  # Выборка координаты x
        coord_y = randint(0, 720)  # Выборка координаты y
        r = random()  # Выборка радиуса звезды
        color = choice(['white', 'light blue'])
        canvas.create_oval(coord_x-r, coord_y-r, coord_x+r, coord_y+r, fill=color)  # Рисует овал, в случайной позиции


def circular_path1(x, y, radius, delta_ang, start_ang=0):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path2(x, y, radius, delta_ang, start_ang=120):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path3(x, y, radius, delta_ang, start_ang=40):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path4(x, y, radius, delta_ang, start_ang=320):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path5(x, y, radius, delta_ang, start_ang=80):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path6(x, y, radius, delta_ang, start_ang=240):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path7(x, y, radius, delta_ang, start_ang=160):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path8(x, y, radius, delta_ang, start_ang=200):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def circular_path9(x, y, radius, delta_ang, start_ang=280):
    # Бесконечно генерирует координаты кругового пути через каждые градусы delta_ang
    ang = start_ang % 360
    while True:
        yield x + radius * cos(ang), y + radius * sin(ang)
        ang = (ang + delta_ang) % 360


def update_position1(canvas, id, UI_obj, path_iter):
    UI_obj.x, UI_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = UI_obj.x - oldx, UI_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_mercury, update_position1, canvas, id, UI_obj, path_iter)


def update_position2(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_venus, update_position2, canvas, id, Planet_obj, path_iter)


def update_position3(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_earth, update_position3, canvas, id, Planet_obj, path_iter)


def update_position4(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_mars, update_position4, canvas, id, Planet_obj, path_iter)


def update_position5(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_jupiter, update_position5, canvas, id, Planet_obj, path_iter)


def update_position6(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_saturn, update_position6, canvas, id, Planet_obj, path_iter)


def update_position7(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_uranium, update_position7, canvas, id, Planet_obj, path_iter)


def update_position8(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_neptune, update_position8, canvas, id, Planet_obj, path_iter)


def update_position9(canvas, id, Planet_obj, path_iter):
    Planet_obj.x, Planet_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = Planet_obj.x - oldx, Planet_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(delay_pluto, update_position9, canvas, id, Planet_obj, path_iter)


sun_obj = Planet(635, 360, 25)
mercury_obj = Planet(635+40, 360, 4)
venus_obj = Planet(635+80, 360, 8)
earth_obj = Planet(635+120, 360, 8)
mars_obj = Planet(635+160, 360, 6)
jupiter_obj = Planet(635+200, 360, 20)
saturn_obj = Planet(635+240, 360, 16)
uranium_obj = Planet(635+280, 360, 12)
neptune_obj = Planet(635+320, 360, 12)
pluto_obj = Planet(635+55, 15, 6)

sun = canvas.create_oval(sun_obj.bounds(), fill='yellow', width=0)
canvas.tag_bind(sun, '<Button-1>', UI.Sun)
mercury = canvas.create_oval(mercury_obj.bounds(), fill='grey', width=0)
canvas.tag_bind(mercury, '<Button-1>', UI.Mercury)
venus = canvas.create_oval(venus_obj.bounds(), fill='orange', width=0)
canvas.tag_bind(venus, '<Button-1>', UI.Venera)
earth = canvas.create_oval(earth_obj.bounds(), fill='light blue', width=0)
canvas.tag_bind(earth, '<Button-1>', UI.Earth)
mars = canvas.create_oval(mars_obj.bounds(), fill="red", width=0)
canvas.tag_bind(mars, '<Button-1>', UI.Mars)
jupiter = canvas.create_oval(jupiter_obj.bounds(), fill='brown', width=0)
canvas.tag_bind(jupiter, '<Button-1>', UI.Yupiter)
saturn = canvas.create_oval(saturn_obj.bounds(), fill='light gray', width=0)
canvas.tag_bind(saturn, '<Button-1>', UI.Saturn)
uranium = canvas.create_oval(uranium_obj.bounds(), fill='light green', width=0)
canvas.tag_bind(uranium, '<Button-1>', UI.Uran)
neptune = canvas.create_oval(neptune_obj.bounds(), fill='blue', width=0)
canvas.tag_bind(neptune, '<Button-1>', UI.Neptun)
pluto = canvas.create_oval(pluto_obj.bounds(), fill='dark grey', width=0)
canvas.tag_bind(pluto, '<Button-1>', UI.Pluton)

orbital_radius_mercury = math.hypot(sun_obj.x - mercury_obj.x, sun_obj.y - mercury_obj.y)
orbital_radius_venus = math.hypot(sun_obj.x - venus_obj.x, sun_obj.y - venus_obj.y)
orbital_radius_earth = math.hypot(sun_obj.x - earth_obj.x, sun_obj.y - earth_obj.y)
orbital_radius_mars = math.hypot(sun_obj.x - mars_obj.x, sun_obj.y - earth_obj.y)
orbital_radius_jupiter = math.hypot(sun_obj.x - jupiter_obj.x, sun_obj.y - jupiter_obj.y)
orbital_radius_saturn = math.hypot(sun_obj.x - saturn_obj.x, sun_obj.y - jupiter_obj.y)
orbital_radius_uranium = math.hypot(sun_obj.x - uranium_obj.x, sun_obj.y - uranium_obj.y)
orbital_radius_neptune = math.hypot(sun_obj.x - neptune_obj.x, sun_obj.y - neptune_obj.y)
orbital_radius_pluto = math.hypot(sun_obj.x - pluto_obj.x, sun_obj.y - pluto_obj.y)

path_iter_earth = circular_path1(sun_obj.x, sun_obj.y, orbital_radius_earth, CIRCULAR_PATH_INCR)
path_iter_mercury = circular_path2(sun_obj.x, sun_obj.y, orbital_radius_mercury, CIRCULAR_PATH_INCR)
path_iter_venus = circular_path3(sun_obj.x, sun_obj.y, orbital_radius_venus, CIRCULAR_PATH_INCR)
path_iter_mars = circular_path4(sun_obj.x, sun_obj.y, orbital_radius_mars, CIRCULAR_PATH_INCR)
path_iter_jupiter = circular_path5(sun_obj.x, sun_obj.y, orbital_radius_jupiter, CIRCULAR_PATH_INCR)
path_iter_saturn = circular_path6(sun_obj.x, sun_obj.y, orbital_radius_saturn, CIRCULAR_PATH_INCR)
path_iter_uranium = circular_path7(sun_obj.x, sun_obj.y, orbital_radius_uranium, CIRCULAR_PATH_INCR)
path_iter_neptune = circular_path8(sun_obj.x, sun_obj.y, orbital_radius_neptune, CIRCULAR_PATH_INCR)
path_iter_pluto = circular_path9(sun_obj.x, sun_obj.y, orbital_radius_pluto, CIRCULAR_PATH_INCR)

next(path_iter_earth)  # простой генератор
next(path_iter_mercury)
next(path_iter_venus)
next(path_iter_mars)
next(path_iter_jupiter)
next(path_iter_saturn)
next(path_iter_uranium)
next(path_iter_neptune)
next(path_iter_pluto)

SKY()
root.after(delay_earth, update_position3, canvas, earth, earth_obj, path_iter_earth)
root.after(delay_mercury, update_position1, canvas, mercury, mercury_obj, path_iter_mercury)
root.after(delay_venus, update_position2, canvas, venus, venus_obj, path_iter_venus)
root.after(delay_mars, update_position4, canvas, mars, mars_obj, path_iter_mars)
root.after(delay_jupiter, update_position5, canvas, jupiter, jupiter_obj, path_iter_jupiter)
root.after(delay_saturn, update_position6, canvas, saturn, saturn_obj, path_iter_saturn)
root.after(delay_uranium, update_position7, canvas, uranium, uranium_obj, path_iter_uranium)
root.after(delay_neptune, update_position8, canvas, neptune, neptune_obj, path_iter_neptune)
root.after(delay_pluto, update_position9, canvas, pluto, pluto_obj, path_iter_pluto)
root.mainloop()
