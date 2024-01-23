import csv
import os.path
import string
from collections import Counter
import json
import xml.etree.ElementTree as ET

class FileAnalyzer:                  # create class

    def __init__(self, file_path):   # create function that initializes an instance of the class with a file_path attribute.
        self.file_path = file_path   # create object to store file_path

    def count_words(self):                                          # create function for counting words
        words_count = dict()                                        # create empty dict for future words and counts
        translator = str.maketrans('', '', string.punctuation)      # create object to store all text without any punctuation symbols
        try:                                                        # try exception block to check input file path
            with open(self.file_path) as f:                         # open file with file path location
                if os.stat(self.file_path).st_size == 0:            # if size in bytes of our file is 0
                    print('File is empty')                          # show this message
                else:                                               # if size in bytes of our file is not 0
                    news = f.read()                                 # create object to store all info from file (read file)
                    news = news.translate(translator).lower()       # recreate object text with all lower letters
                    words = news.split()                            # split our text to separate words in list (separator space)
                    for word in words:                              # open loop for each word into list
                        if word in words_count:                     # if current word in dict keys
                            words_count[word] += 1                  # add 1 to the value for this key
                        else:                                       # if current word is not in dict keys
                            words_count[word] = 1                   # do value = 1
        except FileNotFoundError:                                   # if we catch not found file error
            print(f"File not found: {self.file_path}")              # show this message
        return words_count                                          # output dic with words and counts

    def count_letters(self):                                                             # create function for counting letters
        try:                                                                             # try exception block to check input file path
            with open(self.file_path) as f:                                              # open file with file path location
                if os.stat(self.file_path).st_size == 0:                                 # if size in bytes of our file is 0
                    print('File is empty')                                               # show this message
                    result = []                                                          # create empty list
                else:                                                                    # if size in bytes of our file is not 0
                    news = f.read()                                                      # create object to store all info from file (read file)
                    normalized_text = news.lower()                                               # recreate object text with all lower letters
                    letter_counts = Counter(char for char in normalized_text if char.isalpha())  # count all letters if they are is alfa characters ( go in loop per each symbol ) output dict

                    result = [            # create list with dicts
                        {
                            'Letter': letter,                               # show letter
                            'Count_All': letter_counts[letter],             # show count upper and lower letter
                            'Count_Uppercase': news.count(letter.upper()),  # show count only upper letters
                            'Percentage': (letter_counts[letter] / len(normalized_text)) * 100 if len(normalized_text) != 0 else 0  # show percentage from total counts if length is not 0
                        }
                        for letter in letter_counts.keys()                  # for each letter from dict keys
                    ]

        except FileNotFoundError:                                   # if we catch not found file error
            print(f"File not found: {self.file_path}")              # show this message
        return result              # output list with dicts

    def write_to_files(self):                       # create function for saving results to the files
        word_count_result_list = []                 # create empty list for storing count of words
        count_words_result = self.count_words()     # create object to store result after the call count_words function
        count_letters_result = self.count_letters() # create object to store result after the call count_letters fuction

        if not count_words_result or not count_letters_result:                  # if output for functions is empty
            print("No data to write. You can try again with another path")      # show this message
            return                                                              # end function

        for key, value in count_words_result.items():               # start loop for each key and value from count_words output items
            word_count_result_list.append({key: value})             # add to the list result for each key value

        with open('csv1.csv', 'w', newline='') as csv_file:             # open file to write result for count_word fucntion output
            fieldnames = ['Word', 'Count']                              # create object to store columns name
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)    # create object to save dicts to the csv file with column names from previous object
            writer.writeheader()                                        # create first row with name of columns to the file
            for item in word_count_result_list:                             # for each element from list
                word, count = list(item.keys())[0], list(item.values())[0]  # assing to word and count values new value first key and value for current item
                writer.writerow({'Word': word, 'Count': count})             # create row with this key value

        with open('csv.csv', 'w', newline='', encoding='utf-8') as csvfile:     # open file to write result for count_letter fucntion output
            fieldnames = count_letters_result[0].keys()                         # create object to store names for columns like first element (dict) from the list
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)             # create object to save dicts to the csv file with column names from previous object
            writer.writeheader()                                                # create first row with name of columns to the file
            for row in count_letters_result:                                    # for each element from count_letter output
                writer.writerow(row)                                            # create row

        print('File successfully created and all information is saved')         # show this message

    def remove_source_file(self):                                       # create function for remove input file
        try:                                                            # try to check that file is exists
            if os.stat(self.file_path).st_size == 0:                    # if file is empty
                print('File removal was failed! File is empty!')        # show this message
            else:                                                       # if file is not empty
                with open(self.file_path, 'r') as f:
                    f.close()                                           # close the file
                os.remove(self.file_path)                               # delete this file
                print(f'Source file removed: {self.file_path}')         # show this message
        except FileNotFoundError:                                       # if there is no such file
            print(f'File not found: {self.file_path}')                  # show this message


