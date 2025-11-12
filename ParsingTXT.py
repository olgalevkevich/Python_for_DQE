import re
from ParsingFile import ParsingFile

# Class that parses a text file of a certain format
class ParsingTXT(ParsingFile):
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file (self):
        # Read the file content
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Patterns for valid posts
        news_pattern = re.compile(r'<post>\s*<type>News</type>\s*<text>.*?</text>\s*<city>.*?</city>\s*</post>',re.DOTALL)
        ad_pattern = re.compile(r'<post>\s*<type>Private Ad</type>\s*<text>.*?</text>\s*<date>.*?</date>\s*</post>',re.DOTALL)
        birthday_pattern = re.compile(r'<post>\s*<type>Birthday Greeting</type>\s*<person>.*?</person>\s*<birth_year>\d{4}</birth_year>\s*<text>.*?</text>\s*</post>',re.DOTALL)

        # Patterns for required data in valid posts
        news_pattern_data = re.compile(r"<post>\s*<type>News</type>\s*<text>(.*?)</text>\s*<city>(.*?)</city>\s*</post>",re.DOTALL)
        ad_pattern_data = re.compile(r"<post>\s*<type>Private Ad</type>\s*<text>(.*?)</text>\s*<date>(.*?)</date>\s*</post>",re.DOTALL)
        birthday_pattern_data = re.compile(r"<post>\s*<type>Birthday Greeting</type>\s*<person>(.*?)</person>\s*<birth_year>(\d{4})</birth_year>\s*<text>(.*?)</text>\s*</post>",re.DOTALL)

        # Find all valid posts
        news_posts = news_pattern.findall(content)
        ad_posts = ad_pattern.findall(content)
        birthday_posts = birthday_pattern.findall(content)

        # Find all required data in valid posts
        news_posts_data = news_pattern_data.findall(content)
        ad_posts_data = ad_pattern_data.findall(content)
        birthday_posts_data = birthday_pattern_data.findall(content)

        # Find all <post>...</post> blocks
        all_posts = re.findall(r'<post>.*?</post>', content, re.DOTALL)

        # Identify invalid posts
        valid_posts_set = set(news_posts + ad_posts + birthday_posts)
        invalid_posts = [post for post in all_posts if post not in valid_posts_set]

        # Also, find lines that not inside <post>...</post> blocks
        not_posts_content = re.sub(r'<post>.*?</post>', '', content, flags=re.DOTALL)
        not_posts_lines = [line for line in not_posts_content.splitlines() if line.strip()]

        # Save invalid posts and lines not inside <post>...</post> to bad_records_txt.txt
        with open('bad_records_txt.txt', 'w', encoding='utf-8') as f:
            for post in invalid_posts:
                f.write(post + '\n')
            for line in not_posts_lines:
                f.write(line + '\n')

        # make news, advertisement, birthday greetings lists with data from valid posts
        news_list = [ [item[0].strip(), item[1].strip()] for item in news_posts_data ]
        ad_list = [ [item[0].strip(), item[1].strip()] for item in ad_posts_data]
        birthday_list = [ [item[0].strip(), int(item[1]), item[2].strip()] for item in birthday_posts_data]

        is_invalid_format = 0
        if invalid_posts != [] or not_posts_lines != []:
            is_invalid_format = 1
        return news_list, ad_list, birthday_list, is_invalid_format



