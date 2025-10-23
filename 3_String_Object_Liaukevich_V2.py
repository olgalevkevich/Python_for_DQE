import re
# Save the original text to a string variable: input_text
input_text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# split sting into sentence strings (separators: .!?) and save it to a list: text_list
text_list = re.split(r'[.!?]', input_text)
# find all separators: .!?  in the string and save them to sentence_endings list
sentence_endings = re.findall(r'[.!?]', input_text)

# go through each sentence in the list. In each sentence, find the first non-whitespace character and normalize the letter case from there to the end of the sentence.
# Add whitespaces at the beginning and end-of-sentence characters at the end. Join sentences in one string text_norm_letter_cases
text_norm_letter_cases = ''
last_words =''
for k in range(len(text_list)):
    whitespace_str = ''
    for i in range(len(text_list[k])):
        if text_list[k][i].isspace():
            whitespace_str += text_list[k][i]
        else:
            text_norm_letter_cases += whitespace_str + text_list[k][i:].capitalize() + sentence_endings[k]
            break
# Find the last words in each sentence, form a new sentence from them and save it into string last_words.
    last_words += ' ' + text_list[k].split(' ')[-1]

# Split string text_norm_letter_cases into 2 parts at the place where it is needed to insert a sentence from the last words.
parts_list = text_norm_letter_cases.split('to the end of this paragraph.')

# Form a new string:  new_text, with normalized letter case and an inserted sentence from the last words.
new_text = parts_list[0] + 'to the end of this paragraph. ' + last_words.strip().capitalize() + '.' +  parts_list[1] + '\n'
#print (new_text)

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