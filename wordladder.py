def findword(curr, tmp):
    c = 0
    l = len(curr)

    for i in range(l):
        if curr[i] != tmp[i]:
            c = c+1
        if c > 1:
            break

    if(c==1):
        return 1
    else:
        return 0


class QItem(): 
  
    def __init__(self, word, len): 
        self.word = word 
        self.len = len

def findlen(start, end, D, wrg):
    #print("1st ", start)
    #print("lst ", end)
    #print("D---------------------", D)

    Q = []
    item = QItem(start, 1)
    Q.append(item)
    Res = []

    flg = 0

    while(len(Q)>0):
        curr = Q.pop()

        for i in D:
            tmp = i
            r = findword(curr.word, tmp)
            if(r==1 and i != wrg):
                #print("item--------------------------", item.word)
                Res.append(item.word)
                item.word = tmp
                item.len = curr.len + 1
                Q.append(item)
                
                #print("yeah---------------------------")

                f = findword(end, tmp)
                if(f==1):
                    print("Result-------------")
                    flg = 1
                    item.word = tmp
                    item.len = curr.len + 1
                    Q.append(item)
                    Res.append(item.word)
                    Res.append(end)
                    return(Res)
                
                D.remove(tmp)

if __name__ == '__main__':
    f = open("words.txt", 'r')
    D = f.read().splitlines()
    #print(D)
    start = "flour"
    end = "bread"
    wrg = ""
    r = []
    r = findlen(start, end, D, wrg)
    print(r)
    for i in r:
        print(i)
