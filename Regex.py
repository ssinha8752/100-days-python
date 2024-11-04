import re
print(re)

#pattern to find a digit with with 4 occurance
s=r"\d{3}"
pattern=re.compile(s) #changes the raw string to pattern
str="The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."
result=re.findall(pattern,str) #find the pattern in the string
print(result)

pattern1=r'\d{3}'
result1=re.search(pattern1,str)
print(result1) #first match of the string for the occurance of the pattern -> <re.Match object; span=(15, 18), match='600'>

pattern2=r"\w{3}" #finds a 3 alphanumeric word
result2=re.match(pattern2,str)
print(result2) #will check if the pattern in present in the begining of the string or else will return None

pattern3=r".{285}" #finds anything with 285 characters
result3=re.fullmatch(pattern3,str)
print(result3) #true if whole of the string matches with the pattern else None

result4=re.split(r"\s",str) #\s matches with \t \r \n
print(result4)

result5=re.sub(r"[A-Z]{2,}","INDEX", str,2)
print(result5)


result6=re.subn(r"[A-Z]{2,}","INDEX", str,2)
print(result6)

result6=re.search(r".+\s(.+ex).+.(\d\d\s.+).",str)
print(result6)
print(result6.groups())
print(result6.group(0))
print(result6.group(1))
print(result6.group(2))


print(result6.start(1))
print(result6.start(2))

print(result6.end(1))
print(result6.end(2))

result7=re.findall(r"the",str)
print(result7)

result8=re.findall(r"the",str,re.I)
print(result8)

str1="Hello\nPython"
result9=re.search(r".+",str1, re.S)
print(result9)

result10=re.search(r".+\s(.+ex).+.(\d\d\s.+).",str,re.X)
print(result10.groups())

