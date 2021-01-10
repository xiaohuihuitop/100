import os

"""
for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
一共有多少级目录 就会循环多少次
root 会逐渐深入目录  然后加上 files 中的文件名 就可以得到所有的文件了
"""


def File_Scan(file_dir):
    return_list = []
    for root, dirs, files in os.walk(file_dir):  # 得到当前目录 root 目录列表 dirs 文件列表 files
        # print(root)
        # print(dirs)
        # print(files)
        for file in files:
            file_name = root + "\\" + file
            if os.path.splitext(file_name)[-1] == ".py":
                return_list.append(file_name)

    return return_list


def File_Scan2(open_file_path):
    root_dir = open_file_path
    return_list = []
    file_list = os.listdir(root_dir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(file_list)):
        com_path = os.path.join(root_dir, file_list[i])
        if os.path.isfile(com_path):
            return_list.append(com_path)
        if os.path.isdir(com_path):
            return_list.extend(File_Scan2(com_path))
    return return_list


File_List = File_Scan(os.getcwd())
# print(File_List)


for fil_name in File_List:
    print(fil_name)
