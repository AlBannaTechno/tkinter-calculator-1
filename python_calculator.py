#Python Calculator using Tkinter GUI
from Tkinter import *


class Calculator:
	"""Calculator that implements addition, subtraction, multiplication, and division. Also 
	implements a clear button, and a decimal point."""

	def __init__(self, master):
		self.master = master
		master.title("Python Calculator")
		
		self.display = Entry(master)
		self.display.grid(column = 0, row = 0, columnspan = 3, sticky = N+E+S+W)
		
		self.button_0 = Button(master, text = "0", command = lambda: self.click_event("0"))
		self.button_0.grid(column = 1, row = 4, sticky = NSEW)
		#self.button_0.bind(0)


		self.button_1 = Button(master, text = "1", command = lambda: self.click_event("1"))
		self.button_1.grid(column = 0, row = 3, sticky = N+E+W+S)
		#self.button_1.bind(1, lambda: self.click_event())
		

		self.button_2 = Button(master, text = "2", command = lambda: self.click_event("2"))
		self.button_2.grid(column = 1, row = 3, sticky = N+E+W+S)

		self.button_3 = Button(master, text = "3", command = lambda: self.click_event("3"))
		self.button_3.grid(column = 2, row = 3, sticky = N+E+W+S)

		self.button_4 = Button(master, text = "4", command = lambda: self.click_event("4"))
		self.button_4.grid(column = 0, row = 2, sticky = N+E+W+S)

		self.button_5 = Button(master, text = "5", command = lambda: self.click_event("5"))
		self.button_5.grid(column = 1, row = 2, sticky = N+E+W+S)

		self.button_6 = Button(master, text = "6", command = lambda: self.click_event("6"))
		self.button_6.grid(column = 2, row = 2, sticky = N+E+W+S)

		self.button_7 = Button(master, text = "7", command = lambda: self.click_event("7"))
		self.button_7.grid(column = 0, row = 1, sticky = N+E+W+S)

		self.button_8 = Button(master, text = "8", command = lambda: self.click_event("8"))
		self.button_8.grid(column = 1, row = 1, sticky = N+E+W+S)

		self.button_9 = Button(master, text = "9", command = lambda: self.click_event("9"))
		self.button_9.grid(column = 2, row = 1, sticky = N+E+W+S)

		

		self.button_minus = Button(master, text = "-", command = lambda: self.click_event("-"))
		self.button_minus.grid(column = 3, row = 3, sticky = N+E+W+S)

		self.button_plus = Button(master, text = "+", command = lambda: self.click_event("+"))
		self.button_plus.grid(column = 3, row = 2, sticky = N+E+W+S)

		self.button_multiply = Button(master, text = "x", command = lambda: self.click_event("*"))
		self.button_multiply.grid(column = 3, row = 1, sticky = N+E+W+S)

		self.button_divide = Button(master, text = "/", command = lambda: self.click_event("/"))
		self.button_divide.grid(column = 3, row = 0, sticky = N+E+W+S)

		self.button_equal = Button(master, text = "=", command = lambda: self.equal())
		self.button_equal.grid(column = 3, row = 4, sticky = N+E+W+S)

		self.button_clear = Button(master, text = "C", command = lambda: self.click_event("C"))
		self.button_clear.grid(column = 0, row = 4, sticky = N+E+W+S)

		self.button_decimal = Button(master, text = ".", command = lambda: self.click_event("."))
		self.button_decimal.grid(column = 2, row = 4, sticky = N+E+W+S)

		for row in range(4):
			master.rowconfigure(row, weight = 1)

		for column in range(4):
			master.columnconfigure(column, weight = 1)

	def click_event(self, key):

		#prevents integer division
		if key == "/" and "." not in self.display.get():
			self.display.insert(END, ".0")
			
		if key == "C":
			self.display.delete(0, END)
		else:
			self.display.insert(END, key)

	def equal(self):
		answer = eval(self.display.get())
		self.display.delete(0, END)
		self.display.insert(END, answer)


		


root = Tk()
app = Calculator(root)
root.mainloop()