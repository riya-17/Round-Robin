import sys

def words(w):
	count = {} 
	print("==========================================================================================================")
	print("Occurrences of each letter in the text.")
	print("==========================================================================================================")
	for i in w:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1

	#print(count)
	for keys,values in count.items():
		print(keys, ": ", values)
    

def noOfLetters(w):
	freq = {}
	ls = w.split(" ")
	print("==========================================================================================================")
	print("The number of one-letter, two-letter, three-letter words and so on.")
	print("==========================================================================================================")
	for i in ls:
		l = len(i)
		if l in freq:
			freq[l].append(i)
		else:
			freq[l] = []
			freq[l].append(i)

	sortDic = sorted(freq.items())
	#print("frequency of each word",sortDic)
	for i in sortDic:
		print(i)

def OccOfEachDiffWord(w):
	count = {}
	ls = w.split(" ") 

	print("==========================================================================================================")
	print("The number of occurrences of each different word in the text.")
	print("==========================================================================================================")

	for i in ls:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1

	#print(count)
	for keys,values in count.items():
		print(keys, ": ", values)


if __name__ == '__main__':

	f = open("sonnets.txt",'r')
	s = ""

	alist = f.read().splitlines()

	for i in alist:
		s = s+" "+i

	input = int(sys.argv[1])
	strng = ""

	v = 0

	ls = s.split(" ")
	for i in ls:
		l = len(i)
		if(l<=3):
			if(i.isdigit()):
				n = int(i)
				if(n == input):
					j = ls[ls.index(i)+2]
					strng = j
					k = ls.index(i)+3
					for k in range(k, len(ls), 1):
						ll = len(ls[k])
						if(ll<=3):
							if(ls[k].isdigit()):
								v = v+1
								break
						strng = strng+" "+ls[k]
			elif(v==1):
				break
	print("")
	print("Shakspear's Sonnet no. ", input)
	print("")

				

	words(strng)
	print(" ")
	print("----------------------------------------------------------------------------------------------------------")
	print(" ")
	noOfLetters(strng)
	print(" ")
	print("----------------------------------------------------------------------------------------------------------")
	print(" ")
	OccOfEachDiffWord(strng)
