# Photo-Viewer
A Refactor of a Python Project that allows you to view images
<br><br>
This refactor will utilize an extension to the base library (TKinter) for better overall UI design and to lessen complexity. It will also revisit the implementation of functions within the program to better optimize UX design.
<br><br>
Description:
This program is a TKinter-based program that allows you to view photos from a given folder, which allows you to view multiple photos.
<ul>
   <li><i>photo-viewer.py</i></li>
</ul>
<br>
To Build:
Create an Environment and install the packages listed in 'requirements.txt'

To create an executable file:
Use pyinstaller and package CustomTKinter with the Python project file:
   To find the location of the CustomTKinter package, use the command: <i>pip show customtkinter</i>
   <br><br><br>
   Command: <i>pyinstaller --noconfirm --onedir --windowed --add-data "Path to CustomTKinter"  "Path to Python Script"</i>
