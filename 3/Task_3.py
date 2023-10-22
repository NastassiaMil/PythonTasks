import re

input_text = '''homEwork:
    tHis iz your homeWork, copy these Text to variable.



    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

sentences = re.split(r'(?<=[.!?:])\s+', input_text)                                      # divide string by sentences if we see one of the [.!?:] characters and after it '\s+' one or more spaces
capitalized_first_letter = '\n'.join([sentence.capitalize() for sentence in sentences])  # for each sentence into list do UPPER CASE for first letter in each of the sentences and add all sentences into one string with Enter delimiter

output_like_input = ""                                                                   # create empty string for new text with paragraphs like in original text

sentences = re.split(r'(?<=[.!?:])\s+', capitalized_first_letter)                       # divide new string with UPPER letters by sentences if we see one of the [.!?:] characters and after it '\s+' one or more spaces
last_words = [sentence.split()[-1] if sentence else "" for sentence in sentences]       # divide each sentence by words (space separator) and choose the last word from each sentence and if sentence is not empty else empty result
new_sentence = ' '.join(last_words)                                                     # create new sentence and add each last word from the previous query
corrected_sentence = re.sub(r'[.:]+(?!$)', '', new_sentence)                            # delete all '.' and ':' from sentence if it is not the last word (not the end of the row $)

capitalized_first_letter = capitalized_first_letter + '\n' + corrected_sentence         # add sentence at the end of all text

paragraphs = capitalized_first_letter.split('\n')
paragraphs_array = [paragraphs[:1], paragraphs[1:2], paragraphs[2:4] + paragraphs[9:], paragraphs[4:6], paragraphs[6:9]]  # create array with sub-arrays with elements from paragraphs like slices (first with the element[0], the second with [1] and for third [2],[3] and [9] etc)

for row in paragraphs_array:                                    # loop for each sub-array
    list_to_str = ' '.join(map(str, row))                       # add each element in string format to the string with space separator
    output_like_input = output_like_input + list_to_str + '\n'  # add each text row with slice elements to the string with enter between each row

replace_one_iz = re.sub(r'“iz”', '“YYY“', output_like_input)                   # replace the right "iz" to avoid replication in future
replace_all_iz = replace_one_iz.replace("iz", "is").replace("“YYY“","“iz“")    # replace others iz with is and then replace the right "iz" which is "YYY" now like "iz" from the original row

whitespace_count = input_text.count(' ') + input_text.count('\n')            # count all spaces and enters into original text

print('1) Text in sensitive case and sentence with the last words: \n\n' + output_like_input )
print('2) Replace all wrong iz : \n\n' + replace_all_iz )
print('3) Count all whitespaces : ' + str(whitespace_count))
