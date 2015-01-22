from Tkinter import *
import subprocess

class ibuc(Frame):
	
	def __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		self.instruction = Label(self, text = "Copia la direccion web del libro a bajar de www.bajaebooks.com")
		self.instruction.grid(row=0,column=0,columnspan=2, sticky=W)
		
		self.link = Entry(self, width=50)
		self.link.insert(0,'Copia aqui el link')
		self.link.grid(row=1,column=1,sticky=W,pady=10)
		
		self.opt = Entry(self, width=20)
		self.opt.insert(0,'EPUB')
		self.opt.grid(row=2,column=1,sticky=W,pady=10)
		
		self.procesar = Button(self, text="Descargar", command = self.descargar, width=42, height=2)
		self.procesar.grid(row=3,column=1,sticky=W,pady=5)
		
	def descargar(self):
		content = self.link.get() + ' ' + self.opt.get() 
		subprocess.call("py -2 main.py " + content, shell=True)
root = Tk()
root.title("ibuc - Descarga ebooks de bajaebooks.com")
root.iconbitmap(default='favicon.ico')
root.geometry("350x150")
app = ibuc(root)
root.mainloop()