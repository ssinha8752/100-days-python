Lecture 1 -

Data types :
bool
float
int
string

Typecast :
int(-1.99)=-1
int('dog',26_=17728

Using int('dog', 36) in Python is an attempt to convert the string 'dog' into an integer, using base 36. In base 36, digits include 0-9 and letters a-z. So, 'd' = 13, 'o' = 24, and 'g' = 16. Combined, 'dog' in base 36 translates to:

13×36^2+24×36^1+16×36^0=16760
So, int('dog', 36) evaluates to 16760.

bool(-1) = True
bool(0)=False
float(-inf)=-inf


String Encoding
ord('a')=97
ord('A')=65
chr(97)=a

Arithmetic Operators
+,=,+=,/,//(shows the quotient),%,5e3 => 5*10*10*10

Logical Operators
not, or, and

Assignment Operators
+=,%=,**=

Comparison Operators
<,<=,>,>=

String Operators
'a'+'b'='ab'
'-'*10='----------'
s='Shubham'
len(s) = 7
s[2] = u
s[2:5]=ubh

print('Program name: {} \nCourse name: {} \nCourse code: {}'.format('MITB', 'CT with Python', 'IS628'))


#reverse of a number
n=101
s=str(n)
rev_s=s[::-1]
rev_n=int(rev_s)
if n==rev_n:
    true
else:
    false