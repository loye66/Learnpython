# -- coding: utf-8 --
import h5py

class  Handlehdf5:
    def __init__(self,path1,path2):
        self.path1 = path1
        self.path2 = path2

    def handlehdf5(self):
        #打开hdf5文件
        time = 0#次数
        f1 = h5py.File(self.path1, "r")
        f2 = h5py.File(self.path2, "r")
        #获取含有@的table列表
        tablelist = []
        for tabindex in range(len(f1.keys())):
            if '@' in f1.keys()[tabindex]:
                tablelist.append(f1.keys()[tabindex])
        # 计算次数
        for tablename in tablelist:
            a = f1[tablename]
            b = f2[tablename]
            for i in range(len(a)):
                for j in range(len((a[i]))):
                    if (a[i][j][0][0] != b[i][j][0][0]):
                        time+=1
        return time

if __name__ == "__main__":
    Handlehdf5 = Handlehdf5("D:\\myword\\compare\\compare\\test_01.hdf5", "D:\\myword\\compare\\compare\\test_02.hdf5")
    difTimes = Handlehdf5.handlehdf5()
    print difTimes


