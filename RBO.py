import rbo
alphabet='abcdefghijklmnopqrstuvqxyz{|}~'
def ed(a,b):
        adict={k: alphabet[v] for v, k in enumerate(a)}
        astring=alphabet[:len(a)]
        bdict={}
        bstring=''
        for i in range(len(b)):
            if b[i] in bdict:
            	bdict[b[i]]=alphabet[len(a)+i+1]
            	bstring+=alphabet[len(a)+i+1]
            	continue
            if b[i] in adict:
                bdict[b[i]]=adict[b[i]]
                bstring+=adict[b[i]]
            if b[i] not in adict:
                bdict[b[i]]=alphabet[len(a)+i+1]
                bstring+=alphabet[len(a)+i+1]
        return ([char for char in astring],[chara for chara in bstring])

#S = [1, 2, 3]; T = [1,2,2]
#S1,T1=ed(S,T)
#temp=rbo.RankingSimilarity(S1, T1).rbo()
#rint(temp)
delhilink=[]
c3=7
while c3!=0:
		s=input()
		if s[0]=='h':
			delhilink.append(s)
			c3-=1
#print(delhilink)
c1=7
rboo=[]
while c1!=0:
	link=[]
	c2=7
	while c2!=0:
		s=input()
		if s[0]=='h':
			link.append(s)
			c2-=1
	s1,s2=ed(delhilink,link)
	tempppp=rbo.RankingSimilarity(s1, s2).rbo()
	rboo.append(tempppp)
	print(tempppp)
	c1-=1
print(rboo)