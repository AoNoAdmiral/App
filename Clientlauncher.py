import sys
from tkinter import Tk
from Client import Client

if __name__ == "__main__":
	
	root = Tk()
	
	# Create a new client
	app = Client(root)
	app.master.title("Glasshouse")	
	root.mainloop()
	