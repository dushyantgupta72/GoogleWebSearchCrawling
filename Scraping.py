#logged out search

from __future__ import division
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
from random import randint
# from urllib.request import urlopen as uReq
import time
from random import randint
from selenium.webdriver.common.keys import Keys
import itertools

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False) 
profile.set_preference("browser.privatebrowsing.autostart", True)               #incognito mode
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
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
        for i in range(m + 1): 
            for j in range(n + 1): 
                if i == 0: 
                    dp[i][j] = j   
                elif j == 0: 
                    dp[i][j] = i   
                elif str1[i-1] == str2[j-1]: 
                    dp[i][j] = dp[i-1][j-1]  
                else: 
                    dp[i][j] = min(1 + dp[i][j-1],        # Insert 
                                   1 + dp[i-1][j],        # Remove 
                                    2 + dp[i-1][j-1])    # Replace 
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



urllist = urllist = [['https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIFRGVsaGk', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGbXVtYmFp', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHa29sa2F0YQ', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJYmFuZ2Fsb3Jl', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHY2hlbm5haQ', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJaHlkZXJhYmFk', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIEcHVuZQ', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGSmFpcHVy', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJQWhtZWRhYmFk', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIKQ2hhbmRpZ2FyaA', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHTHVja25vdw', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGSW5kb3Jl', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIFS29jaGk', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIU3JpbmFnYXI', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4', 'https://www.google.co.in/search?q=Trekking+Places+in+India&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIVmFyYW5hc2k'], ['https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIFRGVsaGk', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGbXVtYmFp', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHa29sa2F0YQ', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJYmFuZ2Fsb3Jl', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHY2hlbm5haQ', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJaHlkZXJhYmFk', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIEcHVuZQ', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGSmFpcHVy', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIJQWhtZWRhYmFk', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIKQ2hhbmRpZ2FyaA', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIHTHVja25vdw', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGSW5kb3Jl', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIFS29jaGk', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIGTmFncHVy', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIU3JpbmFnYXI', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIRGVocmFkdW4', 'https://www.google.co.in/search?q=Affordable+Holiday+Destinations+in+India &gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICIIVmFyYW5hc2k']]


# cities = ['Delhi','Mumbai','Kolkata','Bangalore','Chennai','Hyderabad','Pune']

# cities = ['Jaipur','Ahmedabad','Chandigarh','Lucknow',Indore','Kochi']





for i in range(len(urllist)):
    # sasta=list(urllist[i][0])
    # sasta=sasta[:-16]
    # sasta.append('CAIQICIFRGVsaGk')                                 #for control city - Delhi
    # listToStr = ''.join([str(elem) for elem in sasta])
    # browser.get(listToStr)
    delhilink = urllist[i][0]
    browser.get(delhilink)
    content = browser.page_source
    soup = BeautifulSoup(content,"lxml")
    newlist=[]
    search_div = soup.find_all(class_='rc')                         # find all divs tha contains search result
    l = len(search_div)
    print("Total links : ")
    print(l)
    for x in range(min(7 , l)):                                     # taking only top 7 links from result list
        result = search_div[x] 
        print('%s'%result.a.get('href'))                            #geting a.href 
        newlist.append(result.a.get('href'))

    randomnumber=randint(1,10)                                      #to prevent block
    if randomnumber>4:                                              
        time.sleep(randomnumber)
        browser.execute_script("window.scrollTo(0,500)")    
        time.sleep(10-randomnumber)
        browser.execute_script("window.scrollTo(0,-269)")

    cntrlgrplist = newlist

    # repeated above steps for city to be compared

    numbers=[]
    for URL in urllist[i]:
        if URL == delhilink:
            continue
        print("before next query..waiting 11 minutes..")
        time.sleep(660)                                           #11 minute wait to remove carry-over effect
        browser.get(URL)
        time.sleep(randint(7,10))                                   #wait for content to load
        content = browser.page_source
        newlist=[]
        soup = BeautifulSoup(content,"lxml")
        search_div = soup.find_all(class_='rc')                     # find all divs tha contains search result
        l = len(search_div)
        for x in range(min(7 , l)):
            result = search_div[x]
            print('%s'%result.a.get('href'))                        #geting a.href 
            newlist.append(result.a.get('href'))

        randomnumber=randint(1,10)                                   #for preventing block
        if randomnumber>4:
            time.sleep(randomnumber)
            browser.execute_script("window.scrollTo(0,500)")
            time.sleep(10-randomnumber)
            browser.execute_script("window.scrollTo(0,-269)")
       
        x,y=functionlist(cntrlgrplist,newlist)                      #sending links for comparison
        # print(x,y)                                                #print jaccard index and edit distance for each url
        numbers.append([x,y])
        browser.delete_all_cookies()
    print(numbers)                                                  #print distances for each city wrt Delhi
browser.quit()
