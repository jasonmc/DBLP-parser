
erdos = u'Paul Erd\xf6s'

def getData():
    import pickle
    authorsFile = open('authors','r')
    return pickle.load(authorsFile)



def findNumber(authors,fromPerson='Tao Lin',toPerson='Donald E. Knuth'):
    global prev
    prev = {}

    searchList = []
    searchList.extend(authors[fromPerson])
    for x in authors[fromPerson]:
        prev[x] = fromPerson
    lookedAt = set([fromPerson])

    num = 1

    if fromPerson == toPerson:
        return 0

    if toPerson in searchList:
        return 1
    else:
        notFound = True
        while notFound:
            num += 1
            #print '-',num
            newSearchList = []
            lookedAt.update(searchList)
            for x in searchList:
                #lookedAt.add(x)
                for author in authors[x]:
                    #distance[author] = num
                    if author == toPerson:
                        prev[author] = x
                        notFound = False
                        b = author
                        while b != fromPerson:
                            print b
                            b = prev[b]
                        return num
                    
                    if not author in lookedAt:
                        newSearchList.append(author)
                        prev[author] = x
                #print 'NewSearchList size is', len(newSearchList)

            searchList = newSearchList

            if not searchList:
                return -1


# def computeNumbers(authors):
#     authorDistances = {}

#     for x in authors:
        

def getPath(authors,fromPerson='Tao Lin',toPerson='Donald E. Knuth'):
    
    currentPerson = fromPerson
    path = []
    
    while currentPerson != toPerson:
        j = []
        for p in authors[currentPerson]:
            j.append((findNumber(authors,p,toPerson),p))
        currentPerson = sorted(j)[0][1]
        print currentPerson
        path.append(currentPerson)

def findNumber2(authors,fromPerson='Tao Lin',toPerson = 'Donald E. Knuth'):
    

    num = 0
    searchList = [fromPerson]
    lookedAt = set([])
    global prev
    prev = {}
    notFound = True
    while notFound:
        newSearchList = []
        lookedAt.update(searchList)
        for s in searchList:
            if s == toPerson:
                p = toPerson
                while p != fromPerson:
                    print p
                    p = prev[p]
                return num
            else:
                #lookedAt.add(s)
                for a in authors[s]:
                    if not a in lookedAt: #and not a in searchList:
                        prev[a] = s
                        newSearchList.append(a)

        num += 1
        searchList = newSearchList

