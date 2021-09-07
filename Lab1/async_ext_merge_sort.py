import os
import sys
import asyncio
from queue import PriorityQueue

class heapnode:

	def __init__(self, item, fileHandler):
		self.item = item
		self.fileHandler = fileHandler
	def __lt__(self, other):
		return self.item < other.item


tempFileHandlers = []

# def mergeSortFiles():
# 	q = PriorityQueue()
# 	dir_path = r"~/Study/cmpe273/"
# 	file_path = r"sorted/sortedFinal"
# 	fileformat = ".txt"
# 	for tempFileHandler in tempFileHandlers:
# 		item = int(tempFileHandler.readline().strip())
# 		q.put(heapnode(item, tempFileHandler))

# 	sorted_output = []
# 	file = open(os.path.expanduser(dir_path+file_path+fileformat),'a+')
# 	while not q.empty():
# 		if len(sorted_output) >= 100:
# 			file.write("\n".join(sorted_output))
# 			file.write("\n")
# 			sorted_output.clear()
# 		min_item = q.get()
# 		sorted_output.append(str(min_item.item))
# 		fileHandler = min_item.fileHandler
# 		next_item = fileHandler.readline()
# 		if next_item:
# 			q.put(heapnode(int(next_item), fileHandler))
# 		else: 
# 			continue
# 			fileHandler.close()
# 	file.write("\n".join(sorted_output))

async def readData():
	for i in range(1, 11):
		file = asyncio.create_task(sort_files(i))	

async def sort_files(i):
	dir_path = r"~/Study/cmpe273/"
	file_path = r"unsorted/unsorted_"
	fileformat = ".txt"
	l = []
	with open(os.path.expanduser(dir_path + file_path + str(i) + fileformat)) as f:
		data = f.readline()
		while data:
			l.append(int(data))
			task = asyncio.create_task(f.readline())
			data = await task
	l.sort()
	file = open(os.path.expanduser(dir_path+"sorted/"+"sorted_"+str(i)+fileformat),'w+')
	for j in l:
		file.write(str(j) + "\n")
	file.seek(0)
	tempFileHandlers.append(file)



if __name__=='__main__':
	
	asyncio.run(readData())

	# mergeSortFiles()