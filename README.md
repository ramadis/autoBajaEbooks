# autoBajaEbooks
A script made with love in python, which automates the process of ebook download for the website www.bajaebooks.com, to the not-so-computer-skilled people.

###Dependencies
Requires ebook-convert, coming from calibre (http://calibre-ebook.com).
My script is already including epub2mobi.py from Juan Reyero. https://github.com/juanre/epub2mobi

###Instructions
Open the file gui.pyw to start using the application.
Just copy the link to your favorite book into the GUI, specify your extension (Currently only *.EPUB* and *.MOBI*[kindle]) and the download begins automatically. If you chose the .MOBI format, the file will be downloaded in a new folder named *kindle* in the same directory the script was executed.