from googlesearch import search

query = "inurl:/wp-admin/admin.php?"

links = []
file_lst = open("res.lst", "a+")
for j in search(query, tld="co.in", num=100000, stop=1000000, pause=2):
	# links.append(j)
	file_lst.write(j+'\n')