from FileSystem.file_manager import FileManager
class Machine:
    def __init__(self, machine_ip, file_system):
        self.machine_ip:str = machine_ip
        self.file_system: FileManager = file_system