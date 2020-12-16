from tkinter import *
import math
from random import randint, choice, random

DELAY = 100
CIRCULAR_PATH_INCR = 10

sin = lambda degs: math.sin(math.radians(degs))
cos = lambda degs: math.cos(math.radians(degs))

root = Tk()
fr = Frame(root)
root.title("easySpace")
root.geometry("1920x1080")
canvas = Canvas(root,  bg='black')
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
        coord_x = randint(0, 1920)  # Выборка координаты x
        coord_y = randint(0, 1080)  # Выборка координаты y
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
    canvas.after(DELAY, update_position, canvas, id, UI_obj, path_iter)


sun_obj = UI(960, 540, 35)
mercury_obj = UI(960+60, 540, 4)
venus_obj = UI(960+100, 540, 12)
earth_obj = UI(960+140, 540, 12)
mars_obj = UI(960+180, 540, 8)
jupiter_obj = UI(960+250, 540, 25)
saturn_obj = UI(960+320, 540, 20)
uranium_obj = UI(960+370, 540, 15)
neptune_obj = UI(960+420, 540, 15)
pluto_obj = UI(960+460, 540, 7)

sun = canvas.create_oval(sun_obj.bounds(), fill='yellow', width=0)
mercury = canvas.create_oval(mercury_obj.bounds(), fill='grey', width=0)
venus = canvas.create_oval(venus_obj.bounds(), fill='orange', width=0)
earth = canvas.create_oval(earth_obj.bounds(), fill='light blue', width=0)
mars = canvas.create_oval(mars_obj.bounds(), fill="red", width=0)
jupiter = canvas.create_oval(jupiter_obj.bounds(), fill='brown', width=0)
saturn = canvas.create_oval(saturn_obj.bounds(), fill='light gray', width=0)
uranium = canvas.create_oval(uranium_obj.bounds(), fill='light green', width=0)
neptune = canvas.create_oval(neptune_obj.bounds(), fill='blue', width=0)
pluto = canvas.create_oval(pluto_obj.bounds(), fill='dark grey', width=0)

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
