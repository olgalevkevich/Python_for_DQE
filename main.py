import os
import elevate
from datetime import datetime
from NewsFeed import PostFromFile, News, PrivateAd, BirthdayGreeting
if __name__ == "__main__":
    file_name = "news_feed.txt" # specify the path and file name
    while True:
        # If the specified file exists, suggest user to choose the post type: News/Private Ad/Birthday Greeting or exit the application
        if os.path.exists(file_name):
            print("""Select post type you want to add to news feed:
                1 - News
                2 - Private Ad
                3 - Birthday Greeting
                4 - Post from file
                5 - Exit the application""")
            choice = input("Enter your choice (1/2/3/4/5): ")
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
            # if post type: 4 - Post from file, ask enter required  file path. Create a record  - object of Birthday Greeting class.
            elif choice == '4':
                while True:
                    file_path_user = input("Enter file path or enter '-' to use default path: ")
                    if file_path_user == '-':
                        file_path_user =  "C:/Users/post_file.txt"
                    record = PostFromFile('Post from file', file_path_user)
                    try:
                        record.read_file()
                        file_to_delete = record.return_file_path()
                        break
                    except(FileNotFoundError, PermissionError):
                        print ("Entered file path is incorrect of file does not exists.")
                        choice_file = input("Do you want to enter again (y/n)? : ")
                        if choice_file == 'y':
                            continue
                        elif choice_file == 'n':
                            file_to_delete = ''
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue
            # if Exit then stop ask question, break while loop
            elif choice == "5":
                print("Exiting.")
                break
            # else - warning message, continue asking questions
            else:
                print("Invalid choice. Try again.")
                continue
            record.create_title_info()
            # Open specified file to write data to the end of the file.
            if choice != '4' or (choice == '4' and file_to_delete != ''):
                with open(file_name, "a", encoding="utf-8") as file:
                    record.publish(file) # call publish method of corresponding record object
                    # display a message about the publication.
                print("Post published!\n")
            if choice == '4' and file_to_delete != '':
                # Check if the file exists and delete it
                try:
                    os.path.exists(file_to_delete)
                    os.remove(file_to_delete)
                    print(f"File '{file_to_delete}' has been deleted.\n")
                except(FileNotFoundError):
                    print(f"File '{file_to_delete}' does not exist.")
                except(PermissionError):
                    print(f"Access to '{file_to_delete}' is denied. To delete the file, the program must be restarted to elevate its privileges. All published posts will remain published.")
                    while True:
                        choice_permitions = input("Do you want to restart the program? Enter your choice (y/n): ")
                        if choice_permitions == 'y':
                            elevate.elevate()
                            break
                        elif choice_permitions == 'n':
                            break
                        else:
                            print("Invalid choice. Try again.")
                            continue
        # If the specified file does not exist, open the file and write the general header.
        else:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write('News feed:\n')
