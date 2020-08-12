def wordcount(a1):
        d,f=a1.split(),{}
        e=set(d)
        for j in e:
                f[j]=d.count(j)
        return f
def addpref(a,b):
        d,e=a.split('.'),[]
        for i in d:
                e.append(b+i)
        return e
def mirror(a):
        return a[::-1]
def chrrem(a,b):
        c=a.replace(b,'')
        return c
def strcat(a,b):
        return a+b
def swap(a,b):
        return b,a
def strrep(a,b,c):
        d,e=a.split(),""
        for i in d:
                if i==b:
                        e=e+' '+c
                else:
                        e=e+' '+i
        return e.lstrip()
def cwlcount(a):
        b,c,k=a.split('.'),"",[]
        c=a.replace('.','')
        d,e=list(c.split()),list()
        for i in c:
                e.append(i)
        b1,d1,e1=set(b),set(d),set(e)
        def fun(g,g1):
                h={}
                for i in g1:
                        h[i]=g.count(i)
                k.append(h)
        fun(e,e1)
        fun(d,d1)
        fun(b,b1)
        return k
def slicesub(a):
        for i in range(0,len(a)):
                print (a[:i+1])
def ismem(a,b):
        if b in a:
                return True
        else:
                return False
def ispalindrome(a):
        if a==a[::-1]:
                return True
        else:
                return False
def vowcons(a):
        b="aAeEiIoOuU"
        v,c=0,0
        for i in a:
                if i in b:
                        v+=1
                else:
                        c+=1
        d={'vowel':v,'consonant':c}
        return d
def abece(a):
        b,c="ABCDEFGHIJKLMNOPQRSTUVWXYZ",''
        for i in b:
               c+=i+a+'\t'
        return c
def vowrem(a):
        temp_str=''
        for i in a:
                if i in "aAeEiIoOuU":
                        pass
                else:
                        temp_str+=i
        return temp_str
def chrcount(s, c):
        c1=0
        for i in s:
                if i == c:
                        c1+=1
        return c1
