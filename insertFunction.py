lst=list(input('Enter a list:'))
endElement=lst[len(lst)-1]
lst.insert(0,endElement)
lst.pop(len(lst)-1)
print('The required list is:',lst)