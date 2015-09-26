from Query import *
from FileReader import *
from Select import *
from Metadata import *
from Data import *
class Main:
	database={}
	md=Metadata()
		
	statement=''
	while statement!='quit':
		statement=input("SQL>")
		statement=statement.lower()
		statement=statement.replace('\"',"")
		statement=statement.replace('\'',"")	
		statement=statement.replace(",","|")
		

		print(statement)
		if statement == 'quit':
			break
		else:
			q1=Query(statement,database)
			q1.classify_query();
			
		


	

	

