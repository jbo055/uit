import tkinter as tk
import math

window = tk.Tk()
window.title("Draggable Circles")
window.geometry("400x300")
window.resizable(False, False)

class Circles:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        