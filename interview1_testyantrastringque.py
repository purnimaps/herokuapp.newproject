import re

sentence = 'hello123world567welcometo9724python'
# Write a program to fetch the below output
# output2 --> 123 + 576 + 9724

temp = re.findall(r"\d+",sentence)

print(sum([int(i) for i in temp]))
