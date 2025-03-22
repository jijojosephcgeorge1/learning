#https://www.youtube.com/watch?v=YLI1YP8FHh8
# '''reverse a string using slice'''
# a='abcdefg'
# b = a[::-1]
# print(b)

# '''reverse a string using reveresed'''
# a='abcdefg'
# b=reversed(a)
# c=''.join(b)
# print(c)


# '''reverse a string using script'''
# a='Jijo'
# output=''
# i = len(a) -1
# while i >= 0:
#     output = output+a[i]
#     i = i-1
# print(output)

# '''reverse the words using slice'''
# a = 'Hello how are you'
# b = a.split()
# print(b)
# l=b[::-1]
# print(' '.join(l))

# '''reverse the words only word by word of a string'''
# s = "Hello how are you"
# l1=[]
# t=s.split()
# for i in t:
#     l1.append(i[::-1])
# print(' '.join(l1))

'''reverse content of every second word'''
s = "Hello how are you"
l1=[]
t=s.split()
j=0
for i in t:
    if j%2==0:
        l1.append(i[::-1])
        j+=1
    else:
        l1.append(i)
        j+=1
print(' '.join(l1))
