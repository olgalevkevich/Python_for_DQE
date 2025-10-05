import random
import string

"""
1. create a list of random number of dicts (from 2 to 10)

dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

"""

# Generate the number of dictionaries in the list using randint() function from random module
dict_number = random.randint (2,10)
print(f'The number of dictionaries in the list: {dict_number}')

# declare list of dictionaries
dict_list = []
for i in range(dict_number): # loop for craating dictinary elements in list with list length = generated dict_number
    key_number = random.randint (1,5) # Generate the number of elements  in each dictionary in the list
    keys = random.sample(string.ascii_lowercase, key_number) # generate list of dictonary keys: list length = key_number, elements come from random string of lowercase letters
    dict_list.append({key: random.randint(0,100) for key in keys}) # add dictionary elements in the list: for each key in previously created keys list add radom value from 0 to 100

print(f'list of random number of dicts (from 2 to 10): {dict_list}')

"""
2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

"""
common_dict = {} # final common dictionary
common_list = [] # a list consisting of lists, each of which contains the number of an element in the original list, a dictionary key, and a dictionary value: [[0, 'a', 5], [0, 'b', 7]....]
initial_keys = [] # list for keys in dictionaries

# Create common_list list consisting of lists, each of which contains the number of an element in the original list, a dictionary key, and a dictionary value: [[0, 'a', 5], [0, 'b', 7]....]
for i in range(len(dict_list)):
    for key, value in dict_list[i].items():
        new_list = [i, key, value]
        common_list.append(new_list)

# Iterate through the elements of the created list, find identical keys, and if any subsequent elements have a value greater than the current one for the same key,
# then I write the key with the index and the key value to the corresponding lists. set the flag to 1.
for element in common_list:
    flag = 0
    new_key = []
    new_value = []
    for i in range(len(common_list)-1):
        if element[1] == common_list[i+1][1] and common_list[i+1][2] > element[2]: #
            new_key.append(common_list[i+1][1]+ '_' + str(common_list[i+1][0]+1))
            new_value.append(common_list[i+1][2])
            flag = 1
    if flag == 1: # If the flag is 1, then find the maximum value and the key for this maximum value
        dict_value = max(new_value)
        ind = new_value.index(max(new_value))
        dict_key = new_key[ind]
    else: # If the flag is 0 - that is, there are no identical keys --> then  take the value and key from the current element of the created common_list list
        dict_value = element[2]
        dict_key = element[1]
# Checking whether the original keys were written to the common dictionary.
    if element[1] not in initial_keys:
        common_dict[dict_key] = dict_value # if not - add element in common dictionary
        initial_keys.append(element[1]) # After adding an element to the dictionary, save the original keys for subsequent verification.
print(f'Created common dictionary: {common_dict}')



