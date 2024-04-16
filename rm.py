from tkinter import *
from tkinter import filedialog
from PIL import Image
import rembg
import numpy as np



class remove_bg:
    def __init__(self):
        pass
    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (('text files',".txt"),("all files", "*.*")))
        self.file_path  = self.filename
        self.filename = self.filename.split("/")[-1]
        self.filename = self.filename.split(".")[0]
    def remove_background(self):
        input_image = Image.open(self.file_path)
        input_array = np.array(input_image)
        output_array = rembg.remove(input_array)
        output_image = Image.fromarray(output_array)
        save_image = input("enter if you want save image [y,n]")
        if save_image == "y":
            output_image.save(f"{self.filename}.png")
        else:
            print("click on exit")

rbg = remove_bg()
rbg.browseFiles()
rbg.remove_background()
