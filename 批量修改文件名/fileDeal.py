import re
import os
import os.path
class FileDeal:
    def __init__(self,path,id,name):
        self.path=path
        self.id=id
        self.name=name
    def listfile(self):
        filelist=[f for f in os.listdir(self.path) if self.id in f and os.path.isfile(os.path.join(self.path,f))]
#获取对应路径下含有指定标识的文件名


if __name__=='__main__':
    test=FileDeal('path','id','name')