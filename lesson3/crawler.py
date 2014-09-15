# coding the webcrawler
import urllib2

# get the page source code
def get_page(url):
	return urllib2.urlopen(url).read()

# get next targe
def get_next_target(page):
	# 
	start_link = page.find('<a href=')
	# if there is not a ref reutn -1
	if start_link == -1:
		return None, 0
	# get the link path
	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote + 1)
	# get the path
	url         = page[start_quote + 1 : end_quote]
	# return the result
	return url, end_quote


# get all the links
def get_all_links(page):
	# assign a variable links
	links = []
	# loop the entire page
	while True:
		# assign url and the last position
		url, endpos = get_next_target(page)
		# if the url exits
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	# return all the links
	return links


test = get_all_links(get_page('https://www.udacity.com/cs101x/index.html'))

print test



