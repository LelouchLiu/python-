import sys
sys.path.append('.\cfn')
from fileDeal import FileDeal

class Manage:
    def fileManage(self,path,id,name):
        fd=FileDeal(path,id,name)
        fd.chname()