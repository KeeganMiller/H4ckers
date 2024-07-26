class FileObject:
    def __init__(self, name, absolute_path):
        self.name = name
        self.absolute_path = absolute_path

    def open(self):
        pass

class File(FileObject):
    def __init__(self, name, absolute_path, extension):
        super.__init__(name, absolute_path)
        self.extension = extension

    def open(self):
        pass

    def download(self):
        pass

class Folder(FileObject):
    def __init__(self, name, absolute_path, parent_folder):
        super.__init__(name, absolute_path)
        self.parent_folder = parent_folder
        self.folder_assets = []

    def open(self):
        pass

    def add_asset(self, asset):
        self.folder_assets.append(asset)

    def list_assets(self):
        for asset in self.folder_assets:
            if(asset is Folder):
                print(asset.name)
            else:
                print(f'{asset.name}.{asset.extension}')