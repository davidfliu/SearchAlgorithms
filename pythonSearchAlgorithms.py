import random

#Linear search program that takes a list and a search value
#with a return value of true or false depending if the search value was found.

def linear(aList, searchValue):
	i = 0
	count = 0
	size = len(aList)
	while i < size:
		if aList[i] == searchValue:
			count += 1
			return True, count   #Returns true/false and the # of comparisons to be used in Question 3.
		i = i + 1
		count += 1
	if aList == []:
		count += 1
	return False, count  


#Binary search program that takes a list and a search value
#with a return value of true or false depending if the search value was found.
def binary(aList, searchValue):
	low = 0
	count = 0
	high = len(aList) - 1
	while low <= high:
		mid = (low + high) // 2
		if searchValue < aList[mid]:
			high = mid - 1
			count += 1
		elif searchValue > aList[mid]:
			low = mid + 1
			count += 1
		else:
			count += 1
			return "true", count   #Returns true/false and the # of comparisons to be used in Question 3.
	if aList == []:
		count += 1
	return "false", count


#Making a table to indicate # of comparisons made for linear and
#binary search.

#Generates random list of numbers of a specific length.
		def generate(numitems):
	mylist = range(numitems)
	random.shuffle(mylist)
	return mylist

#Provides linear and binary search results based on several different list sizes.
#Search value is a random integer. Binary search is through a sorted list, whereas
#the linear search is through a random list.
def generatedList():
	listSize = [10, 100, 1000, 10000, 100000]
	for i in listSize:
		randomList = generate(i)
		sortedList = sorted(randomList)
	 	searchValue = random.randint(1,i)
	 	print "For list size of", i
	 	print "Linear search results:", linear(randomList, searchValue)
	 	print "Binary search results:", binary(sortedList, searchValue)


#Bubble sort program

#Swap function to be used in bubble sort.
def swap(numsList, pos1, pos2):
	numsList[pos1], numsList[pos2] = numsList[pos2], numsList[pos1]

def bubbleSort(numsList):
	size = len(numsList) #Place this operation out of while loop, so it isn't iterated multiple times.
	i = 0
	isSorted = False
	while i < size and not isSorted:
		j = size - 1
		isSorted = True
		while j > i:
			if numsList[j] < numsList[j-1]:
				swap(numsList, j, j-1)
			 	isSorted = False
			j = j - 1
		i = i + 1
	return numsList

#Testing code below:

def testLinear():
	print linear([0, 1, 2, 3, 4, 5], 0)
	print linear([0, 1, 2, 3, 4, 5], 5)
	print linear([0, 1, 2, 3, 4, 5], 3)
	print linear([10, 1, 12, 333, 47, 5], 7)
	print linear([], 4)
	print linear([1], 1)

def testBinary():    
	print binary([1, 7, 9, 45, 67, 136, 154, 200, 719, 1000], 7)
	print binary([1, 7, 9, 45, 67, 136, 154, 200, 719, 1000], 719)
	print binary([1, 7, 9, 45, 67, 136, 154, 200, 719, 1000], 7000)
	print binary([1, 7, 9, 45, 67, 136, 154, 200, 1000], 136)
	print binary([], 10)
	print binary([1], 1)

print "Linear test results:"
testLinear()
print "\n"

print "Binary test results:"
testBinary()
print"\n"

print "List of binary & search results from a given list size:"
generatedList()
print"\n"

print "Bubble sort results:"
print bubbleSort([0,2,5,3,4,9,5,7])  # An example of bubble sort working.
print bubbleSort(generate(10))
print bubbleSort(generate(35))
print bubbleSort(generate(100))


