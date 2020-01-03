import tkinter as tk
import sys
import os

window = tk.Tk()
window.geometry("300x300")
# to rename the title of the window
window.title("SOURCE SEPARATION DATA COLLECTION TOOL")
# pack is used to show the object in the window
# ~ label = tk.Label(window, text = "test text").pack()

# ~ button_widget = tk.Button(window,text="Button")
# ~ button_widget.pack()

# ~ canvas_widget = tk.Canvas(window, width=200, height=100)

label = tk.Label(window, text = "Input # of Takes:").pack()
takes_widget = tk.Entry(window)
takes_widget.insert(0, "3")
takes_widget.pack()

label = tk.Label(window, text = "Input Length of Takes (s)").pack()
inpLength_widget = tk.Entry(window)
inpLength_widget.insert(0, "3")
inpLength_widget.pack()

label = tk.Label(window, text = "Input Desired Sample Rate (Hz)").pack()
sampleRate_widget = tk.Entry(window)
sampleRate_widget.insert(0, "44100")
sampleRate_widget.pack()


def startRecording():
	sampleLength = inpLength_widget.get()
	sampleRate = sampleRate_widget.get()
	print("Sample Length: ", sampleLength, " Sample Rate: ", sampleRate)
	print("---RECORDING START---")
	
	for i in range (int(takes_widget.get())):
		record(sampleLength, sampleRate, i)
		
	print("---RECORDING STOP---")
	
def record(sl, sr, i):
	print("     recording take #" + str(i+1) + "...")
	
	# ~ os.system('python3 play_a.py')
	# ~ os.system('python3 play_b.py')
	#init recording beeps
	os.system('python3 beep.py')
	os.system('python3 beep.py')
	os.system('python3 beep.py')
	
	#record
	# ~ print("Sample Length: ", sl, " Sample Rate: ", sr)
	# ~ print("python3 record.py " + str(sl) + ' ' + str(sr))
	os.system("python3 record.py " + str(sl) + ' ' + str(sr))
	
	#stop recording beep
	os.system('python3 beepstop.py')
	print("     finished")

B=tk.Button(window,text="START RECORDING",command = startRecording)
B.pack()



mainframe = tk.Frame(window)
# ~ mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 10)

# Create a Tkinter variable
tkvar = tk.StringVar(window)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = tk.OptionMenu(mainframe, tkvar, *choices)
tk.Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)



window.mainloop()


#	input number of takes: ___
#	input length of each take: ___
#	sample rate: ____
#	add noise? yes/no
#	record button: X
#		- records for number of takes, playing a 123 beep before each,
#		 stop signal after each
#		- recorded files are saved numerically


# ~ def inptest():
	# ~ print(takes_widget.get());
# ~ C=tk.Button(window,text="inpt text",command= inptest)
# ~ C.pack()


