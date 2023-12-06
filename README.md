# Photo_Selecter_UI
Fun project - Simple Python UI to choose photos

This is a TKinter based simple UI to select and sort out photos from a given folder. This is particulary helpful when we need to choose multiple images from a huge number of photos inside a folder. It becomes tiresome to select manually by just looking at the thumbnails of the images. Also keeping track of the pre-selected images is a challenge. To help with that, this UI will display the images and provide options to select/de-select images. The selected ones will be watermarked with "SELECTED" tag on revisiting.
All the selected photos will be copied into a new "Select" folder inside the main folder.

1. pic_select_final.py - this contains the python code for the UI. Please install the dependencies (Tkinter, PIL) and execute directly.
2. iqa.py - this provides a Image quality assessment using BRISQUE score for all the photos in the folder. This score helps in determining and sorting the bad quality images. (Considerable BRISQUE range for good quality : Below 40)

3. TO make this environment independent, use pyinstaller and create an executable file"
   command : pyinstaller --onefile --name pic_selection pic_select_final.py
