grocery_list = []
end_convo = ""

print("Hello welcome to market")
print(" Available fruits: \n Apple \n Banana \n Orange")

while end_convo == "" or end_convo == 'n':
	order = str(input("What do you want to buy? " )).lower()
	
	if order == 'apple':
		grocery_list.append('apple')
	elif order == 'banana':
		grocery_list.append('banana')
	elif order == 'orange':
		grocery_list.append('orange')
	else:
		print("Not an item")
		continue

	print(grocery_list)
	end_convo = str(input("Are you done shopping? (y/n) " )).lower()

print("Thank you for shopping")
print("Your final grocery list, \n", grocery_list)