from __future__ import division
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
from random import randint
from urllib.request import urlopen as uReq
import time
from random import randint
from selenium.webdriver.common.keys import Keys
import itertools

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 
browser =webdriver.Firefox(profile)
linkslist=[]
def functionlist(a,b):
	alphabet='abcdefghijklmnopqrstuvqxyz{|}~'
	def jaccard_index(s1, s2):
		size_s1 = len(s1)
		size_s2 = len(s2)
		intersect = s1 & s2
		size_in = len(intersect)
		jaccard_in = size_in  / (size_s1 + size_s2 - size_in)
		return jaccard_in
	def editDistDP(str1, str2, m, n): 
	    # Create a table to store results of subproblems 
	    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
	  
	    # Fill d[][] in bottom up manner 
	    for i in range(m + 1): 
	        for j in range(n + 1): 
	  
	            # If first string is empty, only option is to 
	            # insert all characters of second string 
	            if i == 0: 
	                dp[i][j] = j    # Min. operations = j 
	  
	            # If second string is empty, only option is to 
	            # remove all characters of second string 
	            elif j == 0: 
	                dp[i][j] = i    # Min. operations = i 
	  
	            # If last characters are same, ignore last char 
	            # and recur for remaining string 
	            elif str1[i-1] == str2[j-1]: 
                	dp[i][j] = dp[i-1][j-1] 
	  
	            # If last character are different, consider all 
	            # possibilities and find minimum 
	            else: 
	                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
	                                   dp[i-1][j],        # Remove 
	                                   dp[i-1][j-1])    # Replace 
	  
	    return dp[m][n]
	def ed(a,b):
		adict={k: alphabet[v] for v, k in enumerate(a)}
		astring=alphabet[:len(a)]
		bdict={}
		bstring=''
		for i in range(len(b)):
			if b[i] in adict:
				bdict[b[i]]=adict[b[i]]
				bstring+=adict[b[i]]
			if b[i] not in adict:
				bdict[b[i]]=alphabet[len(a)+i+1]
				bstring+=alphabet[len(a)+i+1]
		return (astring,bstring)
	astr,bstr=ed(a,b)
	aset=set(list(a))
	bset=set(list(b))
	edit=editDistDP(astr,bstr,len(astr),len(bstr))
	jacc=jaccard_index(aset,bset)
	return (edit,1-jacc)

#time.sleep(randint(500,1000))
urllist = [['https://www.google.co.in/search?q=Sachin+Pilot&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Sachin+Pilot&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Sachin+Pilot&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4', 'https://www.google.co.in/search?q=Sachin+Pilot&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4'], ['https://www.google.co.in/search?q=Google+Jio+deal&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Google+Jio+deal&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Google+Jio+deal&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4', 'https://www.google.co.in/search?q=Google+Jio+deal&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4']]
#time.sleep(randint(2000,2500))
# cities = ['Delhi','Mumbai','Kolkata','Bangalore','Chennai','Hyderabad','Pune']
numbers=[]
numberslist=[]
filename = "tier3CA.csv"
csv_writer = csv.writer(open(filename, 'w'))
cnt = 0
for i in range(len(urllist)):
	sasta=list(urllist[i][0])
	sasta=sasta[:-16]
	sasta.append('CAIQICIFRGVsaGk')
	listToStr = ''.join([str(elem) for elem in sasta])
	browser.get(listToStr)
	content = browser.page_source
	soup = BeautifulSoup(content,"html.parser")
	newlist=[]
	randomnumber=randint(1,10)
	if randomnumber>4:
		time.sleep(randomnumber)
		browser.execute_script("window.scrollTo(0,500)")
		time.sleep(10-randomnumber)
		browser.execute_script("window.scrollTo(0,-269)")
	#for a in soup.findAll('a',href=True, attrs={'class':'g'}):
	links= soup.findAll("div",{"class":"r"})
	#print(links)
	time.sleep(7)
	for link in links:
		temp=str(link)[23:]
		try:
			ind=temp.index('onmouse')
			print(temp[1:ind-2])
			newlist.append(temp[1:ind-2])
		except:
			continue

	cntrlgrplist=newlist
	time.sleep(randint(20,25))
	#cntrlgrplist= ['https://en.wikipedia.org/wiki/Hospital', 'https://www.definitions.net/definition/HOSPITAL', 'https://www.newsweek.com/best-hospitals-2020/india', 'https://www.reuters.com/article/uk-factcheck-hospital-stands-for/false-claim-hospital-stands-for-house-of-sick-people-in-trauma-and-labor-idUSKCN229262', 'https://en.wikipedia.org/wiki/Hospital', 'https://www.justdial.com/Delhi/Private-Hospitals/nct-10390288', 'https://www.britannica.com/science/hospital', 'http://www.indiahealthcaretourism.com/hospital_lists.php?location=11', 'http://health.delhigovt.nic.in/wps/wcm/connect/DoIT_Health/health/home/hospitals/delhi+govt.+hospital', 'https://www.blkhospital.com/', 'https://www.apollohospitals.com/locations/india/delhi', 'https://health.economictimes.indiatimes.com/news/hospitals', 'https://www.who.int/hospitals/en/']


	for URL in urllist[i]:
		cnt +=1 
		browser.get(URL)
		time.sleep(randint(7,10))
		content = browser.page_source
		soup = BeautifulSoup(content,"html.parser")
		newlist=[]
		randomnumber=randint(1,10)
		if randomnumber>4:
			time.sleep(randomnumber)
			browser.execute_script("window.scrollTo(0,500)")
			time.sleep(10-randomnumber)
			browser.execute_script("window.scrollTo(0,-269)")
		#for a in soup.findAll('a',href=True, attrs={'class':'g'}):
		links= soup.findAll("div",{"class":"r"})
		#print(links)
		for link in links:
			temp=str(link)[23:]
			try:
				ind=temp.index('onmouse')
				print(temp[1:ind-2])
				csv_writer.writerow([temp[1:ind-2]])
				newlist.append(temp[1:ind-2])
			except:
				continue
		print(newlist)
		x,y=functionlist(cntrlgrplist,newlist)
		print(x,y)
		numbers.append([x,y])
		df = pd.DataFrame({'Search Result': newlist})
		csv_writer.writerow(' ')
		if cnt == 10:
			time.sleep(randint(400,600))
			cnt = 0
		browser.delete_all_cookies()
		time.sleep(randint(60,80))
	print(numbers)
	numberslist.append([numbers])
	time.sleep(randint(200,250))
print(numberslist)
df.to_csv('tier3CA.csv', encoding='utf-8')
browser.quit()
