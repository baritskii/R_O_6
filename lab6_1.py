import numpy as np
import cv2
from tkinter import *


def Video(video):


    video.set(3,600) # установка размера окна
    video.set(4,350)

    ret, frame1 = video.read()
    ret, frame2 = video.read()

    while video.isOpened():

        difference = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilate = cv2.dilate(threshold, None, iterations=3)
        contour, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame1, contour, -1, (0, 0, 255), 2)
        cv2.imshow("image", frame1)
        frame1 = frame2
        ret, frame2 = video.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()


def One():
    video = cv2.VideoCapture("video1.mp4")

    Video(video)

def Two():

    video = cv2.VideoCapture(0)

    Video(video)



def Menu():
    window = Tk()

    
    window.title("Menu")

    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200
    window.geometry('600x300+{}+{}'.format(w, h))
    window.configure(bg='#D0FBFF')

    btn = Button(window, text="Распознавание движения на видео", padx=10, pady=7, command =One, bg='#7CFFA8', font="Arial")  
    btn.pack(anchor="center", padx=50, pady=20)

    btn = Button(window, text="Распознавание движения в реале", padx=10, pady=7, command =Two, bg='#7CFFA8', font="Arial")  
    btn.pack(anchor="center", padx=50, pady=20)

    btn1 = Button(window, text="Выход", padx=10, pady=7, command =exit, bg='#7CFFA8', font="Arial")  
    btn1.pack(anchor="center", padx=50, pady=20)
    


    window.mainloop()

Menu()