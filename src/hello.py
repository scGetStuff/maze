from tkinter import Tk, ttk
import tkinter


# https://docs.python.org/3/library/tkinter.html#a-hello-world-program
def doHello1():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


# https://tkdocs.com/tutorial/install.html#helloworld
def doHello2():
    root = Tk()
    ttk.Button(root, text="Hello World").grid()
    root.mainloop()


def main():
    doHello1()
    doHello2()
    tkinter._test()


if __name__ == "__main__":
    main()
