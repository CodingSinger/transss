import shelve


class WordEntry:
    def __init__(self, en, zh, detail):
        self.en = en
        self.zh = zh
        self.detail = detail
        self.__limit = 3
        self._level = 3

    def setLimit(self, limit):
        self.__limit = limit

    def getLimit(self):
        return self.__limit

    def decrementLimit(self):
        self.__limit -= 1
        return self._limit

    def setlevel(self, level):
        self._level = level

    def incrementLimit(self):
        self.__limit += 1

    def decrementLevel(self):
        self._level -= 1
    def copy(self):
        temp = WordEntry(None,None,None)
        temp.en = self.en
        temp._level = self._level
        temp.__limit = self.__limit
        temp.detail = self.detail
        return temp


def saveWords(filepath, words):
    with shelve.open(filepath) as entrys:
        for i in words:
            entrys[i.en] = i



# words 为单词数组
def delWords(filepath, words):
    deleted = []
    with shelve.open(filepath) as entrys:

        for i in words:
            temp = entrys[i].copy()
            deleted.append(temp)
            del entrys[i]
    return deleted



#移动到高优先级db并且limit加1 非最高优先级答错
def incLevelAndUpdate(src,dst,keys):

    res = delWords(src,keys)
    for r in res:
        r.decrementLimit()
        r.decrementLevel()

    saveWords(dst,res)


#limit+1 仅限于最高优先级的db 答错

def incLimit(path,words):
    with shelve.open(path) as entries:
        for word in words:
            entries[words].incrementLimit()
#limit-1 答对操作

def decLimitIfNotZeroOrRemove(path,words):

    with shelve.open(path) as entries:
        for word in words:
             if entries[words].decrementLimit() == 0:
                 del entries[words]







def getEntriesEn(filepath):
    res = []
    with shelve.open(filepath) as entries:
        for i in entries:
            res.append(entries[i].en)
        # res = map(lambda x:entries[x].en,entries)

    return res