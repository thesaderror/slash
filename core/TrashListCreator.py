#class used for creating a list of social/forum that doesn't exist anymore
import os
class TrashListCreator:
    def __init__(self , trash_list_file_path = ".db/trash_list.txt"):
        self.trash_list_file_path = trash_list_file_path
        self.create_trash_list()

    def create_trash_list(self):
        #if the file aaa.txt doesn't exist, create it
        if  not os.path.isfile(self.trash_list_file_path):
            with(open(self.trash_list_file_path, "w")) as f:
                f.write("")

    
    def get(self):
        with(open(self.trash_list_file_path, "r")) as f:
            return f.read()

    def add(self, site):
        with(open(self.trash_list_file_path, "a")) as f:
            f.write(f"{site}\n")
    
    def check(self, site):
        trash_list = self.get()
        if site in trash_list:
            return True
        return False