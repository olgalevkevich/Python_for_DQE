import random
import string

"""
Module 2 Collections. Task 1.

Function that create a list of random number of dicts - the minimum and maximum values of the dictionaries are input variables for the function;

dict's random numbers of keys should be letter - the minimum and maximum values of the keys are input variables for the function.
dict's values should be a number - the minimum and maximum values of dict's values  are input variables for the function.
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

"""

def generate_random_dict_list (min_num_dict, max_num_dict, min_num_key, max_num_key, min_num_value, max_num_value) -> list:
    # Generate the number of dictionaries in the list using randint() function from random module
    dict_number = random.randint (min_num_dict, max_num_dict)
    # declare list of dictionaries
    dict_list = []
    for i in range(dict_number): # loop for craating dictinary elements in list with list length = generated dict_number
        key_number = random.randint (min_num_key,max_num_key) # Generate the number of elements  in each dictionary in the list
        keys = random.sample(string.ascii_lowercase, key_number) # generate list of dictonary keys: list length = key_number, elements come from random string of lowercase letters
        dict_list.append({key: random.randint(min_num_value,max_num_value) for key in keys}) # add dictionary elements in the list: for each key in previously created keys list add radom value

    return dict_list

# Call the function
created_dict_list = generate_random_dict_list(2, 10, 1,5, 0, 100)
print(f'Generated list of dictionaries: {created_dict_list}')

"""
Module 2 Collections. Task 2.
Function that get previously generated list of dicts as an input variable and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

"""
def create_common_dict (input_dict_list) -> dict:

    common_dict = {} # final common dictionary
    common_list = [] # a list consisting of lists, each of which contains the number of an element in the original list, a dictionary key, and a dictionary value: [[0, 'a', 5], [0, 'b', 7]....]
    initial_keys = [] # list for keys in dictionaries

    # Create common_list list consisting of lists, each of which contains the number of an element in the original list, a dictionary key, and a dictionary value: [[0, 'a', 5], [0, 'b', 7]....]
    for i in range(len(input_dict_list)):
        for key, value in input_dict_list[i].items():
            new_list = [i, key, value]
            common_list.append(new_list)

    # Iterate through the elements of the created list, find identical keys, and if any subsequent elements have a value greater than the current one for the same key,
    # then write the key with the index and the key value to the corresponding lists. set the flag to 1.
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
    return common_dict

# Call the function
created_common_dict = create_common_dict(created_dict_list)
print(f'Created common dictionary: {created_common_dict}')

"""
Module 3 String Object
"""
# Original text
original_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

"""
Module 3 
1. Function that normalizes text (input variable) from letter cases point of view
"""

def normalize_letter_cases (input_text) -> str:
    # Make the text lowercase, split sting into sentence strings (separator: '.') and save it to a list: text_list
    text_list = input_text.lower().split('.')

    # Create a new list of sentence strings from the list, removing leading whitespaces (trailing whitespaces are not important since the previous list was obtained by dot-splitting)
    # and capitalizing the letters in each sentence string using list comprehension
    text_list_capitalize = [x.strip().capitalize() for x in text_list]

    # loop through two lists of sentences: text_list has leading whitespaces, text_list_capitalize has no leading whitespaces spaces and hase capital letters.
    # I check which whitespaces is in that particular sentence and add that in the sentence string without a whitespaces in text_list_capitalize.
    for i in range(len(text_list)):
        if text_list[i].startswith(' \n\n\t'):
            text_list_capitalize[i] = ' \n\n\t' + text_list_capitalize[i]
        elif text_list[i].startswith('\n\n\t'):
            text_list_capitalize[i] = '\n\n\t' + text_list_capitalize[i]
        elif text_list[i].startswith('\n'):
            text_list_capitalize[i] = '\n' + text_list_capitalize[i]
        elif text_list[i].startswith(' '):
            text_list_capitalize[i] = ' ' + text_list_capitalize[i]

    # Join list items - sentences with capital letters into string text_norm_letter_cases
    text_norm_letter_cases = '.'.join(text_list_capitalize)
    return text_norm_letter_cases

# Call the function
text_normalized = normalize_letter_cases(original_text)
print(f'Normalized text from letter cases point of view: \n{text_normalized}')

"""
Module 3 
2. Function that find the last words in each sentence of given text, form a new sentence, insert the sentence to the end of given place
"""
insert_after_part = 'paragraph.'

def new_sentence_insert (given_text, after_part) -> str:
    last_words = ''
    # split given_text into sentence strings (separator: '.') and save it to a list: text_list_str
    text_list_str = given_text.split('.')
    for i in range(len(text_list_str)):
        # Find the last words in each sentence, form a new sentence from them and save it into string last_words.
        if i == 0:
            last_words = text_list_str[i].split(' ')[-1].capitalize()
        elif i == len(text_list_str) - 2:
            last_words = last_words + ' ' + text_list_str[i].split(' ')[-1] + '.'
        else:
            last_words = last_words + ' ' + text_list_str[i].split(' ')[-1]
    # Split string given_text into 2 parts at the place where it is needed to insert a sentence from the last words.
    parts_list = given_text.split(after_part)

    # Form a new string:  new_text with inserted sentence from the last words.
    new_text = parts_list[0] + after_part + ' ' + last_words.strip() + parts_list[1]
    return new_text

# Call the function
text_new_sentence = new_sentence_insert(text_normalized, insert_after_part)
print(f'Normalized text from letter cases point of view and with new sentence from last words: \n{text_new_sentence}')

"""
Module 3 
3. Function that replace words in a given text. In our case 'iz' with 'is' where 'iz' is separate word
"""
to_replace = 'iz'
to_insert = 'is'

def replace_words (provided_text, replacement_word, inserted_word) -> str:
    # Replace words
    replacement_word = ' ' + replacement_word + ' '
    inserted_word = ' ' + inserted_word + ' '
    new_text_replace = provided_text.replace(replacement_word, inserted_word)
    return new_text_replace

# Call the function
text_new_replace_words = replace_words(text_new_sentence, to_replace, to_insert)
print(f'Normalized text from letter cases point of view with, new sentence from last words and replaced iz with is: \n{text_new_replace_words}')


"""
Module 3 
4. Function that calculate number of whitespace in  text
"""

def calculate_whitespaces (final_text) -> int:
    count_whitespace = sum([1 for element in final_text if element.isspace()])
    return count_whitespace

# Call the function
number_whitespaces = calculate_whitespaces(text_new_replace_words)
print(f'Number of whitespaces in the text: {number_whitespaces}')