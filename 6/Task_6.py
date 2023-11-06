import datetime
from datetime import date
from Task_4_for_5 import perform_text_transformations_1, perform_text_transformations_2
import os.path

class NewsFeed:                                                 # create class which will keep and update out news

    def __init__(self):                                         # create function with list of news
        self.records = []                                       # create empty list for future news
        self.file_path = ''                                     # create empty file path

    def add_record(self, record_type, text, add_info=None):     # create function with 2 obligatory parameters and 1 not
        if record_type == '1':                                  # if we choose 1
            record_type = "News"                                # then our record type is News
        elif record_type == '2':                                # if we choose 2
            record_type = "Private ad"                          # then our record type is Private Ad
        elif record_type == '3':                                # if we choose 3
            record_type = "My personal news"                    # then our record type My personal news
        elif record_type == '4':                                # if we choose 4
            record_type = "My file news"                        # then our record type My file news

        if record_type == "News":                                                                             # if we have record type as News
            current_date = date.today()                                                                       # get current date and save into current_date object
            record = "NEWS \n    Text: %s \n    City: %s\n    Date: %s" % (text, add_info, current_date)      # create record with all necessary info for with record, each info on a new row for this record type (text, city and date)
        elif record_type == "Private ad":                                                                     # if we have record type as Private Ad
            try:                                                                                              # try exception block to check date for a correct format
                expiration_date = datetime.datetime.strptime(add_info, '%Y-%m-%d')                            # try to recreate our input info from additional_info like YYYY-MM-DD fornat
                days_left = (expiration_date - datetime.datetime.now()).days                                  # find left days like current date minus out input date
                record = "PRIVATE AD \n    Text: %s \n    Expiration date %s \n    %s days left" % (text, expiration_date.strftime('%Y-%m-%d'), days_left)  # create record for Private Add with all necessary info for this record type (text, expiration date and left days)
            except ValueError:                                                                                # if there is an error
                print("ERROR - Please use YYYY-MM-DD format for date")                                        # show this message
                return                                                                                        # stop add_record function to avoid adding row with wrong date formate
        elif record_type == "My personal news":                                                               # if we have record type My personal news
            record = "PERSONAL NEWS \n    Text: %s \n    Additional info: %s" % (text, add_info)              # create new record with text and additional info for this record type
        elif record_type == "My file news":                                                                   # if we have record type My file news
            try:
                normal_text = perform_text_transformations_2(perform_text_transformations_1(text))              # create object to store normalized text by using function from Task_4.py
                record = "NEWS FROM MY FILE \n Text: {0}".format(normal_text)                                   # create record to save text for news from file
            except:
                None
        if text is not None and text.strip():       # if our text object is not empty or null
            self.records.append(record)             # add new records to the records list from NewsFeed class


    def read_news_from_file(self):                  # create function for reading news from file

        case = input("""Your default file path : %s   
            Please enter 1 if you agree    
            Please enter 2 if you want to change it
Select an option: """ % os.path.join(os.getcwd(), r'C:\Users\Nastassia_Svirydava\PycharmProjects\Task1\news'))    # create object to store user choice if he argee or disagree with default file path
        if case == '1':                                                                                           # if choice is 1
            file_path = os.path.join(os.getcwd(), r'C:\Users\Nastassia_Svirydava\PycharmProjects\Task1\news')     # then file path = default file path
            with open(file_path, encoding="utf8") as f:                                                           # open file with file path
                news = f.read()                                                                                   # read all data from the file and save to the object in string format
        elif case == '2':                                                                                         # if choice is 2
            file_path = input("Enter full file path for your news: ")                                             # create object to save user file path
            self.file_path = file_path                                                                            # save file path to the self object
            try:                                                                                                  # try exception block to check input file path
                with open(file_path, encoding="utf8") as f:                                                       # open file with file path
                    if os.stat(file_path).st_size == 0:                                                           # if file is empty (sixe = 0)
                        print('File is empty')                                                                    # show this message
                    else:                                                                                         # if file is not empty
                        news = f.read()                                                                           # read all data from the file and save to the object in string format
            except FileNotFoundError:                                                                             # if we catch not found file error
                print('ERROR - Please enter correct file path')                                                   # show this message
        else:                                                                                                     # if choice not in [1,2]
                print("ERROR - Please choose the correct option")                                                 # print this message

        try:                                                                                                      # try exception block to check that we can read any data from input file path to return object
            if os.stat(file_path).st_size != 0:                                                                   # if our file is not empty
                return news                                                                                       # return object news
        except:                                                                                                   # if we have any error
            return None                                                                                           # return None


    def file_removal(self):                                         # create fuction for input file removal if it was proccessed
        if os.stat(self.file_path).st_size != 0:                    # if our file is not empty
            print('File %s will be remoted now' % self.file_path)   # show message about next command
            try:                                                    # try exception block to check that we can remote our file
                os.remote(self.file_path)                           # remote file with input path file
                print('File was successfully remoted!')             # show this message if removal was successful
            except:                                                 # if any error
                print('File removal was failed!')                   # show this message that our file has been remoted

    def display_news(self):                     # create function for showing all records
        if not self.records:                    # if records list is empty
            print("NO ANY NEWS YET")            # then show this message
        else:                                   # if there are ony rows into records list
            for record in self.records:         # go in a loop per each row in list of records from class NewsFeed
                print(record)                   # show each row

    def save_to_file(self, filename):           # create function for publishing records to the file with 2 parameters (link to the object from class NewsFeed and name of the file)
        if self.records:                        # if we have records
            with open(filename, 'w') as file:   # create or open file with input file name for writing with automation closing
                for record in self.records:     # for each record in list if records
                    file.write(record + '\n')   # add each record to the file with enter between them
        else:                                               # if we don't have records
            print('File is not created, no data to save')   # show this message

