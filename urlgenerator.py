city=['CAIQICIGSmFpcHVy','CAIQICIJQWhtZWRhYmFk','CAIQICIKQ2hhbmRpZ2FyaA','CAIQICIHTHVja25vdw','CAIQICIGSW5kb3Jl','CAIQICIFS29jaGk']
queries= ["Vikas+Dubey","Coronavirus+Vaccine","Assam+Floods","Kangana+Ranaut","Nepotism","Sachin+Pilot","Google+Jio+deal"]
url=[]
for query in queries:
	url_temp=[]
	for ct in city:
		s='https://www.google.co.in/search?q='+query+'&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+'+ct
		url_temp.append(s)
	url.append(url_temp)
print(url)		