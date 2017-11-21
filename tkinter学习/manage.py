import sys
sys.path.append('.\批量修改文件名')
from fileDeal import FileDeal

class Manage:
    def fileManage(self,path,id,name):
        fd=FileDeal(path,id,name)
        fd.chname()