# Python 3 code to demonstrate
# removing duplicated from list
# using naive methods

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
test_list = [38,39,65,25,25,50,51]

print ("The original list is : " + str(test_list))

# using naive method
# to remove duplicated
# from list
res = []
for i in test_list:
	if i not in res and i + 1 not in res and i - 1 not in res:
		res.append(i)

# printing list after removal
print ("The list after removing duplicates : " + str(res))
