import json
from ParsingFile import ParsingFile

# Class that parses json file of a certain format
class ParsingJson(ParsingFile):
    def __init__(self, file_path):
        self.file_path = file_path
# Override the parent method since json file must be of a certain structure to be read
    def validate_file_path (self):
        valid = 0
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                json_file = json.load(f)
            valid = 1
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            print ("Entered json file path is incorrect or json file does not exists or json file has wrong structure")
        return valid

    def read_file(self):
        # Load posts from file
        with open(self.file_path, 'r', encoding='utf-8') as f:
            posts = json.load(f)
        news_posts = []
        ad_posts = []
        birthday_posts = []
        bad_records = []
        is_invalid_format = 0
        for post in posts:
            # News validation
            if post.get("type") == "News" and "text" in post and "city" in post and len(post) == 3:
                news_posts.append([post["text"], post["city"]])
            # Private Ad validation
            elif post.get("type") == "Private Ad" and "text" in post and "expiration_date" in post and len(post) == 3:
                ad_posts.append([post["text"], post["expiration_date"]])
            # Birthday Greeting validation
            elif post.get("type") == "Birthday Greeting" and "person" in post and "year_of_birth" in post and "text" in post and len(post) == 4:
                birthday_posts.append([post["person"], post["year_of_birth"], post["text"]])
            else:
                bad_records.append(post)
                is_invalid_format = 1
        # Save invalid posts to bad_records_json.json
        with open('bad_records_json.json', 'w', encoding='utf-8') as f:
            json.dump(bad_records, f, ensure_ascii=False, indent=2)
        return news_posts, ad_posts, birthday_posts, is_invalid_format

