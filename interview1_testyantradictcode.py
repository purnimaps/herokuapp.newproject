from _collections import defaultdict

sentence = "hello world welcome to python programming hi there"
list1 = sentence.split()
d = defaultdict(list)
for item in (list1):
    s1 = item[0]
    d[s1].append(item)
print(*d.items())