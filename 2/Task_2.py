import string
import random

# create objects for future work

list_of_dicts = []                                      # create object for list of dictionaries
common_dict = {}                                        # create dictionary for one dict common result
final_dict = {}                                         # create dictionary for final result

for i in range(random.randint(2,10)):                   # for each dictionary in random number of dictionaries ( from 2 to 10)
    keys = random.sample(string.ascii_lowercase,1)      # create random letters(with size 1 letter) for keys for dicts
    values = (random.randint(0,100) for i in range(3))  # create random numbers (from 0 to 1000) from values for dicts with size 3
    dicts = dict(zip(keys,values))                      # connect random keys with values into dict
    list_of_dicts.append(dicts)                         # add dicts to the list


for index, dict in enumerate(list_of_dicts):                              # loop for each index of dictionary and dictionary itself from list
    for key, value in dict.items():                                       # loop for ech key and value from each dictionary from list
        if key not in common_dict or value > common_dict[key]['value']:   # if current key is not exists into our common dictionary or value for with key > then value for the same key that have been already into common dict
            common_dict[key] = {'value': value, 'index': index}           # add new row into common_dict with key and value like dict (value for current dict, index for current dict)


for key, value in common_dict.items():                                                     # loop for each key, value into common_dict items
    rename = any(d.get(key) for i, d in enumerate(list_of_dicts) if i != value['index'])   # change key name if there is the same key into list_of_dicts (look at all dicts except dict equals to current (with the same index))
    new_key = f"{key}_{value['index']}" if rename else key                                 # if rename is true then rename key like key_index of this dictionary , if false use just key
    final_dict[new_key] = value['value']                                                   # new key added to the final result and it is assigned the value[value] from common_dict


print(list_of_dicts)
print(common_dict)
print(final_dict)


