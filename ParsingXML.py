import xml
import xml.etree.ElementTree as ET
from ParsingFile import ParsingFile

# Class that parses xml file of a certain format
class ParsingXML(ParsingFile):
    def __init__(self, file_path):
        self.file_path = file_path
# Override the parent method xml file must be of a certain structure to be read
    def validate_file_path(self):
        valid = 0
        try:
            tree = ET.parse(self.file_path)
            valid = 1
        except(FileNotFoundError, xml.etree.ElementTree.ParseError):
            print("Entered xml file path is incorrect or xml file does not exists or xml file has wrong structure")
        return valid

    def read_file(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()

        news_posts = []
        ad_posts = []
        birthday_posts = []
        bad_posts = []
        is_invalid_format = 0
        for post in root.findall('post'):
            post_type = post.attrib.get('type')
            # News: needs <text> and <city>
            if post_type == "News":
                text = post.findtext('text')
                city = post.findtext('city')
                if text and city:
                    news_posts.append([text, city])
                else:
                    bad_posts.append(post)
            # Private Ad: needs <text> and <date>
            elif post_type == "Private Ad":
                text = post.findtext('text')
                date = post.findtext('date')
                if text and date:
                    ad_posts.append([text, date])
                else:
                    bad_posts.append(post)
            # Birthday Greeting: needs <person>, <birth_year>, <text>
            elif post_type == "Birthday Greeting":
                person = post.findtext('person')
                birth_year = post.findtext('birth_year')
                text = post.findtext('text')
                if person and birth_year and text:
                    birthday_posts.append([person, birth_year, text])
                else:
                    bad_posts.append(post)
                    is_invalid_format = 1
            else:
                # Invalid type or missing type
                bad_posts.append(post)
                is_invalid_format = 1

        # Save invalid posts to bad_records_xml.xml
        bad_root = ET.Element('bad_posts')
        for bad_post in bad_posts:
            bad_root.append(bad_post)

        bad_tree = ET.ElementTree(bad_root)
        bad_tree.write('bad_records_xml.xml', encoding='utf-8', xml_declaration=True)
        return news_posts, ad_posts, birthday_posts, is_invalid_format