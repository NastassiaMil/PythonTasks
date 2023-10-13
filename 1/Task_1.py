import random

# create objects for further work

random_list = []    # create empty list for random values
sorted_list = []    # create empty list for sorted values

sum_even = 0         # create object to store the values of the sum of even numbers
sum_odd = 0          # create object to store the values of the sum of odd numbers

count_even = 0       # create object to store count of even numbers into list
count_odd = 0        # create object to store count of odd numbers into list


for i in range(100):                              # start loop for creation 100 values into list ( till value <=1000 do )
    random_list.append(random.randint(0, 1000))    # add random int values from 0 to 1000 to the empty list

print('Random list is : %s' % (random_list))     # show updated random_list

while random_list:                                # while list is true (has any values in it) do loop (after each time list decrease)
    min_value = random_list[0]                    # assign the first value from the list like minimum
    for i in random_list:                         # for each element into list do loop
        if i < min_value:                         # if current element < then our minimum
            min_value = i                         # replace our minimum with current element

    sorted_list.append(min_value)                 # add to the empty list out minimum element from each iteration of the loop
    random_list.remove(min_value)                 # delete from random_list our updated minimum element


for i in sorted_list:                             # for each element from sorted list do
    if i % 2 == 0:                                # if the remainder of dividing an element by 2 is 0 (then even)
        sum_even = sum_even + i                   # update sum_even as sum_even + this element
        count_even = count_even + 1               # update count_even as count_even + 1
    elif i % 2 != 0:                              # if the remainder of dividing an element by 2 is NOT 0 (then odd)
        sum_odd = sum_odd + i                     # update sum_odd as sum_odd + this element
        count_odd = count_odd + 1                 # update count_odd as count_odd + 1

avg_even = sum_even / count_even                  # create object for average for even numbers from sorted list like sum_even/count_even
avg_odd = sum_odd / count_odd                     # create object for average for odd numbers from sorted list like sum_odd/count_odd

print('Sorted list is : %s' % (sorted_list))
print('Average for even numbers is : %s' % (avg_even))
print('Average for odd numbers is : %s' % (avg_odd))




