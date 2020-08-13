"""This module gives access to the functions : 
	i) word count() - to count the occurrence of each word in the given string
	ii) addpref() - to add a prefix to each sentence of the given string
	iii) mirror() - to get the mirror of the given string
	iv) chrrem() - to remove the mentioned character in the given string
	v) strcat() - to concatenate two strings
	vi) swap() - to swap the given strings
	vii) strrep() - to replace the occurrence of a string in the given string with a new string
	viii) cwlcount() - to count the occurrence of each character, word and line in the given string
	ix) slicesub() - gives the step by step slice of the given string
	x) ismem() - returns whether the second string is found in the first string or not
	xi) ispalindrome() - returns whether the given string is a palindrome or not
	xii) vowcons() - returns the number of vowels and consonants in the given string
	xiii) abece() - returns an abecedarian series
	xiv) vowrem() - returns a string from the given string with all the vowels removed
	xv) chrcount() - returns the occurrence of the given character in the given string
	xvi) pyramid() - returns a pattern of specified condition
	xvii) iscapitalised() - used to check whether the given string is in capitalised form or not
	xviii) istitled() - checks whether the given string is in titled form
	xix) splitchr() - used to split all the characters in the given string
	xx) lalpha() - used to get the lowercase English alphabets
	xxi) ualpha() - used to get the uppercase English alphabets
	xxii) lalnum() - used to get the lowercase English alphabets with their number (1-26)
	xxiii) ualnum() - used to get the uppercase English alphabets with their number (1-26)"""

__all__=[wordcount, addpref, mirror, chrrem, strcat, swap, strrep, cwlcount, slicesub, ismem, ispalindrome, vowcons, vowrem, abece, chrcount, iscapitalised, istitled, splitchr, lalpha, ualpha, lalnum, ualnum]

	
# word count() - to count the occurrence of each word in the given string
# parameters - one(a string)
# output - a dictionary with words as keys and its occurrence as their values
def wordcount(a1):
        d,f=a1.split(),{}
        e=set(d)
        for j in e:
                f[j]=d.count(j)
        return f
        
# addpref() - to add a prefix to each sentence of the given string
# inputs - two(strings - a string and a prefix)
# output - a list containing prefix added sentences as its elements
def addpref(a,b):
        d,e=a.split('.'),[]
        for i in d:
                e.append(b+i)
        return e
# mirror() - to get the mirror of the given string
# input - one(string)
# output - reverse of the given string
def mirror(a):
        return a[::-1]

# chrrem() - to remove the mentioned character in the given string
# inputs - two (strings - a string and a character to be removed)
# output - a string from the main string with the mentioned character removed
def chrrem(a,b):
        c=a.replace(b,'')
        return c

# strcat() - to concatenate two strings
# inputs - two strings
# output - concatenated string formed from the give. strings
def strcat(a,b):
        return a+b

# swap() - to swap the given strings
# inputs - two strings
# output - swaped strings 
def swap(a,b):
        return b,a

# strrep() - to replace the occurrence of a string in the given string with a new string
# inputs - three strings(a string, string to be replaced, string to be replaced with)
# output - a string with the string to be replaced with the string to be replaced with
def strrep(a,b,c):
        d,e=a.split(),""
        for i in d:
                if i==b:
                        e=e+' '+c
                else:
                        e=e+' '+i
        return e.lstrip()

# cwlcount() - to count the occurrence of each character, word and line in the given string
# inputs - a string
# output - a list containing dictionaries that contain keys as character or word or a line and their occurrence as their values

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
        
# slicesub() - gives the step by step slice of the given string
# input - a string
# output - step by step slices
def slicesub(a):
        for i in range(0,len(a)):
                print (a[:i+1])
                
#  ismem() - returns whether the second string is found in the first string or not
# inputs - two strings
# output - True / False. True is second parameter is in the first parameter. False otherwise
def ismem(a,b):
        if b in a:
                return True
        else:
                return False

# ispalindrome() - returns whether the given string is a palindrome or not
# input - a string
# output - True / False. True if the given string is a palindrome. False otherwise
def ispalindrome(a):
	a = a.lower()
        if a==a[::-1]:
                return True
        else:
                return False

