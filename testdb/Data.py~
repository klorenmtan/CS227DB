from Metadata import *
import itertools

class Data:

	def __init__(self,tbldata,tblname):
		global md
		md=Metadata()		
		self.database={}
		self.tbldata = tbldata
		self.tblname = tblname
		self.clean_data = {}
		self.getPrimary()
		self.addToHash()


	def getPrimary(self):
		self.primary_keys=[]
		for i in range (0,len(self.tbldata)):
			self.primary_keys.append((self.tbldata[i][0]))
		return self.primary_keys
		

	def addToHash(self):
		items={}		
		items1={}
		items2={}
		columns=md.getAllColumns(self.tblname)
		datatype =md.getAllDatatypes(self.tblname)

		#convertion
		for i in range(0,len(datatype)):			
			for j in range(0,len(self.tbldata)):	
				
				if datatype[i] == 'numeric':
				#	print(self.tbldata[j][i])
				#	print("NUMERIC")
					self.tbldata[j][i]=float(self.tbldata[j][i])
					
				if datatype[i] == 'int':
				#	print(self.tbldata[j][i])
				#	print("INT")
					self.tbldata[j][i]=int(self.tbldata[j][i])
					
				else:			
				#	print(self.tbldata[j][i])
				#	print("STRING")
					self.tbldata[j][i]=(self.tbldata[j][i])
					
											
		for i in range(0,len(self.tbldata)):
			for j in range(0,len(columns)):
				items={columns[j]:self.tbldata[i][j]}
				items1.update(items)
			self.clean_data[self.primary_keys[i]]=items1			
			items1={}
			items={}
							
				
	def getDataHash(self):
		return self.clean_data

	def printData(datahash,tblname,typedata):
		for j in range(0,len(tblname)):
			column=md.getAllColumns(tblname[j])
			for i in range(len(column)):	
				print("%10s"%(column[i]),"\t",end='')
		print()
		if typedata == 1:
			for i in range(0,len(datahash)):
				for j in range(0,len(datahash[i])):
					print("%10s"%(datahash[i][j]),"\t",end='')
				print()
		elif typedata == 2:
			for i in range(0,len(datahash)):
				for j in range(0,len(datahash[i])):		
					if (type(datahash[i])) is tuple:					
						for k in range(0,len(datahash[i][j])):
							if type(datahash[i][j][k]) is list:
								for m in range(0,len(datahash[i][j][k])):
									if type(datahash[i][j][k][m]) is list:
										for n in range (0, len(datahash[i][j][k][m])):
											print("%10s"%(str(datahash[i][j][k][m][n])),"\t",end='')
											#print(type(datahash[i][j][k][m][n]))
												
									else:	
										#print(type(datahash[i][j][k][m]))						
										print("%10s"%(str(datahash[i][j][k][m])),"\t",end='') 															
							else:			
								print("%10s"%(str(datahash[i][j][k])),"\t",end='')
					print()

		
		

	def PrintDataALL(tblname, database):
				
		return_data=[]
		datahash=[]		
		count=0;
		cross_data=[]
		k=0
		for j in range(0,len(tblname)):
			column=md.getAllColumns(tblname[j])	
			datahash=Data.getRows(tblname[j],column,database)
			return_data.append(datahash)
		
		a=[]
		a=return_data[0]		
		j=0
		if len(tblname) > 1:
			for i in range(1,len(return_data)):
				a=(list(itertools.product(return_data[i])))		
			#a=list(map(list,a))
			#print(a)		
			#for i in a:
				#print(i)
			#	b=list(map(list,i))
			#	c=list(itertools.chain.from_iterable(b))
				#d=list(itertools.chain.from_iterable(c))
				#c=list(map(list,b))
				
			print(a)			
			#Data.printData(a,tblname,2)
			#list2=list(itertools.chain.from_iterable(a[0]))
			print(len(a),"rows returned")		
		else:
			Data.printData(return_data[0],tblname,1)
			print(len(return_data[0]),"rows returned")	
			
		
	def getRows(tblname,column_name,database):
		return_data=[]
		datahash=[]
		data = []
		counter=0

		for j in range(0,len(list(database[tblname].keys()))):
			for i in range(0,len(list(column_name))):
				if column_name[i] in database[tblname][(list(database[tblname].keys()))[j]]:
					data.append(database[tblname][(list(database[tblname].keys()))[j]][column_name[i]])						
			datahash.append(data)
			data=[]
		return datahash

	
		
	def PrintColumn(tblname,targetPrint,database):
		length=0
		count=0
		
		return_select=[]
		return_data = []
		datahash=list()
		printMe()
		for i in range(0,len(tblname)):		
			datahash=Data.getRows(tblname[i],targetPrint,database)
			return_data.append(datahash)
		
		
		a=[]
		a=return_data[0]		
		if len(return_data) > 1:
			for i in range(1,len(return_data)):
				a=(list(itertools.product(a,return_data[i])))			
			print(len(a),"rows returned")
		else:
			print(len(return_data[0]),"rows returned")


	


