#fobject=open('important.txt','w')
#fobject.write('go go go stop')
#fobject.close()

fobject=open('important.txt','r')
print(fobject.read(5))
print(fobject.read())
fobject.close()