def main():                                     # create main function for class
    news_feed = NewsFeed()                      # create object for the class NewsFeed

    while True:                                 # do loop till user types 6
        print("User-Generated News Feed")       # show options to type
        print("1. Add News")                    # show options to type
        print("2. Add Private ad")              # show options to type
        print("3. Add My personal news")        # show options to type
        print("4. Add news from file")          # show options to type
        print("5. Display News Feed")           # show options to type
        print("6. Save to File")                # show options to type
        print("7. Quit")                        # show options to type
        choice = input("Select an option: ")    # create object to save input from user

        if choice == '1':                                                                                               # if user types 1
            text = input("Please enter record text: ")                                                                  # create object for user text
            add_info = input("Enter additional information about city: ")                                               # create object for user city info
            news_feed.add_record(choice, text, add_info)                                                                # add record to the list of record based on record_type with the input data
        elif choice == '2':                                                                                             # if user types 2
            text = input("Please enter record text: ")                                                                  # create object for user text
            add_info = input("Enter additional information about expiration date in YYYY-MM-DD format: ")               # create object for user expiration date
            news_feed.add_record(choice, text, add_info)                                                                # add record to the list of record based on record_type with the input data
        elif choice == '3':                                                                                             # if user types 3
            text = input("Please enter record text: ")                                                                  # create object for user text
            add_info = input("Enter additional information: ")                                                          # create object for user additional info
            news_feed.add_record(choice, text, add_info)                                                                # add record to the list of record based on record_type with the input data
        elif choice == '4':                                                                                             # if user types 4
            text = news_feed.read_news_from_file()                                                                      # create object to store result from read_news_from_file function
            news_feed.add_record(choice, text)                                                                          # add record to the list of record based on record_type with the input data
            if news_feed.file_path != '':                                                                               # if we have file_path not empty
                news_feed.file_removal()                                                                                # call file_removal function
        elif choice == '5':                                                                                             # if user types 5
            news_feed.display_news()                                                                                    # then call display_news function
        elif choice == '6':                                                                                             # if user types 6
            filename = input("Enter the filename to save the news: ")                                                   # create object to store user input file name
            news_feed.save_to_file(filename)                                                                            # call save to file function with input file name parameter
            print('News saved to %s file' % filename)                                                                   # show text
        elif choice == '7':                                                                                             # if user types 7
            break                                                                                                       # exit the loop
        else:                                                                                                           # if user types something except 1 2 3 4 5 6 7
            print("ERROR - Please choose the correct option")                                                           # show this message

main()          # call main function


