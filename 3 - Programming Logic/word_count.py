def words(string):
	word_list = string.split()
	dic={}
	for x in word_list:
		if not x in  dic:
			dic[x] = string.count(x)
	return dic