import os
import sys

from queue import PriorityQueue

class heapnode:

	def __init__(self, item, fileHandler):
		self.item = item
		self.fileHandler = fileHandler
	def __lt__(self, other):
		return self.item < other.item


class Main:
  
	def __init__(self):
		self.tempFileHandlers = []
		self.files = []

	def mergeSortFiles(self):
		q = PriorityQueue()
		dir_path = r"~/Study/cmpe273/"
		file_path = r"sorted/sortedFinal"
		fileformat = ".txt"
		for tempFileHandler in self.tempFileHandlers:
			item = int(tempFileHandler.readline().strip())
			q.put(heapnode(item, tempFileHandler))

		sorted_output = []
		file = open(os.path.expanduser(dir_path+file_path+fileformat),'a+')
		while not q.empty():
			if len(sorted_output) >= 100:
				file.write("\n".join(sorted_output))
				file.write("\n")
				sorted_output.clear()
			min_item = q.get()
			sorted_output.append(str(min_item.item))
			fileHandler = min_item.fileHandler
			next_item = fileHandler.readline()
			if next_item:
				q.put(heapnode(int(next_item), fileHandler))
			else: continue
		file.write("\n".join(sorted_output))
		file.close()

	def readData(self):
		dir_path = r"~/Study/cmpe273/"
		file_path = r"unsorted/unsorted_"
		fileformat = ".txt"
		for i in range(1, 11):
			l = []
			with open(os.path.expanduser(dir_path + file_path + str(i) + fileformat)) as f:
				data = f.readline()
				while data:
					l.append(int(data))
					data = f.readline()
			l.sort()
			file = open(os.path.expanduser(dir_path+"sorted/"+"sorted_"+str(i)+fileformat),'w+')
			for j in l:
				file.write(str(j) + "\n")
			file.seek(0)
			self.tempFileHandlers.append(file)
			self.files.append(file)


if __name__=='__main__':
	
	m = Main()
	
	m.readData()

	m.mergeSortFiles()
	
	for i in m.files:
		i.close()