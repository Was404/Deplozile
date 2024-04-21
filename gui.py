from tkinter import *
from res.strings import TITLE, DESTINATION_PATH_ON_PC, FILE_PATH_ON_DEVICE
import ADB_modifyPATH

def Quiestion1():
    if ADB_modifyPATH:
        output_text.insert('PATH already modifed for ADB')
    else:
        ADB_modifyPATH()        

root = Tk()

root['bg'] = '#808080' #background color
root.title(TITLE)
#root.iconbitmap("path_to_icon.ico") # Установка иконки окна
root.wm_attributes('-alpha', 0.9) # прозрачность
root.geometry('340x460')

root.resizable(width=False, height=False)

button = Button(root, text='Reload')
path_pc_label = Label(root, text=DESTINATION_PATH_ON_PC)
output_text = Label(root)
output_text.pack()

button.pack(side=BOTTOM, pady=10)
path_pc_label.pack(side= TOP,padx=120)

root.after(500, Quiestion1) #вызов функции через 0.5 сек
root.mainloop()