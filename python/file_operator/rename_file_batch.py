# -*- coding: utf-8 -*-
import os

def rename():
    '''
    将path路径下的文件进行批量重命名(可复制到新路径)
    '''
    path="D:/WorkDoc/vscode/Get-offer"#目标路径
    #newpath = "./skin_masks_resize_rename"
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    
    for files in filelist:#遍历所有文件
        if files==".git":
            continue
        Olddir=os.path.join(path,files)#原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        filename=os.path.splitext(files)[0]#文件名
        #filename=filename.zfill(3);
        #filetype=os.path.splitext(files)[1]#文件扩展名
        #print("filename=",filename,"\n","filetype=",filetype)
        filetype='.cpp'
        newFile=os.path.join(path,filename+filetype)#新的文件路径
        os.rename(Olddir,newFile)#重命名
    print("OK")
        
rename()
