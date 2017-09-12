import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():                           #test3_4.dat read and make dictionary
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []                                #scdb is test3_4.py read and make pickle
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb

def writeScoreDB(scdb):                               # write the data into person db
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):                                       #input and infinite
    while (True):
        inputstr = (input("Score DB >"))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                parse[3]
            except:
                print("Please, enter Name Age Score")
            else:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]

        elif parse[0] == 'del':
            try:
                parse[1]
            except:
                print("Please, enter Name")
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)

        elif parse[0] == 'show':
            try:
                parse[1]
                print("Please, only enter show")
            except:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)

        elif parse[0] == 'find':
            dic_find =[]
            try:
                for p in scdb :
                    if p['Name'] == parse[1]:
                        dic_find += [p]
                    sortKey = 'Name'
                    showScoreDB(dic_find,sortKey)
            except:
                print("Please, enter Name")

        elif parse[0] == 'inc':
            try:
                for p in scdb :
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score'])+int(parse[2]))
            except:
                print("Please, enter Name and Score")

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):                           #show scdb
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

#Name is not exit how?