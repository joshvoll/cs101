# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
	#look up to all the keyword
	for entry in index:
		if keyword in entry:
			return entry[1]
		

	return []

print lookup(index,'computing')
#>>> ['http://udacity.com','http://npr.org']