
# ! ------> common funcions for  list

l1 = [6, 7, 8, 9, 0]
# print(len(l1))

print(max(l1))
# print(min(l1))

l1 = [6, 8, 9, "p", "u"]
print(max(l1)) # ---> eeror coz its a combination pf list and string
print(max(l1)) # ---> eeror coz its a combination pf list and string

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) # -5

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(l1.index(9))

l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of tims an element is repeated
# print(l1.count(6))

#! some function which is specifically used for list

# Toadd element inside list
# ? insert() --> to add elementa at specific index position
l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "cars")
 # print
 # ? to delete element from list
l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# pop() --> last element will be deleted
l1.pop()
print(l1)

pop(index_value) --> used to delete element at specific index
l1.pop(4) is index value
print(l1)

# remove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1)


#* clear() --> to complete delete all element in list
# l1.clear
# print(l1)

# del -> to delete the list
# del l1 # or del(l1)
# print(l1)

# ? ---> join 2 lists


l1 = [9, 0, 8]
l2 = ["p", "o", "t", 34]
print(l1+l2)

# ! or
# * extend() --> to combine 2 lists
# 11.ext(12)
# print(11)
# ? ------> copy()
11= [8,9,0,[5,6],[3,2,1]]
12  copy.copy(11)
print(11))
print(12))


#* deep copy --> used to copy the list with nested list
import copy
l1 = [8, 9, 0,[5, 6],[3, 2, 1]]
print(l1[-1][1]) --> to index nested list

l2 = copy.deepcopy(l1)
l1[-1].append(890)
print(l1)
print(l2)


# ? sort --> arrange elements in list in ascending or descending order
l1 = [9, 7, 45, 0, -6, 5, 12]
l1.sort() # to arrange in ascending order
print(l1)


l1.sort
(reverse=True) # to sort in  descending order
print(l1)


l1 = ['z', 'i', '0', 'p', 9]
.sort()
print(l1) # --> error

list constructor
list() --> to conver other collction datatype to list
l3 = ((8, 9, 0))
print(list(l3))

l4 = (8, 9)
print(list(l4))

# ! ---> nested list
l1 = [8, 9, [0, 8, 7,], ["p", "o", "y"], [8, "t"]]
# print9l1[-2][1]) # --> 0

print(l1[1:4])
print(l1[1:-1])

# ? to delete "t" from l1
(l1[-1].remove('t'))
print(l1)

[10:44 am, 15/03/2024] Savi Ksrm Friends: # ? combine these ["p", "o", 'y'], [8, 't'] lists in l1 to ["p", "o", 'y',8, 't']
[11:26 am, 15/03/2024] Savi Ksrm Friends: # ? combine these ["p", "o", 'y'], [8, 't'] lists in l1 to ["p", "o", 'y',8, 't']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! -----> tuple
# * char of tupple
'''
1.) tuple hav to b surrounded by
2.) the element inside tuple are not changable
3.) the elements inside tuple are changable
4.) the element will execute in order
5.)it is heterogenous
6.)it allow duplicate elements

#* eg:
t1 = (8, 8, 9, 6,5.78, [9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))

# ? indexing, slicing are all same as list

l1 = (8)
print(type(l1)) # int

1 = (8)
print(type(l1)) # int

l1 = (8)
print(type(l1)) # tuple

t1 = 8,9
print(type(t1)) # tuple

t2 = 8,
print(type(t2)) # tuple

len(), min(), max(), index(), count(), --> all  same as list

to ad lement inside tuole --> cannot add
cannot delete any element from tuple

# * join 2 tuples
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1+t2)

# * to add all element inside list and tuple
sum()
l1 = [8, 9, 7, 6]
print(sum(l1))

# * sort tuple
t1 = (8, 9, 0, 89, 12)
print(tuple(sorted(t1,reverse=True)))

# * Iterate list and tuples

# * Iterate based on elements
l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
    ''''
# * iterate based on index value
l1 = [9, 8, 0, 6, 5]
for i in range(0, 5):
    print(l1[i])


# * Iter based on index value
# 11 = [9,8,0,6,5,8,56]
# for i in range

# ---> common functions

# len(), min(), max(), index(), count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

ord()--> usd to find the ASCII value of a character
s1 = 'u'
print9ord(s1))

# ! functiion of string
s1 = "hello world"

#  ? o convert all charaters to upper case
print(s1.upper())

# ? to conver to lower case
s1 = "HFREDGiou"
print(s1.lower())

# > strip() ---> to elimanate the space in beginning and end of string``
s1 = " where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())
'''''
# split() --> to split the words in string based on a character
s1 = " where are you?"
print(s1.split())
print(s1.split("r"))



 * replace() --> to replace a spcific char in the string
s1 = "where are you?"
print(s1.replace('r', '&&'))


 * replace() --> to replace a spcific char in the string
s1 = "where are you?"
print(s1.replace('r', '&&'))

# swapcae() ---> tq convert capital to small and small to capital at a time
s1 = "HEY there"
print(s1.swapcase())

# * title() --> to write th string in format of itle
s1 = 'never giveUP'
print(s1.title())

# * capitalize() --> lst char of string will be converted to capital
s1 = 'nver giveUP'
print(s1.capitalize())

# * join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 = '''
how are you
i am fine
hey there
'''

# splines() --> used to split the string based on lines
print(s1.splitlines()0

# * find() --> to find split the index based on a character
s1 = "hello world"
print(s1.find('z'))
print(s1.index('z'))

# * joint() -->
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))
''''
      
s1 = "welcome to all"
print(s1.endswith('1'))
print(s1.sartswitch('w'))

s1 = "67"
print(tyoe(s1))
print(s1.insigit())

# *print the string in rever manner
# s1 = "welcome to all"
# print(s1[::-1])

# !--->Eg:1
# wap to find the number of lower case letters

.-> Eg:3
'em = "lorem Ipus is simply dummy text of the printing and typesetting  industrt.



# ! ------> Eg:3
'''''
s1 = "lorem ipsum is  simply dummy text of the printing and typesetting industry. lorem ipsum
characters = len(s1)
print(charaters)

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

words = s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))
















