from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import os

# Create an abstract base class NewsFeed with abstract method publish.
# Each subclass: News, PrivateAd, BirthdayGreeting will have this method.
# In each subclass, publish will be overridden according to the task requirements.

class NewsFeed (ABC):
    @abstractmethod
    def publish(self, file):
        pass

# Create class News - subclass of NewsFeed
class News(NewsFeed):
    # Initialize News class with text,city, event_title variables.
    def __init__(self, text, city, event_title):
        self.text = text
        self.city = city
        self.event_title = event_title
    # Overwrite publish method that write News required data in the file
    def publish(self,file):
        formatted_date_time = datetime.now().strftime("%d/%m/%Y %H.%M") # get the current date and time, format datetime objects into strings with a required date/time format
        file.write(f"{self.event_title}\n{self.text}\n{self.city}, {formatted_date_time}\n\n")

# Create class PrivateAd - subclass of NewsFeed
class PrivateAd(NewsFeed):
    # Initialize PrivateAd class with text, expiration_date, event_title variables.
    def __init__(self, text, expiration_date, event_title):
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%d/%m/%Y")
        self.event_title = event_title

    # Overwrite publish method that write Private Ad required data in the file
    def publish(self, file):
        days_left = (self.expiration_date - datetime.now()).days # calculate days left
        file.write(f"{self.event_title}\n{self.text}\nActual until: {self.expiration_date.strftime('%d/%m/%Y')}, {days_left} days left\n\n")

# Create class BirthdayGreeting - subclass of NewsFeed.
# Where person who has birthday,  year of birth, greeting text are as input. Person age is calculated during publishing
class BirthdayGreeting (NewsFeed):
    def __init__(self, person, birth_year, text, event_title):
        self.person = person
        self.birth_year = birth_year
        self.event_title = event_title
        self.text = text

    def publish(self, file):
        current_date = datetime.now().strftime('%d/%m/%Y') # get the current date and time, format datetime objects into strings with a required date
        age = datetime.now().year - int(self.birth_year)
        file.write(f"{self.event_title}\n{self.person}\n{current_date}, {age} yeas old\n{self.text}\n\n")

def main():
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
            def news_feed_title(post_type, title_len=30):
                title = post_type + ' ' + ('-' * (title_len - len(post_type)))
                return title
            # If post type: 1 - News, ask enter required News data. Create a record  - object of News class.
            if choice == "1":
                text = input("Enter news text: ")
                city = input("Enter city: ")
                event_title = news_feed_title('News')
                record = News(text, city, event_title)
            # If post type: 2 - Private Ad, ask enter required Private Ad data. Create a record  - object of PrivateAd class.
            elif choice == "2":
                text = input("Enter advertising text: ")
                expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                try: # validate format and value of expiration date
                    datetime.strptime(expiration_date, "%d/%m/%Y")
                except (ValueError):
                    print("Entered expiration date has wrong format. Try to enter again.")
                    expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                if datetime.strptime(expiration_date, "%d/%m/%Y") < datetime.now():
                    print('Entered expiration date is less then current date. Try to enter again')
                    expiration_date = input("Enter expiration date (dd/mm/yyyy): ")
                event_title = news_feed_title('Private Ad')
                record = PrivateAd(text, expiration_date, event_title)
            # If post type: 3 - Birthday Greeting, ask enter required  Birthday Greeting data. Create a record  - object of Birthday Greeting class.
            elif choice == "3":
                person_name = input("Enter person first and last name whose birthday it is : ")
                input_year = input("Enter person year of birth : ")
                try: # validate data type and value of year of birth
                    int(input_year)
                except (ValueError):
                    print("Entered year of birth has wrong format. Try to enter again.")
                    input_year = input("Enter person year of birth : ")
                if int(input_year) >= datetime.now().year:
                    print('Entered year of birth is more or equal then current year. Try to enter again')
                    input_year = input("Enter person year of birth : ")
                text = input("Enter birthday greeting text: ")
                event_title = news_feed_title('Birthday Greeting')
                record = BirthdayGreeting(person_name, input_year, text, event_title)
            # if Exit then stop ask question, break while loop
            elif choice == "4":
                print("Exiting.")
                break
            # else - warning message, continue asking questions
            else:
                print("Invalid choice. Try again.")
                continue
            # Open specified file to write data to the end of the file.
            with open(file_name, "a") as file:
                record.publish(file) # call publish method of corresponding record object
            # display a message about the publication.
            print("Post published!\n")
        # If the specified file does not exist, open the file and write the general header.
        else:
            with open(file_name, "w") as file:
                file.write('News feed:\n')

if __name__ == "__main__":
    main()