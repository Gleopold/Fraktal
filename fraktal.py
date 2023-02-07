from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class FractalImage:
    def __init__(self, width, height, xmin, xmax, ymin, ymax, maxiter):
        self.width = width
        self.height = height
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.maxiter = maxiter
        self.mandelbrot()

    def mandelbrot(self):
        X = np.linspace(self.xmin, self.xmax, self.width, dtype=np.float32)
        Y = np.linspace(self.ymin, self.ymax, self.height, dtype=np.float32)
        C = X + Y[:, None] * 1j
        Z = np.zeros_like(C, dtype=np.complex64)
        M = np.full(C.shape, True, dtype=bool)
        for i in range(self.maxiter):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
        self.mandelbrot_set = M

    def to_pil_image(self):
        return Image.fromarray(np.uint8(self.mandelbrot_set) * 255)

class FractalImageApp:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.master.title("Fractal Image")
        self.label = Label(self.master, width=self.width, height=self.height)
        self.label.pack()
        self.xmin = -2
        self.xmax = 1
        self.ymin = -1
        self.ymax = 1
        self.maxiter = 256
        self.update_image()

    def update_image(self):
        fi = FractalImage(self.width, self.height, self.xmin, self.xmax, self.ymin, self.ymax, self.maxiter)
        self.photo = ImageTk.PhotoImage(fi.to_pil_image())
        self.label.configure(image=self.photo)

def main():
    root = Tk()
    app = FractalImageApp(root, 512, 512)
    root.mainloop()

if __name__ == "__main__":
    main()
