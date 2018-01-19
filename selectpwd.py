#coding:utf8

import multiprocessing
import codecs
import json
import csv
import os

import sys
reload(sys)
sys.setdefaultencoding("utf8")

src_dir = r"/opt/share/sed_source/step03/"
test_path = [r"000522_cfaf34f17973622_ileehoo_userinfo"]
PROCESS_NUM = 10

'''
返回Conf文件中columns字段对应的值
'''
def LoadConfColumns(filepath):
    with codecs.open(filepath, "r", "utf8") as f:
        conf_line = f.read()
        conf_json = json.loads(conf_line)
        conf_columns = conf_json["columns"]
        return conf_columns.encode("utf8")

'''
返回colunms中字段的下标列表，其中第一位表示有多少个，如果不存在，则返回列表中第一个值为0，其中，输入的columns是List形式
'''
def GetFeatureIndex(columns, feature):
    len = columns.__len__()
    res = [0]
    for i in range(len):
        if columns[i] == feature:
            res[0] += 1
            res.append(i)
    return res

    
'''
将List写入TXT文件
'''
def WriteListToTXT(fd, list):
    for item in list:
        fd.write(item + "\n")


'''
从CSV文件中提取 
    明文     password
    哈希密码 hashpwd
    哈希加盐 hashsalt
输入:CSV文件路径
     文件夹名
'''
def SelectPwd(filepath, dirname, password_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if password_indexs[0] > 0:
            password_file = codecs.open("password/" + dirname + ".txt", "a", "utf8")
            for password_index in password_indexs[1:]:
                values = [row[password_index] for row in reader]
                WriteListToTXT(password_file, values)
            password_file.close()

def SelectHashpwd(filepath, dirname,  hashpwd_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if hashpwd_indexs[0] > 0:
            hashpwd_file = codecs.open("hashpwd/" + dirname + ".txt", "a", "utf8")
            for hashpwd_index in hashpwd_indexs[1:]:
                values = [row[hashpwd_index] for row in reader]
                WriteListToTXT(hashpwd_file, values)
            hashpwd_file.close()

    
def SelectHashsalt(filepath, dirname, hashsalt_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if hashsalt_indexs[0] > 0:
            hashsalt_file = codecs.open("hashsalt/" + dirname + ".txt", "a", "utf8")
            for hashsalt_index in hashsalt_indexs[1:]:
                values = [row[hashsalt_index] for row in reader]
                WriteListToTXT(hashsalt_file, values)
            hashsalt_file.close()

def 


    
def Run(dirnames):
    for dirname in dirnames:
        sub_path = os.path.join(src_dir, dirname)
        for filename in os.listdir(sub_path):
            try:
                if filename.endswith(".conf"):
                    column_str = LoadConfColumns(os.path.join(sub_path, filename))
                    column_list = column_str.split(",")
                    password_indexs = GetFeatureIndex(column_list, "password")
                    hashpwd_indexs = GetFeatureIndex(column_list, "hashpwd")
                    hashsalt_indexs = GetFeatureIndex(column_list, "hashsalt")
                    for _filename in os.listdir(sub_path):
                        if _filename.endswith(".csv"):
                            print _filename + "is processing -------->"
                            SelectPwd(os.path.join(sub_path, _filename), dirname, password_indexs)
                            SelectHashpwd(os.path.join(sub_path, _filename), dirname, hashpwd_indexs)
                            SelectHashsalt(os.path.join(sub_path, _filename), dirname, hashsalt_indexs)
                            print _filename + "is done -------->"
            except BaseException,e:
                print filename
                print e
                continue

if __name__ == "__main__":
    dirnames = os.listdir(src_dir)
    pool = multiprocessing.Pool(processes = PROCESS_NUM)
    file_num = len(dirnames)
    for i in range(0, file_num, file_num / PROCESS_NUM + 1):
        pool.apply_async(Run, (dirnames[i:i+file_num / PROCESS_NUM + 1], ))
    pool.close()
    pool.join()
    
    #Run(test_path)
    
    
