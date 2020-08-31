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
	xv) splitchr() - used to split all the characters in the given string
	xvi) swapchar() - used to swap two characters in the given string
	xvii) char_rotate() - used to rotate a particular character in the given string
	xviii) int_str()  - used to convert the given int value to str"""

__all__=['wordcount','add_linepref','chrrem','strrep','cwlcount','slicesub','ismem','ispalindrome','vowcons','abece','vowrem','pyramid', 'iscapitalised', 'istitled', 'splitchr','swapchar','char_rotate','int_str']

# word count() - to count the occurrence of each word in the given string
# parameters - one(a string)
# output - a dictionary with words as keys and its occurrence as their values
def wordcount(a1):
        if isinstance(a1,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                d,f=a1.split(),{}
                e=set(d)
                for j in e:
                        f[j]=d.count(j)
                return f
        
# add_linepref() - to add a prefix to each sentence of the given string-
# inputs - two(strings - a string and a prefix)
# output - a list containing prefix added sentences as its elements
def add_linepref(a,b):
        if (isinstance(a,str) and isinstance(b,str))==False:
                raise TypeError("invalid arguments for type 'str'")
        else:
                d,e=a.split('.'),[]
                for i in d:
                        e.append(b+i)
                return e

# chrrem() - to remove the mentioned character in the given string
# inputs - two (strings - a string and a character to be removed)
# output - a string from the main string with the mentioned character removed
def chrrem(a,b):
        if (isinstance(a,str) and isinstance(b,str))==False:
                raise TypeError("invalid arguments for type 'str'")
        else:
                c=a.replace(b,'')
                return c

# strrep() - to replace the occurrence of a string in the given string with a new string
# inputs - three strings(a string, string to be replaced, string to be replaced with)
# output - a string with the string to be replaced with the string to be replaced with
def strrep(a,b,c):
        if (isinstance(a,str) and isinstance(b,str)) and isinstance(c,str)==False:
                raise TypeError("invalid arguments for type 'str'")
        else:
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
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
def slicesub(a,reverse=False):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                if reverse ==False:
                        for i in range(0,len(a)):
                                print (a[:i+1])
                        return ''
                elif reverse==True:
                        for i in range(len(a),0,-1):
                                print(a[:i])
                        return ''
                
#  ismem() - returns whether the second string is found in the first string or not
# inputs - two strings
# output - True / False. True is second parameter is in the first parameter. False otherwise
def ismem(a,b):
        if (isinstance(a,str) and isinstance(b,str))==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                if b in a:
                        return True
                else:
                        return False

# ispalindrome() - returns whether the given string is a palindrome or not
# input - a string
# output - True / False. True if the given string is a palindrome. False otherwise
def ispalindrome(a):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                a = a.lower()
                if a==a[::-1]:
                        return True
                else:
                        return False

# vowcons() - returns the number of vowels and consonants in the given string
# input - a string
# output - a dictionary with 'vowels' and 'consonants' as keys and their count as their values
def vowcons(a):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                b,c="ABCDEFGHIJKLMNOPQRSTUVWXYZ",''
                for i in b:
                       c+=i+a+'  '
                return c

# vowrem() - returns a string from the given string with all the vowels removed
# input - a string
# output - a string from the main string with all the vowels removed
def vowrem(a):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
        if isinstance(s,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
#       1) space - False 
#	i) align = 'left' - align the pattern without space to the left
#	i) align = 'right' - align the pattern without space to the right
#	i) align = 'center' - align the pattern without space to the center
#       1) space - True
#	i) align = 'left' - align the pattern with space to the left
#	i) align = 'right' - align the pattern with space to the right
#	i) align = 'center' - align the pattern with space to the center
def pyramid(a,b,space=False,align='left'):
        if ((isinstance(a,str) and isinstance(b,str)) and (isinstance(space,bool) and isinstance(align,str)))==False:
                raise TypeError("invalid arguments for type 'str','str','bool' and 'str'")
        else:
                if space==False:
                        if align=='left':
                                for i in range(1,a+1):
                                        print(i*b)
                        elif align=='right':
                                for i in range(1,a+1):
                                        c=i*b
                                        print(c.rjust(a+1,' '))
                        elif align=='center':
                                a1=2*a
                                for i in range(1,a1,2):
                                        c=i*b
                                        print(c.center(a1,' '))
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
                                b=b+' '
                                for i in range(1,a1,2):
                                        d=(b*i)
                                        c=2*a1
                                        print(d.center(c,' '))
                return ''
    
# iscapitalised() - used to check whether the given string is in capitalised form or not
# input - a string
# output - True / False. True if the first character of each line in the given string is in uppercase and rest are in lowercase. False otherwise				
def iscapitalised(a):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
def istitled(a):
        if isinstance(a,str)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
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
        if (isinstance(a,str) and isinstance(b,bool))==False:
                raise TypeError("invalid arguments for type 'str' and 'bool'")
        else:
                d=list()
                for i in a:
                        d.append(i)
                if duplicate==False:
                        return d
                if duplicate==True:
                        e=list(set(d))
                        return e

# switch() - used two characters in the given string
# inputs - 3 strings (a main string, character1, character2)
# output - a string with the character1 switched with character2 and vice versa
def swapchar(a,b,c):
        if ((isinstance(a,str) and isinstance(b,str)) and isinstance(c,str))==False:
                raise TypeError("invalid arguments for type 'str'")
        else:
                d=''
                for i,j in enumerate(a):
                        if j==b:
                                d=d+c
                        elif j==c:
                                d=d+b
                        else:
                                d=d+j
                return d

# str_rotate() - used to rotate a particular character in the given string
# inputs - 2(a string and a character(may be a string)
# output - list with the given character/string rotated over the given string
def char_rotate(a,b):
        if (isinstance(a,str) and isinstance(b,str))==False:
                raise TypeError("invalid arguments for type 'str'")
        else:
                c=a.replace(b,'')+' '
                d=[]
                for j,i in enumerate(c):
                        e,f=c[:j],c[j:]
                        g=e+b+f
                        d.append(g)
                return d

# int_str() - used to convert the given int value to str
# input - an integer
# output - returns the given integer as string i.e 1 as '1'
def int_str(a):
        if isinstance(a,int)==False:
                raise TypeError("invalid argument for type 'str'")
        else:
                b=''
                while a:
                        r=a%10
                        b=b+chr(48+r)
                        a//=10
                b=b[::-1]
                return b

