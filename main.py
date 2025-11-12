import os
from NewsFeed import News, PrivateAd, BirthdayGreeting
from CreateCSV import FileCSV, WordCountCSV, LetterCountCSV
from ParsingTXT import ParsingTXT
from ParsingJson import ParsingJson
if __name__ == "__main__":
    file_name = "news_feed.txt" # specify the path and file name
    while True:
        # If the specified file exists, suggest user to choose the post type: News/Private Ad/Birthday Greeting or exit the application
        if os.path.exists(file_name):
            print("""Select post type you want to add to news feed:
                1 - News
                2 - Private Ad
                3 - Birthday Greeting
                4 - Post from text file
                5 - Post from json file
                6 - Exit the application""")
            choice = input("Enter your choice (1/2/3/4/5/6): ")
            # create a function that generate post title

            # If post type: 1 - News, ask enter required News data. Create a record  - object of News class.
            if choice == "1":
                text = input("Enter news text: ")
                city = input("Enter city: ")
                record = News(text, city, 'News')
            # If post type: 2 - Private Ad, ask enter required Private Ad data. Create a record  - object of PrivateAd class.
            elif choice == "2":
                text = input("Enter advertising text: ")
                expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                record = PrivateAd(text, expiration_date, 'Private Ad')
                while True:
                    if record.is_valid_date() == False:
                        print('Entered expiration date is invalid. Try to enter again')
                        expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                        record = PrivateAd(text, expiration_date, 'Private Ad')
                    else:
                        break
            # If post type: 3 - Birthday Greeting, ask enter required  Birthday Greeting data. Create a record  - object of Birthday Greeting class.
            elif choice == "3":
                person_name = input("Enter person first and last name whose birthday it is : ")
                text = input("Enter birthday greeting text: ")
                input_year = input("Enter person year of birth : ")
                record = BirthdayGreeting(person_name, input_year, text, 'Birthday Greeting')
                while True:
                    if record.is_valid_birth_year() == False:
                        print('Entered year of birth is invalid. Try to enter again')
                        input_year = input("Enter person year of birth : ")
                        record = BirthdayGreeting(person_name, input_year, text, 'Birthday Greeting')
                    else:
                        break
            # if post type: 4 - Post from file, ask enter required  file path.
            # Receive lists of news, advertisements, birthday greetings from a text file, and the flag if the file contained data with an invalid format.
            elif choice == '4':
                is_invalid = 0
                while True:
                    not_continue_4 = 0
                    file_path_user = input("Enter file path or enter '-' to use default path: ")
                    if file_path_user == '-':
                        file_path_user =  "post_file.txt"
                    txt_data = ParsingTXT(file_path_user)
                    is_valid_path = txt_data.validate_file_path()
                    if is_valid_path == 1:
                        break
                    else:
                        choice_file = input("Do you want to enter again (y/n)? : ")
                        if choice_file == 'y':
                            continue
                        elif choice_file == 'n':
                            not_continue_4 = 1
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue
                if is_valid_path == 1:
                    news, ads, birthday_greetings, is_invalid = txt_data.read_file()
            # if post type: 5 - Post from json file, ask enter required  file path.
            # Receive lists of news, advertisements, birthday greetings from a json file, and the flag if the file contained data with an invalid format.
            elif choice == '5':
                is_invalid = 0
                while True:
                    not_continue_5 = 0
                    file_path_user = input("Enter json file path or enter '-' to use default path: ")
                    if file_path_user == '-':
                        file_path_user =  "post_json.json"
                    json_data = ParsingJson(file_path_user)
                    is_valid_path = json_data.validate_file_path()
                    if is_valid_path == 1:
                        break
                    else:
                        choice_file = input("Do you want to enter again (y/n)? : ")
                        if choice_file == 'y':
                            continue
                        elif choice_file == 'n':
                            not_continue_5 = 1
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue
                if is_valid_path == 1:
                    news, ads, birthday_greetings, is_invalid = json_data.read_file()
            # if Exit then stop ask question, break while loop
            elif choice == "6":
                print("Exiting.")
                break
            # else - warning message, continue asking questions
            else:
                print("Invalid choice. Try again.")
                continue
            # create an objects of WordCountCSV,  class
            word_csv = WordCountCSV(file_name)
            letter_csv = LetterCountCSV(file_name)

            # Open specified file to write data to the end of the file for user choices 1,2,3
            if (choice != '4' and choice != '5'):
                record.create_title_info()
                record.normalize_text()
                with open(file_name, "a", encoding="utf-8") as file:
                    post_published = record.publish(file) # call publish method of corresponding record object
                    # display a message about the publication.
                print(f"Post published:\n{post_published}\n")
                word_csv.read_created_file()
                word_csv.create_csv()
                letter_csv.read_created_file()
                letter_csv.create_csv()
            # Open specified file to write data to the end of the file for user choices: 4,5 since files may contain several news items, advertisements, and birthday greetings.
            if (choice == '4' and not_continue_4 == 0) or (choice == '5' and not_continue_5 == 0):
                with open(file_name, "a", encoding="utf-8") as file:
                    if news != []:
                        for post in news:
                            record = News(post[0], post[1], 'News')
                            record.create_title_info()
                            record.normalize_text()
                            post_published = record.publish(file)
                            print(f"Post published:\n{post_published}\n")
                            word_csv.read_created_file()
                            word_csv.create_csv()
                            letter_csv.read_created_file()
                            letter_csv.create_csv()
                    if ads != []:
                        for post in ads:
                            record = PrivateAd(post[0], post[1], 'Private Ad')
                            if record.is_valid_date() == True:
                                record.create_title_info()
                                record.normalize_text()
                                post_published = record.publish(file)
                                print(f"Post published:\n{post_published}\n")
                                word_csv.read_created_file()
                                word_csv.create_csv()
                                letter_csv.read_created_file()
                                letter_csv.create_csv()
                            else:
                                is_invalid = 1
                                print(f"Private Ad :\n{post}\ncan not be published because it has invalid expiration date\n")
                    if birthday_greetings != []:
                        for post in birthday_greetings:
                            record = BirthdayGreeting(post[0], post[1], post[2], 'Birthday Greeting')
                            if record.is_valid_birth_year() == True:
                                record.create_title_info()
                                record.normalize_text()
                                post_published = record.publish(file)
                                print(f"Post published:\n{post_published}\n")
                                word_csv.read_created_file()
                                word_csv.create_csv()
                                letter_csv.read_created_file()
                                letter_csv.create_csv()
                            else:
                                is_invalid = 1
                                print(f"Birthday Greeting :\n{post}\ncan not be published because it has invalid year of birth\n")
                # Check whether the file formats, date, and year are valid. If so, delete the files.
                if  choice == '4' and is_invalid == 0:
                    txt_data.delete_file()
                elif choice == '4' and is_invalid == 1:
                    print(f"File '{txt_data.file_path}' has not been deleted because it contains invalid posts. Posts with invalid format are in bad_records_txt.txt. Posts with invalid date or year are printed.\n")
                    is_invalid == 0
                if  choice == '5' and is_invalid == 0:
                    json_data.delete_file()
                elif choice == '5' and is_invalid == 1:
                    print(f"File '{json_data.file_path}' has not been deleted because it contains invalid posts. Posts with invalid format are in bad_records_json.json. Posts with invalid date or year are printed.\n")
                    is_invalid == 0
        else:
            # If the specified file does not exist, open the file and write the general header.
            with open(file_name, "w", encoding="utf-8") as file:
                file.write('News feed:\n')


