import shelve


class WordEntry:
    def __init__(self,en,zh,detail):
        self.en = en
        self.zh = zh
        self.detail = detail
        self.__limit = 0
    def setLimit(self,limit):
        self.__limit = limit
    def decrementLimit(self):
        self.__limit -=1





def saveWord(filepath,word):

    with shelve.open(filepath) as entrys:
        entrys[word.en] = word


def delWord(filepath,word):
    with shelve.open(filepath) as entrys:
        del entrys[word.en]










