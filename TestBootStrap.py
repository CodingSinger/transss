# 测试程序 随机取单词 测试 成功limit-1 失败则进行紧急度上升 3-》2-》1
# limit ==0时移出文件夹 往后可以根据limit优先考察limit高的词语
import random

import WordManager

LEVEL1_DB = "data/level1.db"
LEVEL2_DB = "data/level2.db"
LEVEL3_DB = "data/level3.db"


def testStart():
    level1 = WordManager.getEntriesEn(LEVEL1_DB)

    level2 = WordManager.getEntriesEn(LEVEL2_DB)
    level3 = WordManager.getEntriesEn(LEVEL3_DB)

    # level1抽5个 level2抽3个 level3 抽2个

    list1 = random.sample(list(range(len(level1))))
    list2 = random.sample(list(range(len(level2))))
    list3 = random.sample(list(range(len(level3))))

    terrible = []
    wonderful = []
    for i in list1:
        print("测试: " + level1[i])
        answer = input("知道?(Y?N)")

        terrible.append(level2[i]) if answer == "N" else wonderful.append(level1[i])

    ##

    WordManager.decLimitIfNotZeroOrRemove(LEVEL1_DB, wonderful)

    WordManager.incLimit(LEVEL1_DB, terrible)

    terrible.clear()
    wonderful.clear()

    for i in list2:
        print("测试: " + level2[i].en)
        answer = input("知道?(Y?N)")

        terrible.append(level2[i]) if answer == "N" else wonderful.append(level2[i])

    #答对
    WordManager.decLimitIfNotZeroOrRemove(LEVEL2_DB,wonderful)
    #答错
    WordManager.incLevelAndUpdate(LEVEL2_DB,LEVEL1_DB,terrible)


    terrible.clear()
    wonderful.clear()
    for i in list3:
        print("测试: " + level3[i].en)
        answer = input("知道?(Y?N)")

        terrible.append(level3[i]) if answer == "N" else wonderful.append(level3[i])

        # 答对
    WordManager.decLimitIfNotZeroOrRemove(LEVEL3_DB, wonderful)
    # 答错
    WordManager.incLevelAndUpdate(LEVEL3_DB, LEVEL2_DB, terrible)

     

