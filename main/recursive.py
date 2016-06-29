# -*- coding: utf-8 -*-
# 程序实现了图的深度优先递归遍历，用链接矩阵的方法,所用语言python
visited = []  # 全局链表变量，用以标识顶点被访问过与否
depth = []  # 全局变量链表用以存放深度优先遍历结果


class graph:  # 定义一个图的类，变量依次包括顶点个数，边数，存放顶点的链表，存放边的矩阵
    def __init__(self):
        self.Vnum = 0
        self.Enum = 0
        self.aList = []
        self.matrix = [[]]


def DFS(a, ii):  # 深度优先遍历递归函数，调用本身实现遍历

    jj = 0
    visited[ii] = 1

    depth.append(a.aList[ii])
    # print a.aList[ii]
    for jj in range(a.Vnum):
        if a.matrix[ii][jj] == 1 and visited[jj] == 0:  # 若哪个顶点（jj）与ii顶点的在连接矩阵中下标一致的值是1的话，就访问这个jj点，把它的标记改为1
            DFS(a, jj)


def DFSTra(a):
    ii = 0
    for ii in range(a.Vnum):
        visited[ii] = 0  # 将所有顶点标记为未访问过
    for ii in range(a.Vnum):  # 从第0个顶点开始访问
        if visited[ii] == 0:
            DFS(a, ii)

            # 主函数


if __name__ == '__main__':
    ii = 0
    k = 0
    t = 0
    a = graph()  # 定义图的一个对象
    integer1 = raw_input("Enter the num of V:")  # 顶点数
    a.Vnum = int(integer1)
    print "Enter the num of E："  # 边数
    a.Enum = int(raw_input())
    a.matrix = [[0] * a.Vnum for row in range(a.Vnum)]  # 二维矩阵定义，以便给每个矩阵元素赋值
    print "输入各个顶点："  # 输入各个顶点名称
    for ii in range(a.Vnum):
        char1 = raw_input()
        a.aList.append(char1)
    print a.aList,
    for ii in range(a.Vnum):  # 把所有顶点置为未访问过
        integer = 0
        visited.append(integer)
    print " "
    print "V-to-V:"  # 以顶点对来表示边
    for i in range(a.Enum):  # 整个for循环，是用矩阵下标的方式把每条边表示出来
        j = 0
        char1 = raw_input()
        # print "char1=",char1#测试
        char2 = raw_input()
        for j in range(a.Vnum):  # 找到一条边的第一个点在链表中的下标，并且赋给k
            if char1 == a.aList[j]:
                k = j
                # print "k=",k#测试
                break
            else:
                continue
        j = 0

        for j in range(a.Vnum):  # 找到一条边的第二个点在链表中的下标，并且赋给t
            if char2 == a.aList[j]:
                t = j
                # print"t=",t#测试
                break
            else:
                continue
        a.matrix[k][t] = 1
        a.matrix[t][k] = 1  # 把以相连的两个点（第t个值和第k个值）为下标的矩阵值置为1，真
        print (a.aList[k], a.aList[t])
        # aa=0
        # bb=0
        # for aa in range(a.Vnum):#测试矩阵的输出值，发现输出不对，注意第39行二维矩阵定义
        #   for bb in range(a.Vnum):
        #     print(a.matrix[aa][bb])
        # print ","

    # DFS(a,0)
    print "深度优先遍历链表遍历结果为："
    DFSTra(a)  # 进行深度优先遍历
    print depth,
