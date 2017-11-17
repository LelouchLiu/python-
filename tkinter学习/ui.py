from tkinter import *
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from tkinter import *
from fileDeal import FileDeal
class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()
        
    
    def initUI(self):
        
        self.master.title("Simple")
        self.pack(fill=BOTH, expand=1)
        butt=Button(self,text="确认",command=self.onclick).pack(side="bottom")
        self.path=StringVar()
        entryPath=Entry(self,textvariable=self.path).pack(fill='both',side='top')
        self.idtext=StringVar()
        entryId=Entry(self,textvariable=self.idtext).pack()
        self.idtext.set("input file id")
        self.newName=StringVar()
        entryNewName=Entry(self,textvariable=self.newName).pack()
        self.newName.set('input new name')

    def onclick(self):
        print('butt clicked')
        path=self.path.get()
        id=self.idtext.get()
        name=self.newName.get()
        print(path+'\n'+self.idtext.get()+'\n'+self.newName.get())
        deal=FileDeal(path,id,name)
        deal.chname()

#三个按钮的布局都是建立在self下，即是app下的，所以，在self没有进行pack的时候，三个按钮无法显示出来，
def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()  



if __name__ == '__main__':
    main()   