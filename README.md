# ibuc
A script made with love in python, which automates the process of ebook download for the website www.bajaebooks.com, to the not-so-computer-skilled people.

Un script hecho con amor en python, que automatiza el proceso de descarga de ebooks para el sitio web www.bajaebooks.com, para las personas no-tan-hábiles con la computadora.

###Dependencies / Dependencias
Requires ebook-convert, coming from calibre (http://calibre-ebook.com).
My script is already including epub2mobi.py from Juan Reyero. https://github.com/juanre/epub2mobi

Requiere la instalación de Calibre http://calibre-ebook.com y el seteo de EnVars
Mi script ya incluye epub2movi.py, de Juan Reyero. https://github.com/juanre/epub2mobi

Lxml - http://lxml.de/installation.html
Requests - http://docs.python-requests.org/en/latest/
Ghost.py - http://jeanphix.me/Ghost.py/

###Instructions / Instrucciones
Open the file gui.pyw to start using the application.
Just copy the link to your favorite book into the GUI, specify your extension (Currently only *.EPUB* and *.MOBI* [kindle]) and the download begins automatically. If you choose the .MOBI format, the file will be downloaded in a new folder named *kindle* in the same directory the script was executed.

Abre el archivo gui.pyw para comenzar a utilizar la aplicación.
Solamente copia el link de tu libro favorito en la GUI, especifica la extensión deseada (Actualmente solo soporta *.EPUB* y *.MOBI* [kindle]) y la descarga comienza automaticamente. Si seleccionaste el formato .MOBI, el archivo será descargado en una nueva carpeta llamada *kindle* en el mismo directorio en que el script fue ejecutado.