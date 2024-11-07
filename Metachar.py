import re

str="The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result=re.findall(r"\d",str)
print(result)

result1=re.findall(r"\.",str)
print(result1)

result1=re.findall(r"[a-d]",str)
print(result1)

result1=re.findall(r"\b\w{4}\b",str)
print(result1)

result1=re.findall(r"\b\w{3,5}\b",str)
print(result1)

result1=re.search(r"\d{8}|\d{4}|\b[A-Z]{4}\b",str)
print(result1)

result1=re.findall(r"\A([A-Z].*?)\s",str, re.M)
print(result1)

result1=re.findall(r"\bEuro\b",str, re.M)
print(result1)

