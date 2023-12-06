from brisque import BRISQUE
import os
import glob
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
import shutil
from PIL import Image as Im, ImageTk, ImageOps, ImageFont, ImageDraw

openfile = filedialog.askopenfilename(initialdir='/', title='Select image', filetypes=(('jpeg files', '*.jpg'), ('all files', '*.*')))
main_dir = os.path.dirname(openfile)
image_path = glob.glob(main_dir +"/*.*")
try:
    os.makedirs(main_dir + "/bad_brisque_img")
except FileExistsError:
    print("folder already exists")
select_dir = main_dir + "/bad_brisque_img"

print("Brisque score starting ")
for image in image_path:
    img = Image.open(image)
    img = np.array(img)
    obj = BRISQUE(url=False)
    score = obj.score(img)
    # print(str(score) + "\n")

    if score > 35.0:
        print(image, ":", score)
        shutil.copy(image, select_dir)

print("Brisque scoring done")