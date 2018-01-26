#coding:utf8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import codecs
import os
import datetime,time
import multiprocessing

ROOT_DIR = "/opt/share/sed_source/SedEncrypt_li/select pwd/"
LIMIT_SIZE = 16 * 1024 * 1024 * 1024
PROCESS_NUM = 6

def CreateSubFile(dst_path, dst_filename, contents):
    with codecs.open(os.path.join(ROOT_DIR,dst_path, dst_filename), "w", "utf8") as f:
        print "-- create subfile %s --" % dst_filename
        f.writelines(contents)

def CreateSubFileName(src_filename, num):
    pos = src_filename.rindex('.')
    return src_filename[0 : pos] + "_" + str(num) + src_filename[pos:]

def SplitByLineCount(src_path, src_filename, dst_path, size):
    #print "Split"
    with codecs.open(os.path.join(ROOT_DIR, src_path,src_filename), "r", "utf8") as f:
        buf = []
        num = 1
        _t_size = 0
        for line in f:
            #buf.append(line)
            #_t_size += line.__len__()
            if _t_size + line.__len__() >= size:
                CreateSubFile(dst_path, CreateSubFileName(src_filename, num), buf)
                #del buf
                #gc.collect()
                buf = []
                _t_size = 0
                num += 1
            else:
                buf.append(line)
                _t_size += line.__len__()
        if buf.__len__() != 0:
            CreateSubFile(dst_path, CreateSubFileName(src_filename, num), buf)

def CreateFileNameByDatetime():
    dt = datetime.datetime.now()
    tm = time.time()
    #print tm
    #print dt
    filename = str(dt.year)+"_"+str(dt.month)+"_"+str(dt.day)+"_"+str(tm)+".txt"
    #print filename
    return filename

def MergeFile(src_path,src_filename, dst_path, dst_filename, size):
    #print src_path
    #print src_filename
    #print dst_path
    #print dst_filename
    src_filepath = os.path.join(ROOT_DIR, src_path, src_filename)
    dst_filepath = os.path.join(ROOT_DIR,dst_path, dst_filename)
    src_size = os.path.getsize(src_filepath)
    try:
        dst_size = os.path.getsize(dst_filepath)
    except BaseException,e:
        dst_size = 0
    if src_size + dst_size > size:
        filename = CreateFileNameByDatetime()
    else:
        filename = dst_filename
    with codecs.open(os.path.join(ROOT_DIR, dst_path, filename),"a", "utf8") as df:
        with codecs.open(src_filepath, "r", "utf8") as sf:
            content = sf.readlines()
            df.writelines(content)
    return filename

def Process(dirname):
    print dirname 
    dst_filename = CreateFileNameByDatetime()
    #print dst_filename
    src_file_list = os.listdir(os.path.join(ROOT_DIR,dirname))
    #print src_file_list
    dst_path = dirname + "_merge"
    for src_file in src_file_list:
        src_file_path = os.path.join(ROOT_DIR,dirname, src_file)
        if os.path.getsize(src_file_path) > LIMIT_SIZE:
            SplitByLineCount(dirname, src_file, dst_path, LIMIT_SIZE)
        else:
            dst_filename = MergeFile(dirname, src_file, dst_path, dst_filename, LIMIT_SIZE)



if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = PROCESS_NUM)
    pool.apply_async(Process, ("password", ))
    pool.apply_async(Process, ("hashpwd",))
    pool.apply_async(Process, ("hashsalt", ))
    pool.apply_async(Process, ("telnumber", ))
    pool.apply_async(Process, ("im", ))
    pool.apply_async(Process, ("name", ))
    
    pool.close()
    pool.join()
    #Process("password")
    #SplitByLineCount("/opt/share/sed_source/SedEncrypt_li/select pwd/name", "001103_5302bb5d72240c73_sed.txt", "/opt/share/sed_source/SedEncrypt_li/select pwd/name_merge", LIMIT_SIZE)




