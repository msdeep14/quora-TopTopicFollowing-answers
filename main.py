import requests
from bs4 import BeautifulSoup
import urllib, urllib2, cookielib
from lxml import html
from getpass import getpass

limit = 100

# TO-DO
# def getFollowingList(soup):
# 	#response = requests.get(url)
# 	#soup = BeautifulSoup(response.text, 'html.parser')
# 	div = soup.find('div',{'class':'UserConnectionsFollowingList PagedList'})
# 	print div
# 	user_list = []
# 	if div is not None:
# 		for user in div.find_all('a'):
# 			user_list.append("https://www.quora.com{}".format(url.get('href')))
# 	print user_list

# def loginToQuora(username):
# 	cj = cookielib.CookieJar()
# 	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# 	email = str(raw_input("email: "))
# 	login_data = urllib.urlencode({'email' : email, 'password' :getpass()})
# 	opener.open('https://www.quora.com/{}/following'.format(username), login_data)
# 	resp = opener.open('https://www.quora.com/{}/following'.format(username))
# 	doc = html.fromstring(resp.read())
# 	print html.tostring(doc, pretty_print=True)
	
    

    # s = requests.Session()
    # data = {'email': email,'password':getpass()}
    # res = s.post('https://www.quora.com/{}/following'.format(username), data=data)
    # print res
    # r = s.get('https://www.quora.com/{}/following'.format(username))
    # soup = BeautifulSoup(r.content)
    # print soup
    # div = soup.find('div',{'class':'UserConnectionsFollowingList PagedList'})
    # print div
    # user_list = []
    # if div is not None:
    # 	for user in div.find_all('a'):
    # 		user_list.append("https://www.quora.com{}".format(url.get('href')))
    # print user_list
    #followingList = getFollowingList(soup)


# return list of topic urls
def getTopicLinks(username):
	url = "https://www.quora.com/profile/{}/topics".format(username)
	response = requests.get(url)

	
	soup = BeautifulSoup(response.text, 'html.parser')
	div = soup.find('div', {'class': 'PagedList UserTopicProfileList'})
	#print div
	
	url_list = []	
	if div is not None:
		for url in div.find_all('a'):
			url_list.append("https://www.quora.com{}".format(url.get('href')))
	else:
		print "error,just run script again! [unable to fetch]"
	return url_list


# return topic name
def getTopicName(soup):
	div = soup.find('span',{'class':'TopicName TopicNameSpan'})
	if div is not None:
		div = div.getText()
	return div


# print top 10 url of particular topic link
def printTop(topicLink):
	response = requests.get(topicLink)
	soup = BeautifulSoup(response.text, 'html.parser')
	# topic_name = getTopicName(soup)

	div = soup.find('div', {'class': 'feed'})
	if div is not None:
		div = div.find('span',{'class':'timestamp'})
	# print div
	
	ans_url = []	
	i = 0
	if div is not None:
		for url in div.find_all('a'):
			u = url.get('href')
			if u is not None and i < limit:
				u = u.encode('utf-8')
				u = "https://www.quora.com{}".format(u)
				print u + "\n"
				myfile = open("most-upvoted.txt",'a+')
				myfile.write(u+"\n")
				myfile.close()
				ans_url.append(u)
				i = i + 1
	#print ans_url



def getTopQuestionsLink(topicLinks):
	for url in topicLinks:
		printTop(url)


# edit username to get most upvoted answers
# from topics you are following
# change global var limit to set numbers 
# of question links to find(initial limit = 100)

def main():
	# username = str(raw_input("enter username: "))
	myfile = open("most-upvoted.txt",'w')
	myfile.close()
	username = 'Mandeep-Singh-296'
	# loginToQuora(username)
	topicLinks = getTopicLinks(username)
	topicLinks = list(set(topicLinks)) # remove duplicate links
	getTopQuestionsLink(topicLinks)



if __name__ == "__main__":
	main()