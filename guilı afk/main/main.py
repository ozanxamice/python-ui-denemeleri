import customtkinter
import time
import pyautogui
import pydirectinput
import cv2 as cv
import sys, os
from threading import Thread

def button_callback():
    print("button pressed")

def main():
    app = customtkinter.CTk()
    app.title("deneme adam")
    app.geometry("600x600")
    app.resizable(width=False, height=False)
    app.grid_columnconfigure(0, weight=1)

    button = customtkinter.CTkButton(app, text="anti afk başlatıcı ", command=antiafk_thread)
    button.grid(row=0, column=0, padx=10, pady=10,columnspan=2, sticky="ew")

    global check_var
    check_var = customtkinter.StringVar(value="off")
    checkbox_1 = customtkinter.CTkCheckBox(app, text="iki oyun modu", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
    checkbox_1.grid(row=1, column=1, padx=20, pady=20, sticky="w")

    global check_var_stop
    check_var_stop = customtkinter.StringVar(value="off")

    checkbox_1 = customtkinter.CTkCheckBox(app, text="programları sonlandır", command=checkbox_event_iki, variable=check_var_stop, onvalue="on", offvalue="off")
    checkbox_1.grid(row=3, column=1, padx=20, pady=20, sticky="w")
    app.mainloop()


def antiafk():
    print("antiafk başlıyor")
    print("oyuna alt tab atmak için 1 snyen var")
    time.sleep(1)
    while check_var_stop.get() == "off":
        pydirectinput.press('space')
        time.sleep(600)

def dubleantiafk():
    print("ikili ekran anti afksı başlıyor")
    print("oyunlara alt tab atmak için 5 snyen var")
    time.sleep(5)
    while check_var_stop.get() == "off":
        # 1. ekran anti afk
        pydirectinput.click(400, 50)
        pydirectinput.press('space')

        # 2. ekran anti afk
        pydirectinput.click(1400, 50)
        pydirectinput.press('space')
        time.sleep(600)
def checkbox_event():
    print("checkbox toggled, current value:",  check_var.get())
def checkbox_event_iki():
    print("checkbox toggled, current value:",  check_var_stop.get())
def antiafk_thread():
    print(check_var.get())
    if check_var.get() == "off":
        Thread(target=antiafk).start()
    elif check_var.get() == "on":
        Thread(target=dubleantiafk).start()

if __name__ == "__main__":
    main()