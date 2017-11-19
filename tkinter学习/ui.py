
import sys
sys.path.append('.\批量修改文件名')
from tkinter import *
from manage import Manage

class Example(Frame):
  
    def __init__(self):
        super().__init__()
         
        self.initUI()
        self.manage=Manage()
    
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
        self.manage.fileManage(path,id,name)


#三个按钮的布局都是建立在self下，即是app下的，所以，在self没有进行pack的时候，三个按钮无法显示出来，
def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()  



if __name__ == '__main__':
    main()   