from ..FileSystem.file_manager import FileManager
class Machine:
    def __init__(self, machine_ip, file_system):
        self.machine_ip = machine_ip
        self.file_system = file_system