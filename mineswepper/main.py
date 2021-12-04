from tkinter import *
import settings
import utils

root = Tk()
root.configure(bg="black")
root.title("Minesweeper Game")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False) # set resize for height & width

__head__ = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.__height__(25)
)
__head__.place(x=0, y=0)

__left__ = Frame(
    root,
    bg='black',
    width=utils.__width__(25),
    height=utils.__height__(75)
)
__left__.place(x=0,y=utils.__height__(25))

__body__ = Frame(
    root,
    bg='black',
    width=utils.__width__(75),
    height=utils.__height__(75)
)
__body__.place(
    x=utils.__width__(25),
    y=utils.__height__(25)
)

root.mainloop()