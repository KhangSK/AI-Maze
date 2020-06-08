from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
from tkinter.filedialog import askopenfilename


class OpenFileDialog:
    def __init__(self, Title, FileType):
        self.root = Tk()
        self.root.filename = askopenfilename(title=Title, filetypes=FileType)

    def GetFileName(self):
        return self.root.filename

    def Close(self):
        self.root.destroy()


class ChooseAlgorithmAndSpeed:
    def __init__(self, AlgoList):
        self.Algo = "BFS"
        self.Delay = 0
        self.root = Tk()

        self.Algo_Label = Label(master=self.root, text="Algorithm")
        self.Algo_Label.place(x=10, y=15)
        self.Choice = StringVar(self.root)
        self.Choice.set(AlgoList[0])
        self.Algo_Option = OptionMenu(self.root, self.Choice, *AlgoList)
        self.Algo_Option.place(x=80, y=10)

        self.Time_Label = Label(master=self.root, text="Frame delay")
        self.Time_Label.place(x=10, y=60)
        self.Time_Entry = Entry(master=self.root, width=4)
        self.Time_Entry.insert(0, "0.0")
        self.Time_Entry.place(x=100, y=60)

        OK_Button = Button(master=self.root, text="RUN!", width=3,
                           height=1, command=self.Close)
        OK_Button.place(x=50, y=100)

        self.root.title("AI")
        self.root.wait_window()
        

    def Close(self):
        self.Algo = self.Choice.get()
        self.Delay = float(self.Time_Entry.get())
        self.root.destroy()
