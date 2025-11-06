from datetime import datetime
from Functions import normalize_letter_cases
import json
# Create class NewsFeed with abstract methods: create_title_info, publish.
# In each subclass: News, PrivateAd, BirthdayGreeting, publish will be overridden according to the task requirements.
# create_title_info method will be inherited from NewsFeed class without changes.
class NewsFeed:
    def __init__ (self, post_type, info_text = ''):
        self.post_type = post_type
        self.info_text = info_text
    def create_title_info(self, title_len = 30):
        self.title = self.post_type + ' ' + ('-' * (title_len - len(self.post_type)))
        if self.info_text != '':
            self.title += '\n' + self.info_text
    def publish(self, file):
        pass
# Create new class PostFromJsonFile - subclass of NewsFeed
class PostFromJsonFile(NewsFeed):
    def __init__(self, post_type, file_path, posts_json = [], not_remove = 0):
        super().__init__(post_type)
        self.file_path = file_path
        self.post_type = post_type
        self.posts_json = posts_json
        self.not_remove = not_remove
    def read_json_file(self):
        #self.posts_json = json.load(open(self.file_path))
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.posts_json = json.load(f)
    def publish(self, file):
        for element in self.posts_json:
            try:
                if element['type'] == 1:
                    formatted_date_time = datetime.now().strftime("%d/%m/%Y %H.%M")  # get the current date and time, format datetime objects into strings with a required date/time format
                    self.title = self.title.replace("Post from json file", "News")
                    file.write(f"{self.title}\n{element['news']}\n{element['city']}, {formatted_date_time}\n\n")
                    self.title = self.title.replace("News", "Post from json file")
                elif element['type'] == 2:
                    try: # validate format and value of expiration date
                        datetime.strptime(element['expiration_date'], "%d/%m/%Y")
                        expiration_date_json = datetime.strptime(element['expiration_date'], "%d/%m/%Y")
                        days_left = (expiration_date_json - datetime.now()).days  # calculate days left
                        self.title = self.title.replace("Post from json file", "Private Ad")
                        file.write(f"{self.title}\n{element['private_ad']}\nActual until: {expiration_date_json.strftime('%d/%m/%Y')}, {days_left} days left\n\n")
                        self.title = self.title.replace("Private Ad", "Post from json file")
                    except (ValueError):
                        print(f"Expiration date has wrong format. The post '{element}' can not be published.")
                        self.not_remove = 1
                elif element['type'] == 3:
                    try: # validate data type and value of year of birth
                        int(element['year_of_birth'])
                        current_date = datetime.now().strftime('%d/%m/%Y')  # get the current date and time, format datetime objects into strings with a required date
                        age = datetime.now().year - int(element['year_of_birth'])
                        self.title = self.title.replace("Post from json file", "Birthday Greeting")
                        file.write(f"{self.title}\n{element['person']}\n{current_date}, {age} yeas old\n{element['birthday_greeting']}\n\n")
                        self.title = self.title.replace("Birthday Greeting", "Post from json file")
                    except (ValueError):
                        print(f"Year of birth has wrong format. The post '{element}' can not be published.")
                        self.not_remove = 1
                else:
                    print(
                        f"The post '{element}' can not be published because it does not conform to the required format.")
                    self.not_remove = 1
            except (KeyError):
                print(f"The post '{element}' can not be published because it does not conform to the required format.")
                self.not_remove = 1
    def return_file_path(self):
        return self.file_path
# Create new class PostFromFile - subclass of NewsFeed
class PostFromFile(NewsFeed):
    def __init__(self, post_type, file_path, post_lines = []):
        super().__init__(post_type)
        self.file_path = file_path
        self.post_type = post_type
        self.post_lines = post_lines
    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.post_lines = f.readlines()
        f.close()
    def publish(self, file):
        file.write(f'{self.title}\n')
        for line in self.post_lines:
                norm_line = normalize_letter_cases(line)
                file.write(norm_line)
        file.write('\n\n')
    def return_file_path(self):
        return self.file_path

# Create class News - subclass of NewsFeed
class News(NewsFeed):
    # Initialize News class
    def __init__(self, text, city, post_type):
        super().__init__(post_type)
        self.text = text
        self.city = city
        self.post_type = post_type
    # Overwrite publish method that write News required data in the file
    def publish(self, file):
        formatted_date_time = datetime.now().strftime("%d/%m/%Y %H.%M") # get the current date and time, format datetime objects into strings with a required date/time format
        file.write(f"{self.title}\n{self.text}\n{self.city}, {formatted_date_time}\n\n")

# Create class PrivateAd - subclass of NewsFeed
class PrivateAd(NewsFeed):
    # Initialize PrivateAd class
    def __init__(self, text, expiration_date, post_type):
        super().__init__(post_type)
        self.text = text
        self.expiration_date = datetime.strptime(expiration_date, "%d/%m/%Y")
        self.post_type = post_type
    # Overwrite publish method that write Private Ad required data in the file
    def publish(self, file):
        days_left = (self.expiration_date - datetime.now()).days # calculate days left
        file.write(f"{self.title}\n{self.text}\nActual until: {self.expiration_date.strftime('%d/%m/%Y')}, {days_left} days left\n\n")

# Create class BirthdayGreeting - subclass of NewsFeed.
# Where person who has birthday,  year of birth, greeting text are as input. Person age is calculated during publishing
class BirthdayGreeting (NewsFeed):
    def __init__(self, person, birth_year, text, post_type):
        super().__init__(post_type)
        self.person = person
        self.birth_year = birth_year
        self.post_type = post_type
        self.text = text

    def publish(self, file):
        current_date = datetime.now().strftime('%d/%m/%Y') # get the current date and time, format datetime objects into strings with a required date
        age = datetime.now().year - int(self.birth_year)
        file.write(f"{self.title}\n{self.person}\n{current_date}, {age} yeas old\n{self.text}\n\n")
