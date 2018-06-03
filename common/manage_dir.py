import os
import time

'''
function：获取文件的全目录，如果不存在则创建
param[0]:文件夹名
'''
def getDirName(file):
    rootdir = os.getcwd()
    filedir = os.path.join(rootdir,file)
    if not os.path.exists(filedir):
        os.mkdir(filedir)
    return filedir

'''
function：设置文件名
param[0]:文件夹名
param[1]:文件后缀名
'''
def getFileName(file,suffix):
    current_time = time.strftime('%Y%m%d%H%M%S',time.localtime())
    filename = os.path.join(getDirName(file),str(current_time) +'.'+ suffix)
    return filename

    
