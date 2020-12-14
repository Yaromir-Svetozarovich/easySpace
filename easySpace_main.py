from tkinter import * 
root = Tk()
frame =Frame(root)
root.title("easySpace")
root.geometry("1366x768")
canv = Canvas(root,  bg='black')
canv.pack(fill = BOTH, expand = 1)

class Planet():
    def __init__(self,x, y,r,colormode):
        self.x = 0
        self.y =0
        self.r = 0
        self.colormode = ''
    def restangle():
        canv.create_rectangle(60, 80, 140, 190,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))
        
        
  
Mars = Planet.restangle()
root.mainloop()
