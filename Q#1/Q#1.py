#!/usr/bin/env python
# coding: utf-8

# # Q: 1 Review Python language concept that we cover so far.  And implement in one python file.

# # Variables and Data Types 

# In[1]:


x=5+6


# In[2]:


x


# In[3]:


type(x)


# In[5]:


x="welcome"+"3"
x


# In[6]:


type(x)


# In[10]:


x="python"*3


# In[8]:


x


# In[11]:


type(x)


# In[12]:


x=3
y=4
Sum=x+y


# In[13]:


Sum


# In[14]:


type(Sum)


# In[15]:


x=2
y=9
m=print(x*y)


# In[16]:


type(m)


# In[17]:


x=[1,2,3,4,54]


# In[18]:


type(x)


# In[19]:


x={"a":5,"b":7}
x


# In[20]:


type(x)


# In[ ]:





# In[22]:





# # User Input

# In[1]:


x=int(input("Enter the number"))
y=int(input("Enyter the number"))
Sum=x+y
print(Sum)
type(Sum)


# In[4]:


x=int(input("Enter the number"))
y=int(input("Enyter the number"))
Div=x//y
x=print(Div)
type(x)


# # Functions

# In[5]:


x=int(input("Enter the number"))
y=int(input("Enyter the number"))
def add():
    return x+y
def Mult():
    return x*y
add()
Mult()


# In[24]:


def Data(fName,lName,Age):
    print("Name:",fName,"LastName:",lName,"Age:",Age)
Data("Ali","Ahmad",23)


# # If Statements

# In[25]:


num=[1,2,3,4]
alp=["a","b","c","d"]
if num==alp:
    print("equal")
else:
    print("np")


# In[28]:


num=[1,2,3,4]
alp=[1,2,3,4]
if num==alp:
    print("equal")
else:
    print("np")


# In[32]:


alp={"a":3,"b":4}
if "a" in alp:
    print("yes")
else:
    print("NO")


# In[33]:


age=20
res="pak"

if (age > 65 or age < 21) and res == "pak":
    print("Yes")


# In[36]:


age=22
res="paki"

if (age > 65 and age < 21) or res == "pak":
    print("Yes")
else:
    print("No")


# # while loop

# In[11]:


n=2
m=1
p=2
while m<=10:
    print(n, "X", m , "=",p)
    m+=1
    p+=2
print("Python")


# In[13]:


while True:
    line = input('> ')
    if line=='done':
        break
    print(line)
print('The End')


# In[14]:


while True:
    line = input(' >')
    if line[0] == "#":
        continue
    if line=="done":
        break
    print(line)
print("The End")
        


# In[16]:


while True:
    User_Name= input(' Enter the user name ')
    Password= input('Enter the password') 
    if User_Name != "usman" and Password != "bash4588":
        continue
    if User_Name == "usman" and Password == "bash4588":
        break
print("Welcome Usman ! ")
        


# # For loop

# In[21]:


count=0
for i in range(1,1000,4):
    count+=1
print("Number of digits =",count)


# In[ ]:


user1=int(input("Enter the number"))
user2=int(input("Enter the second number"))
user3 = int(input("Enter the third number"))

Ans = int((user1+user2+user3)//2)
x=int(Ans)-user2
print("YOU WON",x)


# In[1]:


Total=0
for i in range(1,15000):
    Total = Total+i
print("Sum of numbers =",Total)


# In[26]:


# Find maximun and minimum nunmber in list
largest = None
print("Before ",largest)
for i in [3,4,5,2,6,34,543,23]:
    if largest == None or i>largest:
         largest=i
print("largest",largest)


# In[31]:


# smallest Number in a list
smallest = None
print("Before ",smallest)
for i in [3,4,5,2,6,34,543,23]:
    if smallest == None or i<smallest:
         smallest=i
print("Smallest",smallest)


# # Data Structure

# # String

# In[32]:


fruit='banana'
letter = fruit[0:3]


# In[33]:


letter


# In[34]:


fruit = 'banana'
len(fruit)


# # strings are immutable

# In[36]:


fruit='banana'
fruit[0]="a"


# In[39]:


'a' in 'banana'


# In[40]:


'p' in 'banana'


# In[41]:


word = 'banana'
word.upper()


# In[42]:


word


# In[43]:


word = 'banana'
index = word.find('a')
print(index)


# In[44]:


line = '   where we go  '
line.strip()


# In[49]:


line = "   Have a nice day  "
line.strip()
print(line)
line.startswith('H')


# # Parsing Strings

# In[59]:


a="From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008"
b=a.find("@")
print(b)
c=a.find("Sat")
print(c)
a[31] 


# # Tuples

# In[60]:


a= "a","b","c"
type(a)


# In[61]:


a =("a")


# In[62]:


type(a)


# In[71]:


a=("efbywvgirhfoewnviwr")
c=sorted(a)
print(c)


# In[66]:


a


# In[72]:


x,y=2,3


# In[73]:


y


# In[74]:


x


# In[75]:


x,y = (92,3)


# In[76]:


y


# In[80]:


x={'chunk':2,'fred':5}
y=x.items()
y


# In[81]:


type(y)


# In[82]:


tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )


# In[83]:


data=[34,31,4,5,67]
data.sort(reverse=True)


# In[84]:


data


# In[89]:


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])


# # Dictionary

# In[1]:


engturd={}
print(engturd)


# In[2]:


type(engturd)


# In[3]:


engturd['one']='Aik'


# In[4]:


engturd


# In[6]:


'one' in engturd


# In[11]:


word = 'brontosaurus'
d=dict()
for c in word:
    print(c)
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print(d)


# In[12]:


d


# In[13]:


print(d.get('n',0))


# In[15]:


word = 'brontosaurus'
d=dict()
for c in word:
    d[c]=d.get(c,0)+1
    print(d)
print(d)


# In[26]:


file="brj3bgvuorbwguorwngipwmdfopwmfopwrnbguwedjonfj3rnv"
d=dict()
for line in file:
    word = line.split()
    for words in word:
        if words not in d:
            d[words]=1
    else:
        d[words]+=1
print(d)


# In[ ]:




