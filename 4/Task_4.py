import string
import random
import re

def perform_list_transformations ( rand_dict_count_min, rand_dict_count_max, rand_number_min, rand_number_max ) :  # create fucntion with 4 inout parameters
    list_of_dicts = []                                                                                        # create object for list of dictionaries
    common_dict = {}                                                                                          # create dictionary for one dict common result
    final_dict = {}                                                                                           # create dictionary for final result

    for i in range(random.randint(rand_dict_count_min, rand_dict_count_max)):                  # for each dictionary in random number of dictionaries ( from rand_dict_count_min to rand_dict_count_max)
        keys = random.sample(string.ascii_lowercase,  1)                                       # create random letters(with size 1 letter) for keys for dicts
        values = (random.randint(rand_number_min, rand_number_max) for i in range(3))          # create random numbers (from rand_number_min to rand_number_max) from values for dicts with size 3
        dicts = dict(zip(keys, values))                                                        # connect random keys with values into dict
        list_of_dicts.append(dicts)                                                            # add dicts to the list

    for index, d in enumerate(list_of_dicts):                                 # loop for each index of dictionary and dictionary itself from list
        for key, value in d.items():                                          # loop for ech key and value from each dictionary from list
            if key not in common_dict or value > common_dict[key]['value']:   # if current key is not exists into our common dictionary or value for with key > then value for the same key that have been already into common dict
                common_dict[key] = {'value': value, 'index': index}           # add new row into common_dict with key and value like dict (value for current dict, index for current dict)

    for key, value in common_dict.items():                                                     # loop for each key, value into common_dict items
        rename = any(d.get(key) for i, d in enumerate(list_of_dicts) if i != value['index'])   # change key name if there is the same key into list_of_dicts (look at all dicts except dict equals to current (with the same index))
        new_key = f"{key}_{value['index']}" if rename else key                                 # if rename is true then rename key like key_index of this dictionary , if false use just key
        final_dict[new_key] = value['value']                                                   # new key added to the final result and it is assigned the value[value] from common_dict

    return list_of_dicts, common_dict, final_dict                                              # fuction return tuple with 3 variables


def perform_text_transformations (input_text):                                               # create fucntion with 1 inout parameter
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

    whitespace_count = input_text.count(' ') + input_text.count('\n')              # count all spaces and enters into original text

    return output_like_input, replace_all_iz, whitespace_count                     # fuction return tuple with 3 variables

def main_1():                                                                               # create our main function to get input parameters
    rand_dict_count_min = int(input("Введите минимальное количество словарей в листе: "))
    rand_dict_count_max = int(input("Введите максимальное количество словарей в листе: "))
    rand_number_min = int(input("Введите минимальное значение для словаря: "))
    rand_number_max = int(input("Введите максимальное значение для словаря: "))

    list_of_dicts, common_dict, final_dict = perform_list_transformations(rand_dict_count_min, rand_dict_count_max, rand_number_min, rand_number_max)   # save results from our perform_list_transformations function to the parameters

    # show the results
    print("Исходный лист со словарями: ", list_of_dicts)
    print("Лист с одним словарем: ", common_dict)
    print("Финальный лист: ", final_dict)

def main_2():                                                       # create our main function for perform_text_transformations function to get input parameter
    input_text = '''homEwork:
    tHis iz your homeWork, copy these Text to variable.



    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



    last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

    output_like_input, replace_all_iz, whitespace_count = perform_text_transformations(input_text)    # save results from our perform_text_transformations function to the parameters

    print('1) Text in sensitive case and sentence with the last words: \n\n' + output_like_input)
    print('2) Replace all wrong iz : \n\n' + replace_all_iz)
    print('3) Count all whitespaces : ' + str(whitespace_count))

main_1() # call main function for perform_list_transformations function
main_2() # call main function for perform_text_transformations function

