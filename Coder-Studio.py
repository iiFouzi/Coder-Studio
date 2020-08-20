from tkinter import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
def newFile():
    global file
    root.title("Untitled - Coder Studio")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Coder Studio")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    info_insert()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Coder Studio")
            print("File Saved")
            info_insert()
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    

def sv(self):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Coder Studio")
            print("File Saved")
        info_insert()
    else:
        # Save the file
        try:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
        except:
            return None
    
def runb():
    import webbrowser
    if os.path.splitext(file)[1]=='.htm' or ".html":
        webbrowser.open(os.path.abspath(file))
    else:
        return False

def run():
    if os.path.splitext(file)[1]=='.py':
        try:
            os.system(f'cd {os.path.dirname(os.path.abspath(file))} && python {file}')
        except Exception:
            print ('Unable to detect Path Please Rename The Path by adding "_" or "-" like symbols rather than empty space and then try again')

def info_insert():
    folderinfo.delete(END, END)
    try:
        os.chdir(os.path.dirname(os.path.abspath(file)))
    except Exception:
        print ('Unable to detect Path Please Rename The Path by adding "_" or "-" like symbols rather than empty space and then try again')
    folderlist = os.listdir()

    for folders in folderlist:
        folderinfo.insert(END, folders)
if __name__ == "__main__":
    root=Tk()
    root.title("Coder Studio")
    file = ""
    folder = ""
    Mainmenu = Menu(root)
    # File Menu
    filemenu = Menu(Mainmenu, tearoff=0)
    filemenu.add_command(label="Open File", command=openFile)
    filemenu.add_command(label="New File", command=newFile)
    filemenu.add_command(label="Save File", command=saveFile)
    Mainmenu.add_cascade(label="File", menu=filemenu)
    root.config(menu=Mainmenu)
    #main frame
    main_Frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
    main_Frame.pack(side=TOP, fill=X)
    main_label = Label(main_Frame, text="Coder Studio", bg="black", fg="white")
    main_label.pack()
    #folder info listbox
    folderinfo = Listbox(root, width=30, bg="black", fg="white")
    folderinfo.pack(side=LEFT, fill=BOTH)
    #text area an scroll bar
    scrollbar = Scrollbar(root)
    TextArea = Text(root, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.pack(fill=BOTH, expand=TRUE)
    #button to open file file in browser
    btn = Button(root, text="Open File In Browser", command=runb)
    btn.pack(side=LEFT)
    #button to run .py and .cpp files 
    btn = Button(root, text="Run Python File", command=run)
    btn.pack(side=LEFT, padx=5)
    
    TextArea.bind('<Control-s>', sv)
    root.mainloop()
