#!/usr/bin/python

# import libraries

from urllib2 import *

# get the page
def get_page(url):
    page = urlopen(url) 
    return page.read()

# get the target of each link
def get_next_target(page):
	# get the first link
	start_link = page.find('<a href=')
	# if start link
	if start_link == -1:
		return None, 0

	# get the first quote
	start_quote = page.find('"', start_link)
	end_quote   = page.find('"', start_quote + 1)
	# get url
	url         = page[start_quote + 1 : end_quote]
	return url, end_quote

# get all links
def get_all_links(page):
	# initial variable
	links = []
	# get all the page
	while True:
		url, endpos = get_next_target(page)
		# if url
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

# union
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# crawler for the web
def crawl_web(seed):
	# initials variables
	tocrawl = [seed]
	crawled = []
	
	# while there is a page for crawl
	while tocrawl:
		page = tocrawl.pop()
		# if not anymore pages
		if page not in crawled:
			union(tocrawl, get_all_links(get_page(seed)))
			crawled.append(page)
	# return the craled 
	return crawled


# test the code
print crawl_web('http://www.beaches.com')