import shelve


def testshelveRead():
    with shelve.open("data/level2.db") as d:
        for i in d:
            print(d[i].en)

if __name__ == '__main__':
    testshelveRead()