import tkinter as tk
from tkinter import*
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

        #crates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #position source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column = 0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure that will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creates buton to seelct destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #poositions destination button in GUI using tkinter grid()
        #on the nest row undeer the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creates entry for desitnation directory selection
        self.destination_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pasy are the same as
        #the button ro ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        ####creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delet(0. END) will be clear the content that is inssereted in the ENtry widget
        #this allows th epath to be inserted into the Entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    ###creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear tthe content that is inserted in the ENTRY widget
        #This allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)


    #creates funvtion to transfer files ffrom one directory to another
    def transferFiles(self):
        #getss sourve directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #define an age threshold
        threshold_age = timedelta(hours=24)
        source_files = os.listdir(source)
        for i in source_files:
        #gets a list of files in the source directory
        #runs through each file in source directory
        #####for i in source_files:
            file_path = os.path.join(source, i)
            file_modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            #calculate age of file
            file_age = datetime.now() - file_modification_time
            #check if each file is older than 24 hours
            if file_age < threshold_age:
                #moves each file from the source to the destination
                #####shutil.move(x + '/' + i, destination)
                shutil.move(file_path, os.path.join(destination, i))
                print(i + ' was successfully transferred.')
 
            
        

        
    #creates function to exit program
    def exit_program(self):
        #root is  the main GUI window, the tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()







if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
