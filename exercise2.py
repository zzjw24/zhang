str='X-DSPAM-Confidence: 0.8475'
sppos=str.find(' ')
print(sppos)
num=str[sppos+1:]
print(num)
print(type(num))
print(type(float(num)))
