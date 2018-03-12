import random
import shelve
import WordManager

def testshelveRead():

    with shelve.open("data/level2.db") as d:
        for i in d:
            print(i+ " "+d[i].en+" "+str(d[i].getLimit()))
            x = d[i]


def updateshelveRead(path,en,limit):
    l = WordManager.getEntries(path) #不能这么做 关闭之后 无法对l进行存取操作

    # for i in l:
    #     print(l[i].en)
    # l[en].setLimit(limit)
def testGetEntriesEn(path):
    return WordManager.getEntriesEn(path)








if __name__ == '__main__':
    # testshelveRead()
    # updateshelveRead("data/level2.db","obvious",10)
    # testshelveRead()

    # random.sample(range(1,10),2)
    # res = testGetEntriesEn("data/level2.db")
    #
    # for i in res:
    #     print(i)
