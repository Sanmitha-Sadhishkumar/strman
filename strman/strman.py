"""This module gives access to the functions : 
	i) word count() - to count the occurrence of each word in the given string
	ii) addpref() - to add a prefix to each sentence of the given string
	iii) chrrem() - to remove the mentioned character in the given string
	iv) strrep() - to replace the occurrence of a string in the given string with a new string
	v) cwlcount() - to count the occurrence of each character, word and line in the given string
	vi) slicesub() - gives the step by step slice of the given string
	vii) ismem() - returns whether the second string is found in the first string or not
	viii) ispalindrome() - returns whether the given string is a palindrome or not
	ix) vowcons() - returns the number of vowels and consonants in the given string
	x) abece() - returns an abecedarian series
	xi) vowrem() - returns a string from the given string with all the vowels removed
	xii) chrcount() - returns the occurrence of the given character in the given string
	xiii) pyramid() - returns a pattern of specified condition
	xvii) iscapitalised() - used to check whether the given string is in capitalised form or not
	xiv) istitled() - checks whether the given string is in titled form
	xv) splitchr() - used to split all the characters in the given string"""
	    
    # word count() - to count the occurrence of each word in the given string
    # parameters - one(a string)
    # output - a dictionary with words as keys and its occurrence as their values
class strmanip:
    def wordcount(self, a1):
            d,f=a1.split(),{}
            e=set(d)
            for j in e:
                    f[j]=d.count(j)
            return f
            
    # addpref() - to add a prefix to each sentence of the given string
    # inputs - two(strings - a string and a prefix)
    # output - a list containing prefix added sentences as its elements
    def addpref(self, a,b):
            d,e=a.split('.'),[]
            for i in d:
                    e.append(b+i)
            return e

    # chrrem() - to remove the mentioned character in the given string
    # inputs - two (strings - a string and a character to be removed)
    # output - a string from the main string with the mentioned character removed
    def chrrem(self, a,b):
            c=a.replace(b,'')
            return c

    # strrep() - to replace the occurrence of a string in the given string with a new string
    # inputs - three strings(a string, string to be replaced, string to be replaced with)
    # output - a string with the string to be replaced with the string to be replaced with
    def strrep(self, a,b,c):
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
    def cwlcount(self, a):
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
    def slicesub(self, a):
            for i in range(0,len(a)):
                    print (a[:i+1])
                    
    #  ismem() - returns whether the second string is found in the first string or not
    # inputs - two strings
    # output - True / False. True is second parameter is in the first parameter. False otherwise
    def ismem(self, a,b):
            if b in a:
                    return True
            else:
                    return False

    # ispalindrome() - returns whether the given string is a palindrome or not
    # input - a string
    # output - True / False. True if the given string is a palindrome. False otherwise
    def ispalindrome(self, a):
        a = a.lower()
        if a==a[::-1]:
            return True
        else:
            return False

    # vowcons() - returns the number of vowels and consonants in the given string
    # input - a string
    # output - a dictionary with 'vowels' and 'consonants' as keys and their count as their values
    def vowcons(self, a):
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
    def abece(self, a):
            b,c="ABCDEFGHIJKLMNOPQRSTUVWXYZ",''
            for i in b:
                   c+=i+a+'\t'
            return c

    # vowrem() - returns a string from the given string with all the vowels removed
    # input - a string
    # output - a string from the main string with all the vowels removed
    def vowrem(self, a):
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
    def chrcount(self, s):
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
    def pyramid(self, a,b,space=False,align='left'):
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
    def iscapitalised(self, a):
        b,c=a.split('.'),0
        for i in b:
            if i[0].isupper() and i[1:].islower():
                c+=1
        if c==len(b):
            return True
        else:
            return False


    #istitled() - checks whether the given string is in titled form
    # input - a string
    # output - True / False. True if the first character of each word is in uppercase and the rest are in lowercase. False otherwise
    def istitled(self, a):
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
    def splitchr(self, a,duplicate=False):
        d=list()
        for i in a:
            d.append(i)
        if duplicate==False:
            return d
        if duplicate==True:
            e=list(set(d))
            return e
strman = strmanip()
