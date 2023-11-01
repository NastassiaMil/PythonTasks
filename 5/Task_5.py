import datetime
from datetime import date

class NewsFeed:                                                 # create class which will keep and update out news

    def __init__(self):                                         # create function with list of news
        self.records = []                                       # create empty list for future news

    def add_record(self, record_type, text, add_info):          # create function with 3 parameters
        if record_type == '1':                                  # if we choose 1
            record_type = "News"                                # then our record type is News
        elif record_type == '2':                                # if we choose 2
            record_type = "Private ad"                          # then our record type is Private Ad
        elif record_type == '3':                                # if we choose 3
            record_type = "My personal news"                    # then our record type My personal news

        if record_type == "News":                                                                                                                           # if we have record type as News
            current_date = date.today()                                                                                                                     # get current date and save into current_date object
            record = "NEWS \n    Text: %s \n    City: %s\n    Date: %s" % (text, add_info, current_date)                                                    # create record with all necessary info for with record, each info on a new row for this record type (text, city and date)
        elif record_type == "Private ad":                                                                                                                   # if we have record type as Private Ad
            try:                                                                                                                                            # try exception block to check date for a correct format
                expiration_date = datetime.datetime.strptime(add_info, '%Y-%m-%d')                                                                          # try to recreate our input info from additional_info like YYYY-MM-DD fornat
                days_left = (expiration_date - datetime.datetime.now()).days                                                                                # find left days like current date minus out input date
                record = "PRIVATE AD \n    Text: %s \n    Expiration date %s \n    %s days left" % (text, expiration_date.strftime('%Y-%m-%d'), days_left)       # create record for Private Add with all necessary info for this record type (text, expiration date and left days)
            except ValueError:                                                                              # if there is an error
                print("ERROR - Please use YYYY-MM-DD format for date")                                      # show this message
                return                                                                                      # stop add_record function to avoid adding row with wrong date formate
        elif record_type == "My personal news":                                                             # if we have record type My personal news
            record = "PERSONAL NEWS \n    Text: %s \n    Additional info: %s" % (text, add_info)            # create new record with text and additional info for this record type

        self.records.append(record)             # add new records to the records list from NewsFeed class

    def display_news(self):                     # create function for showing all records
        if not self.records:                    # if records list is empty
            print("NO ANY NEWS YET")            # then show this message
        else:                                   # if there are ony rows into records list
            for record in self.records:         # go in a loop per each row in list of records from class NewsFeed
                print(record)                   # show each row

    def save_to_file(self, filename):           # create function for publishing records to the file with 2 parameters (link to the object from class NewsFeed and name of the file)
        with open(filename, 'w') as file:       # create or open file with input file name for writing with automation closing
            for record in self.records:         # for each record in list if records
                file.write(record + '\n')       # add each record to the file with enter between them

def main():                                     # create main function for class
    news_feed = NewsFeed()                      # create object for the class NewsFeed

    while True:                                 # do loop till user types 6
        print("User-Generated News Feed")       # show options to type
        print("1. Add News")                    # show options to type
        print("2. Add Private ad")              # show options to type
        print("3. Add My personal news")        # show options to type
        print("4. Display News Feed")           # show options to type
        print("5. Save to File")                # show options to type
        print("6. Quit")                        # show options to type
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
            news_feed.display_news()                                                                                    # then call display_news function
        elif choice == '5':                                                                                             # if user types 5
            filename = input("Enter the filename to save the news: ")                                                   # create object to store user input file name
            news_feed.save_to_file(filename)                                                                            # call save to file function with input file name parameter
            print('News saved to %s file' % filename)                                                                   # show text
        elif choice == '6':                                                                                             # if user types 6
            break                                                                                                       # exit the loop
        else:                                                                                                           # if user types something except 1 2 3 4 5 6
            print("ERROR - Please choose the correct option")                                                           # show this message

main()          # call main function
