# Photo-Viewer
A Refactor of a Python Project that allows you to view images
<br><br>
This refactor will utilize an extension to the base library (TKinter) for better overall UI design and to lessen complexity. It will also revisit the implementation of functions within the program to better optimize UX design.
<br><br>
Description:<br>
This program is a TKinter-based program that allows you to view photos from a given folder, which allows you to view multiple photos.<br><br>
To Build:<br>
Create an Environment and install the packages listed in 'requirements.txt'<br>
<ul>
   <li><i>pip install -r requirements.txt</i></li>
</ul>
<br>
To create an executable file:
Use pyinstaller and package CustomTKinter with the Python project file:<br>
   Command: <i>pyinstaller --noconfirm --onedir --windowed --add-data "Path to CustomTKinter"  "Path to Python Script"</i><br><br>
   To find the location of the CustomTKinter package, use:<br>
   Command: <i>pip show customtkinter</i>
   <br><br><br>
   
