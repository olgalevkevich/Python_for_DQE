# Save the original text to a string variable: input_text
input_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Make the text lowercase, split sting into sentence strings (separator: '.') and save it to a list: text_list
text_list = input_text.lower().split('.')

# Create a new list of sentence strings from the list, removing leading whitespaces (trailing whitespaces are not important since the previous list was obtained by dot-splitting)
# and capitalizing the letters in each sentence string using list comprehension
text_list_capitalize = [x.strip().capitalize() for x in text_list]

last_words =''
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
# Find the last words in each sentence, form a new sentence from them and save it into string last_words.
    if i == 0:
        last_words = text_list[i].split(' ')[-1].capitalize()
    elif i == len(text_list)-2:
        last_words = last_words + ' ' + text_list[i].split(' ')[-1] + '.'
    else: last_words = last_words + ' ' + text_list[i].split(' ')[-1]

# Join list items - sentences with capital letters into string text_norm_letter_cases
text_norm_letter_cases = '.'.join(text_list_capitalize)

# Split string text_norm_letter_cases into 2 parts at the place where it is needed to insert a sentence from the last words.
parts_list = text_norm_letter_cases.split('paragraph.')

# Form a new string:  new_text, with normalized letter case and an inserted sentence from the last words.
new_text = parts_list[0] + 'paragraph. ' + last_words.strip() +  parts_list[1]

# Replace 'iz' with 'is' where 'iz' is separate word
new_text_is = new_text.replace(' iz ', ' is ')

# Calculate number of whitespace in final text using sum, list comprehension, .isspace()
count_whitespace = sum([1 for element in new_text_is if element.isspace()])

# Print original text
print(f'Original text: \n {input_text}')

# Print final text
print(f'Final text: \n {new_text_is}')

# Print number of whitespaces
print(f'Number of whitespaces in final text: {count_whitespace}')