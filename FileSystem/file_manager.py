from FileSystem.file_objects import Folder, File

class FileManager():
    def __init__(self, connected_ip):
        self.connected_ip
        self.current_folder
        self.folder_elements

    def list_folders(self):
        self.current_folder.list_assets

    # Creates a random file system for a machine
    # TODO: Make Random
    @staticmethod
    def create_random_file_system(self, ip) -> __name__:
        home = Folder('Home', '/Home/', '')
        folder_one = Folder('FolderOne', '/Home/FolderOne/', 'Home')
        subfolder_one = Folder('SubFolderOne', '/Home/FolderOne/SubFolderOne', 'FolderOne')
        folder_two = Folder('FolderTwo', '/Home/FolderTwo/', 'Home')
        txt_file_one = File('test', '/Home/folder_one/test.txt', '.txt')
        txt_file_two = File('test2', 'Home/folder_two/test2.txt', '.txt')
        txt_file_three = File('test3', 'Home/folder_one/SubFolderOne/test3.txt', '.txt')

        home.add_asset(folder_one)
        home.add_asset(folder_two)
        folder_one.add_asset(subfolder_one)
        folder_one.add_asset(txt_file_one)
        folder_two.add_asset(txt_file_two)
        subfolder_one.add_asset(txt_file_three)

        new_file_system = FileManager(ip)
        new_file_system.current_folder = home
        return new_file_system

        
