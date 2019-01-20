#Creating a custom calculator
'''tcross, wathc
hist  x ( ) Clear
7  8  9 % s Clear
4  5  6 * / m-=
1  2  3 + - m+=
0 00  . + = mrc
'''

import tkinter as tk
from tkinter import font
import math

class Queue:
    def __init__(self, length):
        self.queue = []
        self.len = length
        for i in range(length):
            self.queue.append("")
        self.write = 0
        self.read = 0
        self.count = 0

    def insert(self, val):
        print(self.write)
        self.queue[self.write] = val
        if(self.count>2):
            if(self.write==self.read):
                self.read += 1
                if(self.read >= self.len):
                    self.read = 0
        else: self.count+=1
        self.write += 1
        if(self.write >= self.len):
            self.write = 0

    def get(self):
        x = self.queue[self.read]
        if(self.read>=self.len): self.read = -1
        self.read += 1

    def getAll(self):
        x = self.write-1
        temp = []
        while(x != self.read):
            temp.append(self.queue[x])
            x-=1
            if(x<0): x = self.len-1
        temp.append(self.queue[x])
        return temp

class Calculator:
    def __init__(self):
        self.historyFile = open("E:\\Computer Science\\Programs\\Python\\history.txt", 'r+', encoding = "utf-8")
        hist = self.historyFile.read()
        self.empty = 1                             #This variable helps as an indicator for setting the expression to 0 when an input is given after calculating result
        self.history = Queue(20)
        for each in hist.split("\n"):
            print(hist)
            self.history.insert(each)
        self.historytxt = "\n".join(self.history.getAll())
        self.top = tk.Toplevel()
        self.historymsg = tk.Text(self.top, relief = tk.FLAT, bg = "lavender blush")
        self.historymsg.insert(0.0,self.historytxt)
        self.historymsg.pack()
        self.top.title("History")
        self.top.geometry("400x320+850+200")
        self.top.withdraw()
    

        self.header = font.Font(family = "Haettenschweiler", size = (base.winfo_width()//12))
        fnsize = int(((base.winfo_height()/42) + (base.winfo_width()/36))/2)
        self.general = font.Font(family = "Sitka Heading bold", size = fnsize)
        self.display = tk.Entry(base, bg = "gray25", fg = "khaki", cursor = "xterm", font = self.header, justify = tk.RIGHT)
        self.display.grid(row = 0, column = 0, rowspan = 2, columnspan = 6, sticky = (tk.N, tk.S, tk.E, tk.W))
        self.display.insert(0, "0")

        default_bg = "mint cream"
        default_fg = "black"
        active_bg = "honeydew3"
        active_fg = "black"

        self.expression = "0"
        self.result = "0"
        self.final = "0"

        self.parenOpen = False


        #Row 1
        #history Button
        self.History = tk.Button(base, text = "HISTORY", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.History.grid(row = 2, column = 0, columnspan = 3, sticky = (tk.N, tk.S, tk.E, tk.W))
        self.History.bind("<Enter>", lambda event: self.History.configure(bg = active_bg, fg = active_fg))
        self.History.bind("<Leave>", lambda event: self.History.configure(bg = default_bg, fg = default_fg))
        self.History.bind("<Button-1>", self.showHistory)
        #Left Parenthesis Button
        self.leftParen = tk.Button(base, text = "(", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.leftParen.configure(command = lambda text = self.leftParen.cget("text") : self.input(text))
        self.leftParen.grid(row = 2, column = 3, sticky = (tk.N, tk.S, tk.E, tk.W))
        self.leftParen.bind("<Enter>", lambda event: self.leftParen.configure(bg = active_bg, fg = active_fg))
        self.leftParen.bind("<Leave>", lambda event: self.leftParen.configure(bg = default_bg, fg = default_fg))
        #self..bind("<Button-1>", )
        #Right Parenthesis Button
        self.rightParen = tk.Button(base, text = ")", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.rightParen.configure(command = lambda text = self.rightParen.cget("text") : self.input(text))
        self.rightParen.grid(row = 2, column = 4, sticky = (tk.N, tk.S, tk.E, tk.W))
        self.rightParen.bind("<Enter>", lambda event: self.rightParen.configure(bg = active_bg, fg = active_fg))
        self.rightParen.bind("<Leave>", lambda event: self.rightParen.configure(bg = default_bg, fg = default_fg))
        #Clear All Button
        self.Clear = tk.Button(base, text = "Clear", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.Clear.configure(command = lambda : self.clear())
        self.Clear.grid(row = 2, rowspan = 2, column = 5, sticky = (tk.N, tk.S, tk.E, tk.W))
        self.Clear.bind("<Enter>", lambda event: self.Clear.configure(bg = active_bg, fg = active_fg))
        self.Clear.bind("<Leave>", lambda event: self.Clear.configure(bg = default_bg, fg = default_fg))

        #Row 2#
        #7 Button
        self.seven = tk.Button(base, text = "7", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.seven.configure(command = lambda text = self.seven.cget("text") : self.input(text))
        self.seven.grid(row = 3, column = 0, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.seven.bind("<Enter>", lambda event: self.seven.configure(bg = active_bg, fg = active_fg))
        self.seven.bind("<Leave>", lambda event: self.seven.configure(bg = default_bg, fg = default_fg))
        #8 Button
        self.eight = tk.Button(base, text = "8", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.eight.configure(command = lambda text = self.eight.cget("text") : self.input(text))
        self.eight.grid(row = 3, column = 1, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.eight.bind("<Enter>", lambda event: self.eight.configure(bg = active_bg, fg = active_fg))
        self.eight.bind("<Leave>", lambda event: self.eight.configure(bg = default_bg, fg = default_fg))
        #9 Button
        self.nine = tk.Button(base, text = "9", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.nine.configure(command = lambda text = self.nine.cget("text") : self.input(text))
        self.nine.grid(row = 3, column = 2, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.nine.bind("<Enter>", lambda event: self.nine.configure(bg = active_bg, fg = active_fg))
        self.nine.bind("<Leave>", lambda event: self.nine.configure(bg = default_bg, fg = default_fg))
        #% Button
        self.percent = tk.Button(base, text = "%", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.percent.configure(command = lambda text = self.percent.cget("text") : self.input(text))
        self.percent.grid(row = 3, column = 3, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.percent.bind("<Enter>", lambda event: self.percent.configure(bg = active_bg, fg = active_fg))
        self.percent.bind("<Leave>", lambda event: self.percent.configure(bg = default_bg, fg = default_fg))
        #√ Button
        self.sqroot = tk.Button(base, text = "√", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.sqroot.configure(command = lambda text = self.sqroot.cget("text") : self.input(text))
        self.sqroot.grid(row = 3, column = 4, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.sqroot.bind("<Enter>", lambda event: self.sqroot.configure(bg = active_bg, fg = active_fg))
        self.sqroot.bind("<Leave>", lambda event: self.sqroot.configure(bg = default_bg, fg = default_fg))
        
        #Row 3
        #4 Button
        self.four = tk.Button(base, text = "4", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.four.configure(command = lambda text = self.four.cget("text") : self.input(text))
        self.four.grid(row = 4, column = 0, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.four.bind("<Enter>", lambda event: self.four.configure(bg = active_bg, fg = active_fg))
        self.four.bind("<Leave>", lambda event: self.four.configure(bg = default_bg, fg = default_fg))
        #5 Button
        self.five = tk.Button(base, text = "5", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.five.configure(command = lambda text = self.five.cget("text") : self.input(text))
        self.five.grid(row = 4, column = 1, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.five.bind("<Enter>", lambda event: self.five.configure(bg = active_bg, fg = active_fg))
        self.five.bind("<Leave>", lambda event: self.five.configure(bg = default_bg, fg = default_fg))
        #6 Button
        self.six = tk.Button(base, text = "6", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.six.configure(command = lambda text = self.six.cget("text") : self.input(text))
        self.six.grid(row = 4, column = 2, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.six.bind("<Enter>", lambda event: self.six.configure(bg = active_bg, fg = active_fg))
        self.six.bind("<Leave>", lambda event: self.six.configure(bg = default_bg, fg = default_fg))
        #× Button
        self.multiply = tk.Button(base, text = "×", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.multiply.configure(command = lambda text = self.multiply.cget("text") : self.input(text))
        self.multiply.grid(row = 4, column = 3, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.multiply.bind("<Enter>", lambda event: self.multiply.configure(bg = active_bg, fg = active_fg))
        self.multiply.bind("<Leave>", lambda event: self.multiply.configure(bg = default_bg, fg = default_fg))
        #÷ Button
        self.divide = tk.Button(base, text = "÷", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.divide.configure(command = lambda text = self.divide.cget("text") : self.input(text))
        self.divide.grid(row = 4, column = 4, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.divide.bind("<Enter>", lambda event: self.divide.configure(bg = active_bg, fg = active_fg))
        self.divide.bind("<Leave>", lambda event: self.divide.configure(bg = default_bg, fg = default_fg))
        #M-= Button
        self.M_minus = tk.Button(base, text = "M-=", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.M_minus.configure(command = lambda : self.mPlusMinus(0))
        self.M_minus.grid(row = 4, column = 5, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.M_minus.bind("<Enter>", lambda event: self.M_minus.configure(bg = active_bg, fg = active_fg))
        self.M_minus.bind("<Leave>", lambda event: self.M_minus.configure(bg = default_bg, fg = default_fg))

        #Row 4
        #1 Button
        self.one = tk.Button(base, text = "1", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.one.configure(command = lambda text = self.one.cget("text") : self.input(text))
        self.one.grid(row = 5, column = 0, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.one.bind("<Enter>", lambda event: self.one.configure(bg = active_bg, fg = active_fg))
        self.one.bind("<Leave>", lambda event: self.one.configure(bg = default_bg, fg = default_fg))
        #2 Button
        self.two = tk.Button(base, text = "2", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.two.configure(command = lambda text = self.two.cget("text") : self.input(text))
        self.two.grid(row = 5, column = 1, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.two.bind("<Enter>", lambda event: self.two.configure(bg = active_bg, fg = active_fg))
        self.two.bind("<Leave>", lambda event: self.two.configure(bg = default_bg, fg = default_fg))
        #3 Button
        self.three = tk.Button(base, text = "3", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.three.configure(command = lambda text = self.three.cget("text") : self.input(text))
        self.three.grid(row = 5, column = 2, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.three.bind("<Enter>", lambda event: self.three.configure(bg = active_bg, fg = active_fg))
        self.three.bind("<Leave>", lambda event: self.three.configure(bg = default_bg, fg = default_fg))
        #+ Button
        self.plus = tk.Button(base, text = "+", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.plus.configure(command = lambda text = self.plus.cget("text") : self.input(text))
        self.plus.grid(row = 5, column = 3, rowspan = 2, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.plus.bind("<Enter>", lambda event: self.plus.configure(bg = active_bg, fg = active_fg))
        self.plus.bind("<Leave>", lambda event: self.plus.configure(bg = default_bg, fg = default_fg))
        #- Button
        self.minus = tk.Button(base, text = "-", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.minus.configure(command = lambda text = self.minus.cget("text") : self.input(text))
        self.minus.grid(row = 5, column = 4, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.minus.bind("<Enter>", lambda event: self.minus.configure(bg = active_bg, fg = active_fg))
        self.minus.bind("<Leave>", lambda event: self.minus.configure(bg = default_bg, fg = default_fg))
        #M+= Button
        self.M_plus = tk.Button(base, text = "M+=", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.M_plus.configure(command = lambda : self.mPlusMinus(1))
        self.M_plus.grid(row = 5, column = 5, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.M_plus.bind("<Enter>", lambda event: self.M_plus.configure(bg = active_bg, fg = active_fg))
        self.M_plus.bind("<Leave>", lambda event: self.M_plus.configure(bg = default_bg, fg = default_fg))

        #Row 5
        #0 Button
        self.zero = tk.Button(base, text = "0", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.zero.configure(command = lambda text = self.zero.cget("text") : self.input(text))
        self.zero.grid(row = 6, column = 0, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.zero.bind("<Enter>", lambda event: self.zero.configure(bg = active_bg, fg = active_fg))
        self.zero.bind("<Leave>", lambda event: self.zero.configure(bg = default_bg, fg = default_fg))
        #00 Button
        self.zero2 = tk.Button(base, text = "00", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.zero2.configure(command = lambda text = self.zero2.cget("text") : self.input(text))
        self.zero2.grid(row = 6, column = 1, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.zero2.bind("<Enter>", lambda event: self.zero2.configure(bg = active_bg, fg = active_fg))
        self.zero2.bind("<Leave>", lambda event: self.zero2.configure(bg = default_bg, fg = default_fg))
        #. Button
        self.dot = tk.Button(base, text = ".", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.dot.configure(command = lambda text = self.dot.cget("text") : self.input(text))
        self.dot.grid(row = 6, column = 2, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.dot.bind("<Enter>", lambda event: self.dot.configure(bg = active_bg, fg = active_fg))
        self.dot.bind("<Leave>", lambda event: self.dot.configure(bg = default_bg, fg = default_fg))
        #= Button
        self.equal = tk.Button(base, text = "=", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.equal.configure(command = lambda : self.calculate(self.expression))
        self.equal.grid(row = 6, column = 4, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.equal.bind("<Enter>", lambda event: self.equal.configure(bg = active_bg, fg = active_fg))
        self.equal.bind("<Leave>", lambda event: self.equal.configure(bg = default_bg, fg = default_fg))
        #MRC Button
        self.MRC = tk.Button(base, text = "MRC", font = self.general, relief = tk.GROOVE, bg = default_bg, fg = default_fg)
        self.MRC.configure(command = lambda : self.mrc())
        self.MRC.grid(row = 6, column = 5, sticky = (tk.N, tk.S, tk.W, tk.E))
        self.MRC.bind("<Enter>", lambda event: self.MRC.configure(bg = active_bg, fg = active_fg))
        self.MRC.bind("<Leave>", lambda event: self.MRC.configure(bg = default_bg, fg = default_fg))

    def showHistory(self, event):
        if(self.top.state() == "withdrawn"):
            self.top.deiconify()
            return
        self.top.withdraw()        

    def input(self, text):
        last = len(self.display.get())-1
        if(len(self.display.get())>20):
            return
        if(self.empty):
            self.expression = ""
            self.empty = 0
        if((self.expression == "") and not(text[-1] in "[√0123456789(]")):
            self.expression = "0"
        if(text == "√"):
            text += " ( "
            if(len(self.expression)):
                if(self.expression[-1] in "[1234567890%]"):
                    text = "×" + " " + text
            self.parenOpen = True
        elif((text == "(")):
            if(len(self.expression)):
                if((self.expression[-1] in "[1234567890%]")):
                    text = "×" + " " + text
            self.parenOpen = True
        elif((text == ")") and (self.parenOpen)):
            selfparenOpen = False
        elif(text == "."):
            if(self.display.get()[last] not in "[0123456789]"):
                text = "0" + text
        elif((text in "[+-×÷]") and (self.display.get()[last] in "[+-×÷]")):
            self.expression = self.expression[:last]
        elif((self.display.get()[last] == "(")and (not(text[0] in "[0123456789√]")) or
            ((text == ")") and not(parenOpen)) or
            ((self.display.get()[last] == "\.") and not(text in "[0123456789]")) or
            ((self.display.get()[last-1:] == "√(") and not((text in "[1234567890]") or text == "√(" or text == "(")) or
            ((self.display.get()[last-1:] == "%×") and not((text in "[1234567890]" or text == "√(" or text == "("))) or
            ((self.display.get()[last] in "[+-×÷]") and (text in "[\.%]")) or
            ((self.display.get()[last] is "\.") and (text[-1] == "\."))):
            top = tk.Toplevel()
            msg = tk.Message(top, text = "Wrong Format!", justify = "center")
            top.title("ERROR")
            msg.pack()
            top.geometry("100x70+550+400")
            top.after(1500, top.destroy)
            return
        if(((self.display.get()[last] in "[\.01234565789]") and (not(text[-1] in "[\.01234565789]"))) or
           ((text[-1] in "[+-×÷]") and (not(self.display.get()[last] in "[+-×÷]"))) or
           ((self.display.get()[last] in "[+-×÷]") and (not(text[-1] in "[+-×÷]")))):
            self.expression += " "
        self.expression+=text
        #Replaces the current value of the entry widget with the new value
        self.display.delete(0, last+1)
        self.display.insert(0, self.expression)

    def calculate(self, exp):
        exp_list = exp.split()
        self.result = self.solve(exp_list)[0]

        self.history.insert(self.expression + " = " + self.result)
        self.historytxt = "\n".join(self.history.getAll())
        self.historyFile.truncate(0)
        for each in self.history.getAll():
            self.historyFile.write(each)
            self.historyFile.write("\n")
            print(each, "\n")
        self.historymsg.insert(0.0, self.expression + " = " + self.result + "\n")
        self.historymsg.update()
        
        self.display.delete(0, len(self.display.get()))
        self.display.insert(0, self.result)
        self.expression = self.result
        self.empty = 1

    def solve(self, exp):
        i = start = 0
        end = len(exp)
        if("(" in exp):
            while(i < len(exp)):
                if(exp[i] == "("):
                    start = i
                    j = i + 1
                    for j in range(i+1, len(exp)):
                        if(exp[j] == ")"):
                            end = j
                            break
                    val = (exp[start+1:end])
                    exp = exp[:start] + val + exp[end+1:]
                i += 1
        i = len(exp)-1
        start = end = 0
        if("√" in exp):
            while(i>=0):
                if(exp[i] == "√"):
                    val = str(math.sqrt(float(exp[i+1])))
                    exp = exp[:i] + [val] + exp[i+2:]
                i -= 1
        i = len(exp)-1
        if("%" in exp):
             while(i>=0):
                if(exp[i] == "%"):
                    val = str(float(exp[i-1]) / 100)
                    val = ([val]+exp[i+1:i+3])
                    exp = exp[:i-1] + val + exp[i+3:]
                i -= 1
        #×÷
        i = 0
        if("÷" in exp):
            while(i<len(exp)):
                if(exp[i] == "÷"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 / num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                elif(exp[i] == "×"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 * num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                i += 1     
        elif("×" in exp):
            while(i<len(exp)):
                if(exp[i] == "×"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 * num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                i+=1
        i = 0
        if("+" in exp):
            while(i<len(exp)):
                if(exp[i] == "+"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 + num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                elif(exp[i] == "-"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 - num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                i += 1     
        elif("-" in exp):
            while(i<len(exp)):
                if(exp[i] == "-"):
                    num1 = float(exp[i-1])
                    num2 = float(exp[i+1])
                    val = str(num1 - num2)
                    exp = exp[:i-1] + [val] + exp[i+2:]
                i+=1
        return exp
                    
    def mPlusMinus(self, state):
        self.calculate(self.expression)
        if(state):
            self.final = str(float(self.final) + float(self.result))
            return
        self.final = str(float(self.final) - float(self.result))

    def mrc(self):
        self.display.delete(0, len(self.display.get()))
        self.display.insert(0, self.final)


    def clear(self):
        self.display.delete(0, len(self.display.get()))
        self.display.insert(0, "0")
        self.expression = ""
        self.result = self.final = "0"

def resize(event):
        global screen_width, screen_height
        if((screen_width == base.winfo_width()) and (screen_height == base.winfo_height())):
            return
        screen_width = base.winfo_width()
        screen_height = base.winfo_height()
        for i in range(6):
            base.grid_rowconfigure(i, minsize = (screen_height/7))
            base.grid_columnconfigure(i, minsize = (screen_width/6))
        base.grid_rowconfigure(6, minsize = (screen_height/7))
        base.grid_rowconfigure(7, minsize = (screen_height/7))
        calc.header.configure(size = (base.winfo_width()//12))
        calc.general.configure(size = int(((base.winfo_height()/42) + (base.winfo_width()/36))/2))
        base.update()

def exitWindow():
    calc.historyFile.close()
    base.destroy()

base = tk.Tk()
base.title("Calculator")
base.geometry("360x490+400+150")
base.configure(background = "white")
base.update()
screen_width = base.winfo_width()
screen_height = base.winfo_height()
base.bind("<Configure>", resize)
for i in range(6):
    base.grid_rowconfigure(i, minsize = (screen_height/7))
    base.grid_columnconfigure(i, minsize = (screen_width/6))
base.grid_rowconfigure(6, minsize = (screen_height/7))
base.grid_rowconfigure(7, minsize = (screen_height/7))

base.protocol("WM_DELETE_WINDOW", exitWindow)

calc = Calculator()
base.update()
tk.mainloop()
