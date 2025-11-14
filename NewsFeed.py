from datetime import datetime
from Functions import normalize_letter_cases
import json
# Create class NewsFeed with abstract methods: create_title_info, publish.
# In each subclass: News, PrivateAd, BirthdayGreeting, publish will be overridden according to the task requirements.
# create_title_info method will be inherited from NewsFeed class without changes.
class NewsFeed:
    def __init__ (self, text, post_type, info_text = ''):
        self.post_type = post_type
        self.info_text = info_text
        self.text = text
    def create_title_info(self, title_len = 30):
        self.title = self.post_type + ' ' + ('-' * (title_len - len(self.post_type)))
        if self.info_text != '':
            self.title += '\n' + self.info_text
    # Method that adds a punctuation mark at the end if one is missing and applies a function to normalize letter case.
    def normalize_text(self):
        if self.text[-1] not in ('.', '!', '?'):
            self.text = self.text.strip() + '.'
        self.text = normalize_letter_cases(self.text)
    def publish(self, file):
        pass
# Create class News - subclass of NewsFeed
class News(NewsFeed):
    # Initialize News class
    def __init__(self, text, city, post_type):
        super().__init__(text, post_type)
        self.text = text
        self.city = city
        self.post_type = post_type
    # Overwrite publish method that write News required data in the file
    def publish(self, file):
        formatted_date_time = datetime.now().strftime("%d/%m/%Y %H.%M") # get the current date and time, format datetime objects into strings with a required date/time format
        published_record = f"{self.title}\n{self.text}\n{self.city}, {formatted_date_time}"
        file.write(f"{published_record}\n\n")
        return published_record

# Create class PrivateAd - subclass of NewsFeed
class PrivateAd(NewsFeed):
    # Initialize PrivateAd class
    def __init__(self, text, expiration_date, post_type):
        super().__init__(text, post_type)
        self.text = text
        self.expiration_date = expiration_date
        self.post_type = post_type
    # method that check date format and validity
    def is_valid_date(self):
        try:
            expiration_date_to_validate = datetime.strptime(self.expiration_date, '%d/%m/%Y')
            if expiration_date_to_validate < datetime.now():
                return False
            return True
        except ValueError:
            return False
    # Overwrite publish method that write Private Ad required data in the file
    def publish(self, file):
        self.expiration_date = datetime.strptime(self.expiration_date, '%d/%m/%Y')
        days_left = (self.expiration_date - datetime.now()).days # calculate days left
        published_record = f"{self.title}\n{self.text}\nActual until: {self.expiration_date.strftime('%d/%m/%Y')}, {days_left} days left"
        file.write(f"{published_record}\n\n")
        return published_record

# Create class BirthdayGreeting - subclass of NewsFeed.
# Where person who has birthday,  year of birth, greeting text are as input. Person age is calculated during publishing
class BirthdayGreeting (NewsFeed):
    def __init__(self, person, birth_year, text, post_type):
        super().__init__(text, post_type)
        self.person = person
        self.birth_year = birth_year
        self.post_type = post_type
        self.text = text
    # method that check year validity
    def is_valid_birth_year(self):
        try:
            int(self.birth_year)
            if int(self.birth_year) >= datetime.now().year:
                return False
            return True
        except ValueError:
            return False

    def publish(self, file):
        current_date = datetime.now().strftime('%d/%m/%Y') # get the current date and time, format datetime objects into strings with a required date
        age = datetime.now().year - int(self.birth_year)
        published_record = f"{self.title}\n{self.person}\n{current_date}, {age} yeas old\n{self.text}"
        file.write(f"{published_record}\n\n")
        return published_record
