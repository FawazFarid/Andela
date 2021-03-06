# -*- coding: utf-8 -*-
import requests

#Prints out the results of the search
def display(data):
	results = 'Search Result : \n\n' 

	if(data['Response'] == 'True'):
		results += 'Title: {}\n\n Year: {}\n\n Plot: {}\n\n Starring: {}\n\n '.format(data['Title'],data['Year'],data['Plot'], data['Actors']) 
	else:
		results += data['Error']

	#encode the string to avoid UnicodeEncodeError
	print results.encode('utf-8')




def movie_search(name):
	"""
	 Search For Movie Information from the Open Movie Database API
	"""
	name_list = name.lower().split() #convert into lower case and split names
	search_query = ''
	for i in name_list:
		search_query += i + '+'

	try:
		#Query the Api and return movie info in json
		r = requests.get('http://www.omdbapi.com/?t=' + search_query + '&y=&plot=full&r=json')
	except:
		raise requests.exceptions.ConnectionError("Connection Problem")	
	
	data = r.json()
	# Display Results
	display(data)



while True:
	movie_name = raw_input('Enter Movie Name : ')
	movie_search(movie_name)