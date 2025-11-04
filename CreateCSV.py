import csv
import re
from collections import Counter
import string

# create CreateFileCSV with 2 methods: to read previously created text file, write data to new csv file
class FileCSV:
    def __init__ (self, file_path, text = ''):
        self.file_path = file_path
        self.text = text
    def read_created_file (self):
        with open(self.file_path, 'r', encoding='utf-8') as f: # Read news feed file contents
            self.text = f.read()
    def create_csv (self, file_path_csv):
        pass
# Create new class WordCountCSV - subclass of FileCSV, to create csv file for word count
class WordCountCSV(FileCSV):
    def __init__ (self, file_path, text = ''):
        super().__init__(file_path, text = '')
        self.file_path = file_path
        self.text = text
    def create_csv (self, file_path_csv = 'word_count.csv'):
        # Extract words (case-insensitive) using regular expression pattern
        words = re.findall(r'\b\w+\b', self.text.lower())
        # Count unique words
        word_counts = Counter(words)
        # Write words count to csv file with delimiter '-'
        with open(file_path_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for word, count in word_counts.items():
                writer.writerow([word, count])

# Create new class LetterCountCSV - subclass of FileCSV, to create csv file for letter count
class LetterCountCSV(FileCSV):
    def __init__ (self, file_path, text = ''):
        super().__init__(file_path, text = '')
        self.file_path = file_path
        self.text = text
    def create_csv (self, file_path_csv = 'letter_count.csv'):
        # Filter only letters (ignore spaces and non-letters using isalpha() and save them into list
        letters = [x for x in self.text if x.isalpha()]

        # Count total number of letters
        total_letters = len(letters)

        # Count all case-insensitive letters, upper case letters and save it to dictionary letters_count
        letters_count = {}
        for l in letters:
            letter = l.lower()
            if letter not in letters_count:
                letters_count[letter] = {'count_all': 0, 'count_upper': 0}
            letters_count[letter]['count_all'] += 1
            if l.isupper():
                letters_count[letter]['count_upper'] += 1

        # Write required data to csv file
        with open(file_path_csv, 'w', newline='', encoding='utf-8') as csvfile:
            headers = ['letter', 'cout_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers)
            writer.writeheader()
            for letter in sorted(letters_count.keys()):
                count_all = letters_count[letter]['count_all']
                count_upper = letters_count[letter]['count_upper']
                percentage = round((count_all / total_letters) * 100, 1)
                writer.writerow({'letter': letter, 'cout_all': count_all, 'count_uppercase': count_upper,
                                 'percentage': f"{percentage}%"})

