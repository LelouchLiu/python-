import re
import os
import os.path
print ('导入fileDeal')
class FileDeal:
    def __init__(self,path,id,name):
        self.path=path
        self.id=id
        self.name=name
    def listfile(self):
        # list1=os.listdir(self.path)
        # for f in list1:
        #     if self.id in f and os.path.isfile(os.path.join(self.path,f)):
        #         print(f)
        #     else:
        #          print('no + '+f)
        filelist=[f for f in os.listdir(self.path) if self.id in f and os.path.isfile(os.path.join(self.path,f))]
#获取对应路径下含有指定标识的文件名
        return filelist
    def chname(self):
        para=r'(\d\d?).*(\..*$)'
        r=re.compile(para)
        with open(os.path.join(self.path,'log.txt'),'w+') as f :
            for file in self.listfile():
                s=r.search(file)
                if s  != None:
                    os.rename(os.path.join(self.path,file),os.path.join(self.path,self.name+s.group(1)+s.group(2)))
                    f.writelines(file+'-->'+self.name+s.group(1)+s.group(2)+'\n')


if __name__=='__main__':
    test=FileDeal('H:\\迅雷下载\\[白夜追凶][1-30集][国语中字][MP4][1080P][更多电影关注微信公众号 XXZYQA]\\白夜追凶','白夜','白夜追凶')
    test.chname()