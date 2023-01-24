#!/usr/bin/env python3

import tkinter as tk
import operator

# from tkinter import ttk

def plus(a, b):
    return a + b
opr = {
    '+': plus,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': operator.truediv,
    '//': lambda a,b: a//b,
    '**': lambda a,b: a**b,
    '%': lambda a,b: a%b,
    
}

class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Foo"
    title_ = "Reverse calculator"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.title_)
        self.bind("<Escape>", self.quit)
        self.entry = MyEntry(self)
        self.entry.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

        self.entry.bind("<Return>", self.process)
        self.entry.bind("<KP_Enter>", self.process)

        self.listbox.bind("<ButtonRelease-1>", self.onclick)

    def onclick(self, event: tk.Event):
        print(self.listbox.get('anchor'))

    def process(self, e: tk.Event):
        line = self.entry.value
        for token in line.split():
            self.line_process(token)
        self.entry.value = ""

    def line_process(self, token:str):
        try:
            token = token.replace(',', '.')
            number = float(token)
            self.listbox.insert(0, number)
        except ValueError:
            if token in opr:
                a = self.listbox.get(0)
                self.listbox.delete(0)
                b = self.listbox.get(0)
                self.listbox.delete(0)
                self.listbox.insert(0, opr[token](a, b))
            pass

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
