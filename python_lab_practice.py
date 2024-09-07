# list= [2,3,4,5,4]
# print(list)
# print(id(list))

# list.append("wdvu")
# print(list[1])
# print(id(list[1]))



# #Set
# set1 = {1,2,34,5,5,5}
# set2 = {23.4,54,323.23,453}
# print(set2.issubset(set1)) 
# print(set2.union(set1))
# print(set2.intersection(set1)) 
# print(set2.issuperset(set1))
# print(set2.isdisjoint(set1)) 
#------------------------------------------------------------------------------
new_list= ["wed","owed","dssa","opsa"]
new_set= set(new_list)
#------------------------------------------------------------------------------
# .sort() sorts the list but returns nothing,
#  but doesn't work on set,
#  since set is unordered
# new_list.sort()
# print(new_list)
#------------------------------------------------------------------------------
# sorted() creates a new list and sorts the list passed as argument,
# but doesn't sort the exsisting one
print(sorted(new_list))
print(new_list)
