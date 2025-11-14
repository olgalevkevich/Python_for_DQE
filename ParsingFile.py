import os
import elevate

# Class that has generic methods to check if file parth is valid, delete the file
class ParsingFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate_file_path (self):
        valid = 0
        if os.path.exists(self.file_path):
            valid = 1
        else:
            print ("Entered file path is incorrect or file does not exists.")
        return valid

    def read_file (self):
        pass

    def delete_file (self):
        try:
            os.remove(self.file_path)
            print(f"File '{self.file_path}' has been successfully processed and deleted.\n")
        except(FileNotFoundError):
            print(f"File '{self.file_path}' does not exist.")
        except(PermissionError):
            print(
                f"Access to '{self.file_path}' is denied. To delete the file, the program must be restarted to elevate its privileges. All published posts will remain published.")
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



