import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		try:
			inputstr = (input("Score DB > "))
			if inputstr == "": continue
			parse = inputstr.split(" ")
			if parse[0] == 'add':
				try:
					record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
					scdb += [record]
				except:
					print('IndexError')

			elif parse[0] == 'del':	
				for k in range(0, len(scdb)):
					for p in (scdb):
						if p['Name'] == parse[1]:
							scdb.remove(p)
			elif parse[0] == 'show':
				try:
					sortKey ='Name' if len(parse) == 1 else parse[1]
					showScoreDB(scdb, sortKey)
				except:
					print('KeyError')

			elif parse[0] == 'quit':
				break
			elif parse[0] == 'find':			
				try:
					for i in scdb:
						if i['Name'] == parse[1]:	
							for j,k in i.items():
								print(j,"=",k,end=" ")
							print()	
				except:
					print('find _Name')
			elif parse[0] == 'inc':
				try:
					for i in scdb:
						if i['Name'] == parse[1]:
							k = int(parse[2]) + int(i['Score'])
							i['Score'] = str(k)
				except:
					print("IndexError")

			else:
				print("Invalid command: " + parse[0])
		except:
			print(' _use quit')

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
