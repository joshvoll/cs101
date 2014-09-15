
# imported libraries
import urllib2

# page method
def get_page(url):
	# return the code of the page
	return urllib2.urlopen(url).read()

# get target link method
def get_next_target(page):
	# get the first link
	start_link = page.find('<a href=')
	# if there is no link return None and 0
	if start_link == -1:
		return None, 0

	# get the first quote
	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote + 1)
	# get the url
	url         = page[start_quote + 1 : end_quote]
	return url, end_quote


def print_all_links(page):
	# while link keep cpming
	while True:
		url, endpos = get_next_target(page)

		# if valid url
		if url:
			print url
			page = page[endpos:]
		else:
			break


print print_all_links(get_page('http://www.sandals.com'))