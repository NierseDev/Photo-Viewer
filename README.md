# Photo-Viewer
A Refactor of a Python Project that allows you to view images
<br><br>
This refactor will utilize an extension to the base library (TKinter) for better overall UI design and to lessen complexity. It will also revisit the implementation of functions within the program to better optimize UX design.
<br><br>
<b>Description:</b><br>
This program is a TKinter-based program that allows you to view photos from a given folder, which allows you to view multiple photos.<br>
<hr>
<b>To Build:</b><br>
Create an Environment and install the packages listed in 'requirements.txt'<br>
<ul>
   <li><i>pip install -r requirements.txt</i></li>
</ul>
<br>
<b>To create an executable file:</b><br>
Use pyinstaller and package CustomTKinter with the Python project file:<br><br>
   Command: <i>pyinstaller --noconfirm --onedir --windowed --add-data "Path to CustomTKinter"  "Path to Python Script"</i>
   <br><br>
   To find the location of the CustomTKinter package, use:<br><br>
   Command: <i>pip show customtkinter</i>
   <br><br><br><br><br>
   <hr>
<b>Original Project Author (Before Refactoring):</b><br>
https://github.com/RiteshKH/Photo_Selecter_UI
