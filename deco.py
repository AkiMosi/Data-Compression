
j=0
inti=0
mid=''
final=''
f = open('bin.txt','r+')
q=open('dec.txt','w')
a=f.readline()
b=[]
for i in range(0,len(a)):
    mid=a[(i*7):(i*7)+7]
    i=i+7
#for i in a:
#    c=int(ord(i))
#    b.append(bin(c))
#for i in range(0, len(a)):
#    m=str(b[0])
#    m=m[2:]
#    final=final+m
#q.writelines(final)
#f.close()
#q.close()