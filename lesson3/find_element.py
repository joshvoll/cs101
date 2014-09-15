# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.
# this is using the index pages

def find_element(p,t):
	# for loop with the index page
	if t not in p:
		return -1
	return p.index(t)


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1