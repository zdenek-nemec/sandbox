import pygame
from tkinter import *


def play():
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def sound():
    pygame.mixer.Sound.play(sound_effect)


pygame.init()
sound_effect = pygame.mixer.Sound('crash.wav')

root = Tk()
root.geometry('180x200')

myframe = Frame(root)
myframe.pack()

mylabel = Label(myframe, text="Pygame Mixer")
mylabel.pack()

button1 = Button(myframe, text="Play", command=play, width=15)
button1.pack(pady=5)
button2 = Button(myframe, text="Sound", command=sound, width=15)
button2.pack(pady=5)
button3 = Button(myframe, text="Unpause", command=unpause, width=15)
button3.pack(pady=5)
button4 = Button(myframe, text="Pause", command=pause, width=15)
button4.pack(pady=5)

root.mainloop()
