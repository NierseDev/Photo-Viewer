import os
import glob
import shutil
import functools
import numpy as np
import tkinter as tk
import customtkinter as ctk
from collections import defaultdict
from tkinter import font, filedialog
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller
        self.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        self.create_widgets()
        self.terminate = False
        self.bg_image = self.controller.bg_image
        self.images = self.controller.images
        self.counter = self.controller.counter
        self.CreateCanvasImage = None

    def create_widgets(self):
        """
        Creates the button widgets for the Photo-Viewer.

        Args:
            self: the instance of the class containing this method.

        Returns:
            Adds the widgets with their pre-disposed placements.
        """

        segUI = font.Font(family='Segoe UI', size=16, weight=font.BOLD)

        # Assets
        photoNext = ImageTk.PhotoImage(Image.open("assets/next.png"))
        photoPrev = ImageTk.PhotoImage(Image.open("assets/prev.png"))

        self.next = ctk.CTkButton(self, image=photoNext, command=self.next_image, hover=True)
        self.next.image = photoNext
        self.next.place(relx = 0.55, rely = 0.15, relwidth = 0.1, relheight = 0.5)
        
        self.prev = ctk.CTkButton(self, image=photoPrev, command=self.prev_image, hover=True)
        self.prev.image = photoPrev
        self.prev.place(relx = 0.35, rely = 0.15, relwidth = 0.1, relheight = 0.5)

    def next_image(self):
        pass

    def prev_image(self):
        pass

    def clear_frame(self, frame):
        frame.pack_forget()
        frame.destroy()

class ImageViewer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.9)

        img = Image.open(self.open_image())
        img = ImageOps.exif_transpose(img)
        self.bg_image = CreateCanvasImage(self, self.images, self.counter)
        self.counter = self.bg_image.counter
        self.title = self.bg_image.title

    def open_image(self):
        """
        Opens a file dialog, loads image information, and initializes variables.

        Args:
            self: the instance of the class containing this method.
        
        Returns:
            The path to the selected image file.
        """

        fileOpen = filedialog.askopenfilename(initialdir='/', title='Select Image', filetypes=(('All Image Files', '*.png *.jpg *.jpeg *.bmp *.ico *.tiff *.webp *.svg'), ('All Files', '*.*')))
        
        if not fileOpen:
            return None
        
        self.main_dir = os.path.dirname(fileOpen)
        self.images = glob.glob(os.path.join(self.main_dir, "*.*"))
        self.counter = self.images.index(fileOpen) + 1

        return fileOpen

class CreateCanvasImage(tk.Frame):
    def  __init__(self, parent, images, counter):
        super().__init__(parent)
        self.pack(side='left', expand=True, fill='both', padx=5)

        self.images = images
        self.counter = counter
        self.image_cache = defaultdict(lambda: None)    # Dictionary to store cached images
        
        self.img_label = tk.Label(self)
        self.img_label.pack()

        self.update_image()

    def update_image(self):
        if self.counter >= len(self.images):
            self.counter = 0

        image_path = self.images[self.counter]
        self.title = image_path

        if image_path in self.image_cache:
            img = self.image_cache[image_path]
        else:
            try:
                img = Image.open(image_path)
            except FileNotFoundError:
                print(f"Error: Image file not found: {image_path}")
                return
        
        # Resampling
        resampleMethod = self._get_resampling_method(image_path)

        # Get frame dimensions
        self.update()
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()

        real_aspect = img.size[0] / img.size[1]
        width = int(real_aspect * frame_height)

        img = ImageOps.exif_transpose(img.resize((width, frame_height), resampleMethod))
        img = ImageOps.pad(img, (frame_width, frame_height), color='black')
        self.image_cache[image_path] = img

        self.counter += 1

    def _get_resampling_method(self, image_path):
        """
        Determines the appropriate resampling method based on the image file extension.

        Args:
            image_path (str): The path to the image file.
        
        Returns:
            The PIL Image.Resampling Method
        """

        ext = image_path.lower().split(".")[-1]

        if ext in ('.jpg', '.jpeg'):
            return Image.Resampling.LANCZOS
        elif ext in ('.png', '.bmp', '.ico', '.tiff', '.webp'):
            return Image.Resampling.NEAREST
        else:
            return Image.Resampling.NEAREST
        
class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.ImageViewer = ImageViewer(parent, self)
        self.title = self.ImageViewer.title
        self.bg_image = self.ImageViewer.bg_image
        self.images = self.ImageViewer.images
        self.counter = self.ImageViewer.counter
        self.main_dir = self.ImageViewer.main_dir

        self.menu = Menu(parent, self)

class Main(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

        # Fetch Screen Size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(f"Resolution: {screen_width, screen_height}")
        self.geometry(f"{screen_width}x{screen_height}")

        self.mainFrame = MainFrame(self)    # Widgets
        self.attributes('-topmost', True)   # Set Above

        self.mainloop()

if __name__ == "__main__":
    Main("Photo Viewer")