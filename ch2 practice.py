def addDict(dict1,dict2):
    union=dict1.copy()
    union.update(dict2)
    return union

#__main__

dict1 = {'apple': 2, 'banana': 3, 'orange': 4, 'kiwi': 1}
dict2 = {'banana': 1, 'orange': 3, 'grape': 5, 'mango': 2}
addDict(dict1,dict2)