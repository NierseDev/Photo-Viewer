
import os
import glob
from tkinter import font
# from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import shutil
import numpy as np
import functools
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.place(relx = 0, rely = 0.9, relwidth = 1, relheight = 0.1)

        self.create_widgets()
        self.terminate = False
        self.bg_image = self.controller.bg_image
        self.images = self.controller.images
        self.counter = self.controller.counter
        self.flag = self.controller.flag
        self.select_dir = self.controller.main_dir + "/select"
        self.create_canvas_image = None

    def create_widgets(self):
        helv36 = font.Font(family='Helvetica', size=15, weight=font.BOLD)

        self.next = tk.Button(self, text='>>', bd = '5', command=self.next_image, font=helv36)
        self.prev = tk.Button(self, text='<<', bd = '5', command=self.prev_image, font=helv36)
        self.sel = tk.Button(self, text='SELECT', bd = '5', command=self.select, font=helv36)
        self.desel = tk.Button(self, text='DE-SELECT', bd = '5', command=self.deselect, font=helv36)

        self.next.place(relx = 0.55, rely = 0.15, relwidth = 0.1, relheight = 0.5)
        self.prev.place(relx = 0.35, rely = 0.15, relwidth = 0.1, relheight = 0.5)
        self.sel.place(relx = 0.7, rely = 0.15, relwidth = 0.2, relheight = 0.5)
        self.desel.place(relx = 0.1, rely = 0.15, relwidth = 0.2, relheight = 0.5)  


    def next_image(self):
        if self.bg_image:
            self.clear_frame(self.bg_image)
        self.bg_image = Create_canvas_image(self.controller.ImageViewer, self.images, self.counter, self.flag)
        self.counter = self.bg_image.counter
        
    def prev_image(self):
        if self.bg_image:
            self.clear_frame(self.bg_image)
        self.counter -= 2
        self.bg_image = Create_canvas_image(self.controller.ImageViewer, self.images, self.counter, self.flag)
        self.counter = self.bg_image.counter
      
    def select(self):
        shutil.copy(self.images[self.counter-1], self.select_dir)
        self.flag[self.counter-1] = 1
        self.next_image
        
    def deselect(self):
        try:
            os.remove(self.select_dir +"/"+ self.images[self.counter-1].split("\\")[-1])
            self.flag[self.counter-1] = 0
            self.next_image
        except OSError:
            pass
        
    def clear_frame(self, frame):
        frame.pack_forget()
        frame.destroy()

class ImageViewer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.9)

        img = Image.open(self.open_file())
        img = ImageOps.exif_transpose(img)
        self.bg_image = Create_canvas_image(self, self.images, self.counter, self.flag)
        self.counter = self.bg_image.counter
        self.title = self.bg_image.title

    def open_file(self):
        openfile = filedialog.askopenfilename(initialdir='/', title='Select image', filetypes=(('jpeg files', '*.jpg'), ('all files', '*.*')))
        self.main_dir = os.path.dirname(openfile)
        try:
            os.makedirs(self.main_dir + "/select")
        except FileExistsError:
            print("select folder already exists")

        self.select_dir = self.main_dir + "/select"
        self.images = glob.glob(self.main_dir +"/*.*")
        for i, file in enumerate(self.images):
            if file.split("\\")[-1] == openfile.split("/")[-1]:
                self.counter = i+1
        pre_selected_imgs = [im.split("\\")[-1] for im in glob.glob(self.select_dir +"/*.*")]
        self.flag = np.zeros(len(self.images))
        for i, file in enumerate(self.images):
            if file.split("\\")[-1] in pre_selected_imgs:
                self.flag[i] = 1
        # self.title = openfile
        return openfile

class Create_canvas_image(tk.Frame):
    def __init__(self, parent, images, counter, flag):
        super().__init__(parent)
        self.pack(side = 'left', expand = True, fill = 'both', padx = 5, pady = 5)

        self.img = None
        self.img_label = tk.Label(self)
        self.img_label.pack()
        self.counter = counter
        image = images[self.counter]
        self.title = image
        img = Image.open(image)
        real_aspect = img.size[0]/img.size[1]
        self.update()
        width = int(real_aspect * self.winfo_height()) 

        bg_img = img.copy()
        
        if flag[self.counter] == 0:
            img = ImageOps.exif_transpose(img)
            img = img.resize((width, self.winfo_height()), Image.Resampling.NEAREST)
            img = ImageOps.pad(img, (self.winfo_width(), self.winfo_height()), color='black')
            self.photo = ImageTk.PhotoImage(img, master=self)
            self.img_label.config(image=self.photo)

        else:
            bg_img = ImageOps.exif_transpose(bg_img)                
            font = ImageFont.truetype("arial.ttf", 100)
            draw = ImageDraw.Draw(bg_img)
            draw.text((20,20), "SELECTED", (255,0,0), font=font, stroke_width=5, stroke_fill="black")

            bg_img = bg_img.resize((width, self.winfo_height()), Image.Resampling.NEAREST)
            bg_img = ImageOps.pad(bg_img, (self.winfo_width(), self.winfo_height()), color='black')
            self.new_img = ImageTk.PhotoImage(bg_img, master=self)
            self.img_label.config(image=self.new_img)
        
        self.counter += 1
        if self.counter >= len(images):
            self.counter = 0



class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        self.ImageViewer = ImageViewer(parent, self)
        self.title = self.ImageViewer.title
        self.bg_image = self.ImageViewer.bg_image
        self.images = self.ImageViewer.images
        self.counter = self.ImageViewer.counter
        self.flag = self.ImageViewer.flag
        self.main_dir = self.ImageViewer.main_dir

        self.menu = Menu(parent, self)

class Main(tk.Tk):
    def __init__(self, title):
        # main setup
        super().__init__()
        self.title(title)
        #Get the current screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print("Resolution: ",(screen_width, screen_height))
        self.geometry(f'{screen_width}x{screen_height}')

        # widgets 
        self.mainFrame = MainFrame(self)
        # self.title(self.mainFrame.title) 
        
        #Make the window jump above all
        self.attributes('-topmost',True)
  
        # run 
        self.mainloop()

    
if __name__ == "__main__":
    
    Main("Photo Selector")