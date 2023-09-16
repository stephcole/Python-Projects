import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.default_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=3, column=5, padx=(10,10), pady=(10, 10))

        #crates button to allow user to choose custom text
        self.custom_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        #position source button in GUI using tkinter grid()
        self.custom_btn.grid(row=3, column = 6, padx=(10, 10), pady=(10, 10))

        #creates entry for custom text
        self.customHTML = Entry(self.master, text="Enter custom text or click Default HTML page button", width=75)
        self.customHTML.insert(0, "Enter custom text or click Default HTML page button")
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure that will line up
        self.customHTML.grid(row=0, column=0, columnspan=7, padx=(20, 10), pady=(30, 0))



    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.customHTML.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
