import json
from datetime import datetime


class Article(object):
	"""
	Article class that is responsible for managing articles on your website.
	"""
	def __init__(self, title, author, date, category):
		self.title = title
		self.author = author
		self.date = date
		self.category = category

	# method to output the information into different formats, such as XML and JSON. 
	def write(self, writer):
		return writer.write(self)



class Writer(object):
	"""This is an Abstract Class, Should not be instantiated"""
	
	"""
	method that accepts an Article object as an argument. 
	Any classes implementing this abstract class will be sure to have this method.
	"""
	def write(self, article):
		raise NotImplementedError()

class XMLWriter(Writer):
	@staticmethod
	def write(article):
		if not isinstance(article, Article):
			raise ValueError("provided argument is not of type Article")
		xml = '<article>'
		xml += '<title>' + article.title + '</title>'
		xml += '<author>' + article.author + '</author>'
		xml += '<date>' + article.date + '</date>'
		xml += '<category>' + article.category + '</category>'
		xml += '</article>'
		return xml

class JSONWriter(Writer):
	@staticmethod
	def write(article):
		if not isinstance(article, Article):
			raise ValueError("provided argument is not of type Article")
		json_output = json.dumps(article.__dict__)
		return json_output


#implementation
article = Article('All about Object Oriented Programming', 'Fawaz', str(datetime.now()), 'Programming')

#XML output
print XMLWriter.write(article)


#JSON output
print JSONWriter.write(article)