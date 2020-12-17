from tkinter import *
import math
from random import randint, choice, random

DELAY = 100
CIRCULAR_PATH_INCR = 10

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

root = Tk()
root.title("easySpace")
root.geometry("1270x720")
root.wm_attributes("-transparent", 'purple')

canvas = Canvas(root, width=1270, height=720, bg='black')
canvas.pack(fill=BOTH, expand=1)


class UI(object):
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


def update_position(canvas, id, UI_obj, path_iter):
    UI_obj.x, UI_obj.y = next(path_iter)  # проводит итерацию пути и установку новой позиции
    # обновление положения соответствующего объекта холста
    x0, y0, x1, y1 = canvas.coords(id)  # координаты холста овала
    oldx, oldy = (x0 + x1) // 2, (y0 + y1) // 2  # текущая центральная точка
    dx, dy = UI_obj.x - oldx, UI_obj.y - oldy  # количество движения
    canvas.move(id, dx, dy)  # перемещение овала на холсте
    # повторение после задержки
    root.after(DELAY, update_position, canvas, id, UI_obj, path_iter)


sun_obj = UI(635, 360, 25)
mercury_obj = UI(635+40, 360, 3)
venus_obj = UI(635+80, 360, 8)
earth_obj = UI(635+120, 360, 8)
mars_obj = UI(635+160, 360, 6)
jupiter_obj = UI(635+200, 360, 20)
saturn_obj = UI(635+240, 360, 16)
uranium_obj = UI(635+280, 360, 12)
neptune_obj = UI(635+320, 360, 12)
pluto_obj = UI(635+345, 360, 6)


def click_sun(event):
    print('Нажали на Солнце')


def click_mercury(event):
    print('Нажали на Меркурий')


def click_venus(event):
    print('Нажали на Венеру')


def click_earth(event):
    print('Нажали на Землю')


def click_mars(event):
    print('Нажали на Марс')


def click_jupiter(event):
    print('Нажали на Юпитер')


def click_saturn(event):
    print('Нажали на Сатурн')


def click_uranium(event):
    print('Нажали на Уран')


def click_neptune(event):
    print('Нажали на Нептун')


def click_pluto(event):
    print('Нажали на Плутон')


sun = canvas.create_oval(sun_obj.bounds(), fill='yellow', width=0)
canvas.tag_bind(sun, '<Button-1>', click_sun)
mercury = canvas.create_oval(mercury_obj.bounds(), fill='grey', width=0)
canvas.tag_bind(mercury, '<Button-1>', click_mercury)
venus = canvas.create_oval(venus_obj.bounds(), fill='orange', width=0)
canvas.tag_bind(venus, '<Button-1>', click_venus)
earth = canvas.create_oval(earth_obj.bounds(), fill='light blue', width=0)
canvas.tag_bind(earth, '<Button-1>', click_earth)
mars = canvas.create_oval(mars_obj.bounds(), fill="red", width=0)
canvas.tag_bind(mars, '<Button-1>', click_mars)
jupiter = canvas.create_oval(jupiter_obj.bounds(), fill='brown', width=0)
canvas.tag_bind(jupiter, '<Button-1>', click_jupiter)
saturn = canvas.create_oval(saturn_obj.bounds(), fill='light gray', width=0)
canvas.tag_bind(saturn, '<Button-1>', click_saturn)
uranium = canvas.create_oval(uranium_obj.bounds(), fill='light green', width=0)
canvas.tag_bind(uranium, '<Button-1>', click_uranium)
neptune = canvas.create_oval(neptune_obj.bounds(), fill='blue', width=0)
canvas.tag_bind(neptune, '<Button-1>', click_neptune)
pluto = canvas.create_oval(pluto_obj.bounds(), fill='dark grey', width=0)
canvas.tag_bind(pluto, '<Button-1>', click_pluto)

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
root.after(DELAY, update_position, canvas, earth, earth_obj, path_iter_earth)
root.after(DELAY, update_position, canvas, mercury, mercury_obj, path_iter_mercury)
root.after(DELAY, update_position, canvas, venus, venus_obj, path_iter_venus)
root.after(DELAY, update_position, canvas, mars, mars_obj, path_iter_mars)
root.after(DELAY, update_position, canvas, jupiter, jupiter_obj, path_iter_jupiter)
root.after(DELAY, update_position, canvas, saturn, saturn_obj, path_iter_saturn)
root.after(DELAY, update_position, canvas, uranium, uranium_obj, path_iter_uranium)
root.after(DELAY, update_position, canvas, neptune, neptune_obj, path_iter_neptune)
root.after(DELAY, update_position, canvas, pluto, pluto_obj, path_iter_pluto)
root.mainloop()

