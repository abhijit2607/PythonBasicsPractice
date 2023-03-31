word_list=eval(input('Enter the list of words:'))
max=''
for i in word_list:
    if len(i)>len(max):
        max=i
print('The longest word is:',max)
