import random;

list_of_random_num = list();
for i in range(0, 10):
	list_of_random_num.append(random.randint(1,100));
print(list_of_random_num);

#highest number
highest_num = list_of_random_num[0];
for i in range(1, len(list_of_random_num)):
	if(highest_num<list_of_random_num[i]):
		highest_num = list_of_random_num[i];
print(highest_num);

#smallest number

smallest_num = list_of_random_num[0];
for i in range(1, len(list_of_random_num)):
	if(smallest_num > list_of_random_num[i]):
		smallest_num = list_of_random_num[i];
print(smallest_num);