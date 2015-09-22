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
		

	def PrintDataALL(tblname, database):
		return_data=[]
		datahash=[]		
		count=0;
		cross_data=[]
		no_columns =0
		k=0
		for j in range(0,len(tblname)):
			column=md.getAllColumns(tblname[j])	

			#print("COLUMN CONTENT\n\n",column)
			datahash=Data.getRows(tblname[j],column,database)
			return_data.append(datahash)
		#print("HELLOW\n",return_data)
		#print(len(return_data))
		

	#def CrossProduct(return_data):
		#for i in range(0, len(return_data),2):
			#print(return_data)
				
		
	def getRows(tblname,column_name,database):
		return_data=[]
		datahash=[]
		data = []
		counter=0

		for j in range(0,len(list(database[tblname].keys()))):
			for i in range(0,len(list(column_name))):
				if column_name[i] in database[tblname][(list(database[tblname].keys()))[j]]:
					data.append(database[tblname][(list(database[tblname].keys()))[j]][column_name[i]])
					#print(data)	
			datahash.append(data)
			data=[]
				
		return datahash

	
		
	def PrintColumn(tblname,targetPrint,database):
		length=0
		count=0
		
		return_select=[]
		return_data = []
		datahash=list()
		
		for i in range(0,len(tblname)):		
			datahash=Data.getRows(tblname[i],targetPrint,database)
			return_data.append(datahash)
		
		#print(return_data)
		a=[]
		a=return_data[0]		
		if len(return_data) > 1:
			for i in range(1,len(return_data)):
				#a=return_data[i]
				#if i+2 < len(return_data):		
				a=(list(itertools.product(a,return_data[i])))
				
			#print("CROSSPRODUCT\n\n\n\n\n\n\n\n\n",a)

		print(len(a),"rows returned")
	
	
		
		#print(return_select)



