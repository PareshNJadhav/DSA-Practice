def find_common_elements(list1,list2):
    common=[]
    mydict = {}
    for i in list1:
        mydict[i] = True
    for j in list2:
        if j in mydict:
            common.append(j)
    return common

list1 = [1,2,5]
list2 = [2,3,5]

print(find_common_elements(list1,list2))