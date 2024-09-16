from tkinter import * # Import tkinter
    
class ChangeLabelDemo:
    def __init__(self):
        window = Tk() # Create a window 
        window.title("GUI Demo") # Set a title
        
        # Add a label to frame1
        frame1 = Frame(window) # Create and add a frame to window 
        frame1.pack()        
        
        # Add a label, an entry, a button, and two radio buttons to frame2
        frame2 = Frame(window) # Create and add a frame to window 
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg) 
        bt1 = Button(frame2, text = "OK")
        bt2 = Button(frame2, text = "Cancel")
        cbtBold = Checkbutton(frame2, text = "Bold") 
        cbtItalic = Checkbutton(frame2, text = "Italic") 
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", 
            variable = self.v1, value = 'R') 
        rbYellow = Radiobutton(frame2, text = "Yellow",
                                variable = self.v1, value = 'Y') 
        
        label.grid(row = 1, column = 3)
        entry.grid(row = 1, column = 4)
        bt1.grid(row = 1, column = 1)
        bt2.grid(row = 1, column = 2)
        cbtBold.grid(row = 1, column = 4)
        cbtItalic.grid(row = 1, column = 5)
        rbRed.grid(row = 1, column = 6)
        rbYellow.grid(row = 1, column = 7)
        
        window.mainloop() # Create an event loop
        
ChangeLabelDemo() # Create GUI 