# vowcons() - returns the number of vowels and consonants in the given string
# input - a string
# output - a dictionary with 'vowels' and 'consonants' as keys and their count as their values
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

# abece() - returns an abecedarian series
# input - a string
# output - an abecedarian series with the given string
def abece(a):
        b,c="ABCDEFGHIJKLMNOPQRSTUVWXYZ",''
        for i in b:
               c+=i+a+'\t'
        return c

# vowrem() - returns a string from the given string with all the vowels removed
# input - a string
# output - a string from the main string with all the vowels removed
def vowrem(a):
        temp_str=''
        for i in a:
                if i in "aAeEiIoOuU":
                        pass
                else:
                        temp_str+=i
        return temp_str

# chrcount() - returns the occurrence of the each character in the given string
# inputs - a string 
# output - a dictionary containing each character as keys and their occurrence as their values
def chrcount(s):
        a=list()
        for i in s:
                a.append(i)
        b,c=set(a),dict()
        for i in b:
                c[i]=a.count(i)
        return c

# pattern - returns a pattern of specified condition
# inputs - four (an integer, a string, parameter space = True / False, parameter align = 'left' / 'right' / 'center')
# output - returns a pattern based on the given condition
#	1) space - False 
#		i) align = 'left' - align the pattern without space to the left
#		i) align = 'right' - align the pattern without space to the right
#		i) align = 'center' - align the pattern without space to the center
#	1) space - True
#		i) align = 'left' - align the pattern with space to the left
#		i) align = 'right' - align the pattern with space to the right
#		i) align = 'center' - align the pattern with space to the center
def pyramid(a,b,space=False,align='left'):
	if space==False:
		if align=='left':
			for i in range(1,a+1):
				print(i*b)
		elif align=='right':
			for i in range(1,a+1):
				b=i*'*'
				print(b.rjust(a,' '))
		elif align=='center':
			a1=2*a
			for i in range(1,a1,2):
				b=i*'*'
				print(b.center(a1,' '))
	elif space==True:
		if align=='left':
			b=b+' '
			for i in range(1,a+1):
				print(i*b)
		elif align=='right':
			b=b+' '
			for i in range(1,a+1):
				c,d=i*b,2*a
				print(c.rjust(d,' '))
		elif align=='center':
			a1=2*a
			for i in range(1,a1,2):
				b=i*"* "
				c=2*a1
				print(b.center(c,' '))

# iscapitalised() - used to check whether the given string is in capitalised form or not
# input - a string
# output - True / False. True if the first character of each line in the given string is in uppercase and rest are in lowercase. False otherwise				
def iscapitalised(a):
    if a[0].isupper() and a[1:].islower():
        return True
    else:
        return False


#istitled() - checks whether the given string is in titled form
# input - a string
# output - True / False. True if the first character of each word is in uppercase and the rest are in lowercase. False otherwise
def istitled(a):
    a1=a.replace('.','')
    b,c=a1.split(),0
    for i in b:
        if i[0].isupper() and i[1:].islower():
            c+=1
    if c==len(b):
        return True
    else:
        return False

# splitchr() - used to split all the characters in the given string
# inputs - a string and a parameter duplicate = True/False
# output - gives a list with all the characters in the given string
#	i) if duplicate==False, the duplicates are not removed
#	ii) if duplicate==True, duplicates are removed
def splitchr(a,duplicate=False):
    d=list()
    for i in a:
        d.append(i)
    if duplicate==False:
        return d
    if duplicate==True:
        e=list(set(d))
        return e

# lalpha() - used to get the lowercase English alphabets
# input - nil
# output - a list containing all the lowercase English alphabets as its elements
def lalpha():
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return a

# ualpha() - used to get the uppercase English alphabets
# input - nil
# output - a list containing all the uppercase English alphabets as its elements
def ualpha():
    a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return a

# lalnum() - used to get the lowercase English alphabets with their number (1-26)
# input - nil
# output - a dictionary containing all the lowercase English alphabets as its keys and their number as their values i.e a - 1, b - 2, etc
def lalnum():
    a={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    return a

# ualnum() - used to get the uppercase English alphabets with their number (1-26)
# input - nil
# output - a dictionary containing all the uppercase English alphabets as its keys and their number as their values i.e A - 1, B - 2, etc
def ualnum():
    a={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    return a