# file_analyzer = FileAnalyzer(r'C:\Users\Nastassia_Svirydava\PycharmProjects\Task1\nn.txt')       # create object with class call
# file_analyzer.write_to_files()                                                                   # call write fo files function

class JsonFileWriter(FileAnalyzer):                         # create child class for work with JSON

    def __init__(self, file_path, json_file_path):          # create function that initializes an instance of the class with a file_path attribute from parent class and file to the json output file
        super().__init__(file_path)                         # call methods from parent class and initializing file_path
        self.json_file_path = json_file_path                # create object to store file_path for output json

    def write_to_files(self):                               # create function for save results to the json
        count_words_result = self.count_words()             # create object to store count_words output
        count_letters_result = self.count_letters()         # create object to store count_letter output

        if not count_words_result or not count_letters_result:                  # check that there are no any outputs
            print("No data to write. You can try again with another path")      # show this messages
            return                                                              # end function

        json_data = {                                       # create a dictionary to store the results
            'word_count_result': self.count_words(),        # output from the function count_words() from parent class
            'count_letters_result': self.count_letters()    # output from the function count_letters() from parent class
        }

        try:                                                                    # try to check file existence
            with open(self.json_file_path, 'w') as json_file:                   # open json file to write result
                json.dump(json_data, json_file, indent=2)                       # write json_data to the json_file with 2 spaces indent
            print(f'Data about successfully written to {self.json_file_path}')  # show this message
        except FileNotFoundError:                                               # if there is an exception about abstance of the file
            print(f'Error: File not found - {self.json_file_path}')             # show this message

        self.remove_source_file()

class XmlFileProcessor(FileAnalyzer):                             # create child class for work with XML
    def __init__(self, input_file_path, output_xml_path):         # create function with input file path and output path for future xml file
        super().__init__(input_file_path)                         # call methods from parent class and initializing input file_path
        self.output_xml_path = output_xml_path                    # create object to store file_path for output xml

    def process_and_write_to_xml(self):                           # create function for write data into a new file
        try:                                                      # try to check file existence
            with open(self.file_path, 'r') as input_file:         # open input file in read mode
                records = [line.strip() for line in input_file.readlines()]   # read all the lines from the input_file and return a list of strings with removal of all whitespaces

                if not records:                                               # if input file is empty
                    print("No records to process. Check the file format.")    # show this message
                    return                                                    # end function

                print(f"Records from {os.path.basename(self.file_path)}:")    # show this message
                for record in records:                                        # for each element in list
                    print(record)                                             # show elements

                root = ET.Element("root")                                     # create the root element
                for record in records:                                        # for each element from list
                    record_elem = ET.SubElement(root, "record")               # create element for each record
                    record_elem.text = record                                 # create object to store line like the content of the record

                xml_tree = ET.ElementTree(root)                               # create an ElementTree object from the provided root element
                xml_tree.write(self.output_xml_path)                          # write results to XML file

                print(f'Data successfully written to {self.output_xml_path}') # show this message

                input_file.close()                                            #close file
                self.remove_source_file()                                     # remove the input file if processed successfully

        except FileNotFoundError:                                            # if there is an exception about abstance of the file
            print(f"File not found: {self.file_path}")                       # show this message

xml_processor = XmlFileProcessor(r'C:\Users\Nastassia_Svirydava\PycharmProjects\Task1\nnd.txt', 'output.xml')   # create object with class call
xml_processor.process_and_write_to_xml()   # call process_and_write_to_xml function

# file_analyzer_with_json = JsonFileWriter(r'C:\Users\Nastassia_Svirydava\PycharmProjects\Task1\nn3.txt', 'results2.json') # create object with class call
# file_analyzer_with_json.write_to_files()                # call write fo files function
# file_analyzer_with_json.remove_source_file()            # call remove source file function

