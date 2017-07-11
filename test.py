# _*_ coding: utf-8 _*_
__author__ = 'alan'
__date__ = '2017/7/11 下午2:34'

import os


def rename():
    count = 0
    path = "/Users/zhouyongqing/Downloads/名录all/wechat"
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        Olddir = os.path.join(path, files)  # 原来的文件路径
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名
        filetype = os.path.splitext(files)[1]  # 文件扩展名
        print(filename, filetype)
        filename = filename.split('_')
        Newdir = os.path.join(path, str(filename[0]) + '.jpg')  # 新的文件路径
        os.rename(Olddir, Newdir)  # 重命名
        count += 1
    print(count)

    from PIL import Image

    count = 0
    # path = "/Users/zhouyongqing/Downloads/名录all/wechat"
    # filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    # for files in filelist:  # 遍历所有文件
    #     Olddir = os.path.join(path, files)  # 原来的文件路径
    #     im = Image.open(Olddir)
    #     (x, y) = im.size  # read image size
    #     if x >= y :
    #         x_s = 140  # define standard width
    #         y_s = y * x_s / x  # calc height based on standard width
    #     if y > x :
    #         y_s = 140
    #         x_s = x * y_s / y
    #     out = im.resize((int(x_s), int(y_s)), Image.ANTIALIAS)  # resize image with high-quality
    #     out.save(Olddir)

    # path = "/Users/zhouyongqing/Downloads/名录all/logo"
    # filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    # for files in filelist:  # 遍历所有文件
    #     Olddir = os.path.join(path, files)  # 原来的文件路径
    #     print(Olddir)
    #     if '.DS_Store' in Olddir :
    #         continue
    #     im = Image.open(Olddir)
    #     (x, y) = im.size  # read image size
    #     if x/y >= 300.0/170:
    #         x_s = 300  # define standard width
    #         y_s = y * x_s / x  # calc height based on standard width
    #     else:
    #         y_s = 170
    #         x_s = x * y_s / y
    #     out = im.resize((int(x_s), int(y_s)), Image.ANTIALIAS)  # resize image with high-quality
    #     out.save(Olddir)

rename()