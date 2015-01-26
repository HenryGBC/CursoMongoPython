import pymongo
import sys

# esctablish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.studentstest
grades = db.grades



def remove():
	
	try:
		for i in range(200):
			query ={'student_id': i, 'type': 'homework'}
			cursor = grades.find(query)
			count = 0
			listScore = []
			
			for doc in cursor:
				listScore.append(doc['score'])

			listScore.sort()
			listScore[0]
			queryRemove ={'student_id': i, 'type': 'homework', 'score': listScore[0]}
			doc = grades.remove(queryRemove)
			print "Removing"

	except:
		print "Unexpected error:", sys.exc_info()[0]

	sanity = 0
	
		

remove()