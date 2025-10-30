from datetime import datetime
import os
from NewsFeed import *

if __name__ == "__main__":
    file_name = "news_feed.txt" # specify the path and file name
    while True:
        # If the specified file exists, suggest user to choose the post type: News/Private Ad/Birthday Greeting or exit the application
        if os.path.exists(file_name):
            print("""Select post type you want to add to news feed:
                1 - News
                2 - Private Ad
                3 - Birthday Greeting
                4 - Exit the application""")
            choice = input("Enter your choice (1/2/3/4): ")
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
                while True:
                    try: # validate format and value of expiration date
                        datetime.strptime(expiration_date, "%d/%m/%Y")
                        if datetime.strptime(expiration_date, "%d/%m/%Y") < datetime.now():
                            print('Entered expiration date is equal or less then current date. Try to enter again')
                            expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                        else:
                            break
                    except (ValueError):
                        print("Entered expiration date has wrong format. Try to enter again.")
                        expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                record = PrivateAd(text, expiration_date, 'Private Ad')
            # If post type: 3 - Birthday Greeting, ask enter required  Birthday Greeting data. Create a record  - object of Birthday Greeting class.
            elif choice == "3":
                person_name = input("Enter person first and last name whose birthday it is : ")
                input_year = input("Enter person year of birth : ")
                while True:
                    try: # validate data type and value of year of birth
                        int(input_year)
                        if int(input_year) >= datetime.now().year:
                            print('Entered year of birth is more or equal then current year. Try to enter again')
                            input_year = input("Enter person year of birth : ")
                        else:
                            break
                    except (ValueError):
                        print("Entered year of birth has wrong format. Try to enter again.")
                        input_year = input("Enter person year of birth : ")
                text = input("Enter birthday greeting text: ")
                record = BirthdayGreeting(person_name, input_year, text, 'Birthday Greeting')
            # if Exit then stop ask question, break while loop
            elif choice == "4":
                print("Exiting.")
                break
            # else - warning message, continue asking questions
            else:
                print("Invalid choice. Try again.")
                continue
            record.create_title_info()
            # Open specified file to write data to the end of the file.
            with open(file_name, "a", encoding="utf-8") as file:
                record.publish(file) # call publish method of corresponding record object
            # display a message about the publication.
            print("Post published!\n")
        # If the specified file does not exist, open the file and write the general header.
        else:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write('News feed:\n')
