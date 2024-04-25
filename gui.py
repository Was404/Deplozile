import tkinter as tk
import sys
from res.strings import TITLE, DESTINATION_PATH_ON_PC, FILE_PATH_ON_DEVICE
import ADB_modifyPATH


#def Quiestion1():
#    if ADB_modifyPATH:
#        output_text.insert('PATH already modifed for ADB')
#    else:
#        ADB_modifyPATH()        

def main():
    root = tk.Tk()
    root.title("Deploy_settings")

    root['bg'] = '#808080' #background color
    root.title(TITLE)
    #root.iconbitmap("path_to_icon.ico") # Установка иконки окна
    root.wm_attributes('-alpha', 0.9) # прозрачность
    root.geometry('340x460')
    root.resizable(width=False, height=False)

    btn_wake_up = tk.Button(text="btn wake up")
    btn_wake_up.pack()
    # Example print statements
    #print("This will be redirected to the Tkinter Text widget.")
    #print("You can also see this in the console.")
    #root.after(500,) #вызов функции через 0.5 сек
    root.mainloop()

if __name__ == "__main__":
    main()
