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
undo_path = "undo.txt"
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
        if columns[i].find(feature) >= 0:
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
                values = []
                for row in reader:
                    try:
                        values.append(row[password])
                    except BaseException,e:
                        continue
                #values = [row[password_index] for row in reader]
                WriteListToTXT(password_file, values)
            password_file.close()

def SelectHashpwd(filepath, dirname,  hashpwd_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if hashpwd_indexs[0] > 0:
            hashpwd_file = codecs.open("hashpwd/" + dirname + ".txt", "a", "utf8")
            for hashpwd_index in hashpwd_indexs[1:]:
                values = []
                for row in reader:
                    try:
                        values.append(row[hashpwd_index])
                    except BaseException,e:
                        continue
                #values = [row[hashpwd_index] for row in reader]
                WriteListToTXT(hashpwd_file, values)
            hashpwd_file.close()

    
def SelectHashsalt(filepath, dirname, hashpwd_indexs, hashsalt_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if hashsalt_indexs[0] > 0 and hashpwd_indexs[0] > 0:
            hashsalt_file = codecs.open("hashsalt/" + dirname + ".txt", "a", "utf8")
            for i in range(1, hashsalt_indexs.__len__()):
                values = []
                for row in reader:
                    try:
                        values.append(row[hashpwd_indexs[i]]+":"+row[hashsalt_indexs[i]])
                    except BaseException,e:
                        continue
                #values = [row[hashsalt_index] for row in reader]
                WriteListToTXT(hashsalt_file, values)
            hashsalt_file.close()

def SelectNameLables(filepath, dirname, name_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if name_indexs[0] > 0:
            name_file = codecs.open("name/" + dirname + ".txt", "a", "utf8")
            for name_index in name_indexs[1:]:
                values = []
                for row in reader:
                    try:
                        values.append(row[name_index])
                    except BaseException,e:
                        continue
                #values = [row[name_index] for row in reader]
                WriteListToTXT(name_file, values)
            name_file.close()

def SelectTelNumber(filepath, dirname, telnumber_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if telnumber_indexs[0] > 0:
            telnumber_file = codecs.open("telnumber/" + dirname + ".txt", "a", "utf8")
            for telnumber_index in telnumber_indexs[1:]:
                values = []
                for row in reader:
                    try:
                        values.append(row[telnumber_index])
                    except BaseException,e:
                        continue
                #values = [row[telnumber_index] for row in reader]
                WriteListToTXT(telnumber_file, values)
            telnumber_file.close()

            
def SelectIm(filepath, dirname, im_indexs):
    with codecs.open(filepath, "rb", "utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_ALL)
        if im_indexs[0] > 0:
            im_file = codecs.open("im/" + dirname + ".txt", "a", "utf8")
            for im_index in im_indexs[1:]:
                values = []
                for row in reader:
                    try:
                        values.append(row[im_index])
                    except BaseException,e:
                        continue
                #values = [row[im_index] for row in reader]
                WriteListToTXT(im_file, values)
            im_file.close()
    
def Run(dirnames):
    print dirnames
    for dirname in dirnames:
        sub_path = os.path.join(src_dir, dirname)
        for filename in os.listdir(sub_path):
            try:
                if filename.endswith(".conf"):
                    column_str = LoadConfColumns(os.path.join(sub_path, filename))
                    column_list = column_str.split(",")
                    #print column_list
                    password_indexs = GetFeatureIndex(column_list, "password")
                    hashpwd_indexs = GetFeatureIndex(column_list, "hashpwd")
                    hashsalt_indexs = GetFeatureIndex(column_list, "hashsalt")
                    name_indexs = GetFeatureIndex(column_list, "name")
                    #print name_indexs
                    telnumber_indexs = GetFeatureIndex(column_list, "telnumber")
                    #print telnumber_indexs
                    im_indexs = GetFeatureIndex(column_list, "im")
                    #print im_indexs
                    for _filename in os.listdir(sub_path):
                        if _filename.endswith(".csv"):
                            print _filename + "is processing -------->"
                            #SelectPwd(os.path.join(sub_path, _filename), dirname, password_indexs)
                            #SelectHashpwd(os.path.join(sub_path, _filename), dirname, hashpwd_indexs)
                            SelectHashsalt(os.path.join(sub_path, _filename), dirname, hashpwd_indexs, hashsalt_indexs)
                            #SelectNameLables(os.path.join(sub_path, _filename), dirname, name_indexs)
                            #SelectTelNumber(os.path.join(sub_path, _filename), dirname, telnumber_indexs)
                            #SelectIm(os.path.join(sub_path, _filename), dirname, im_indexs)
                            print _filename + "is done -------->"
            except BaseException,e:
                print filename
                print e
                continue

def Fix():
    with codecs.open(undo_path, "r", "utf8") as udf:
        undo_list = udf.readlines()
        for i in range(0, undo_list.__len__(), 2):
            dirname = undo_list[i].rstrip("\n")
            filepath = undo_list[i+1].rstrip("\n")

            sub_path = os.path.join(src_dir, dirname)
            for filename in os.listdir(sub_path):
                try:
                    if filename.endswith(".conf"):
                        column_str = LoadConfColumns(os.path.join(sub_path, filename))
                        column_list = column_str.split(",")
                        password_indexs = GetFeatureIndex(column_list, "password")
                        hashpwd_indexs = GetFeatureIndex(column_list, "hashpwd")
                        hashsalt_indexs = GetFeatureIndex(column_list, "hashsalt")
                        name_indexs = GetFeatureIndex(column_list, "name")
                        #print name_indexs
                        telnumber_indexs = GetFeatureIndex(column_list, "telnumber")
                        #print telnumber_indexs
                        im_indexs = GetFeatureIndex(column_list, "im")
                        print filepath + "is processing -------->"
                        SelectPwd(filepath, dirname, password_indexs)
                        SelectHashpwd(filepath, dirname, hashpwd_indexs)
                        SelectHashsalt(filepath, dirname, hashsalt_indexs)
                        SelectNameLables(filepath, dirname, name_indexs)
                        SelectTelNumber(filepath, dirname, telnumber_indexs)
                        SelectIm(filepath, dirname, im_indexs)
                        print filepath + "is done -------->"
                except BaseException,e:
                    print filepath
                    print e
                    continue
                    
            
    
def test():
    columns = ['username', 'username_lower', 'hashpwd']
    name_indexs = GetFeatureIndex(columns, "name")
    print name_indexs
if __name__ == "__main__":
    file_list_txt = r"sort_file.txt"
    dirnames = []
    with codecs.open(file_list_txt, "r", "utf8") as flf:
        for line in flf:
            dirnames.append(line.rstrip("\n"))
    sp_dirnames=[[0,1],[2,4],[5,8],[9,14],[15,22],[23,34],[35,59],[60,180],[181,400],[400,1283]]
    #print dirnames
    ##dirnames = os.listdir(src_dir)
    pool = multiprocessing.Pool(processes = PROCESS_NUM)
    ##file_num = len(dirnames)
    #pool.apply_async(Run, (dirnames[0:2], ))
    #pool.apply_async(Run, (dirnames[2:5], ))
    #pool.apply_async(Run, (dirnames[5:9], ))
    #pool.apply_async(Run, (dirnames[9:15], ))
    #pool.apply_async(Run, (dirnames[15:23], ))
    #pool.apply_async(Run, (dirnames[23:35], ))
    #pool.apply_async(Run, (dirnames[35:60], ))
    #pool.apply_async(Run, (dirnames[60:180], ))
    #pool.apply_async(Run, (dirnames[180:400], ))
    #pool.apply_async(Run, (dirnames[400:1283], ))
    #
    for i in range(PROCESS_NUM):
        pool.apply_async(Run, (dirnames[sp_dirnames[i][0]:sp_dirnames[i][1]+1], ))
    pool.close()
    pool.join()
    #
    ##Run(os.listdir(src_dir))
    #
    ##test()
    #
    #Fix()
