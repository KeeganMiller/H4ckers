from Machines.machine_objects import Machine
from Machines.machine_database import MachineDatabase
from FileSystem.file_manager import FileManager
from commands import Command
from Applications.application import ApplicationDatabase

class Main:
    def __init__(self):
        self.hacker_name = 'H4CK3R'                     # name of the hacker
        self.is_running = True                          # If the game is running
        self.connected_machine: Machine = None          # reference to the machine connected
        self.hacker_name_set = False
        ApplicationDatabase.setup()                     # setup all the applications

    # Main update loop
    def run(self):
        
        while self.is_running:
            if not self.hacker_name_set:            # Create the hacker name
                name = input(f'Enter your hacker name: ')
                self.hacker_name = name;
                self.hacker_name_set = True
                self.create_home_machine()
            else:               # enter main loop
                # Validate that we are connected to a machine
                if(self.connected_machine == None):
                    raise Exception('Failed to connect to a machine')
                
                # read the players input
                inputValue = input(f'{self.connected_machine.machine_ip}#{self.connected_machine.file_system.current_folder.name} ~ {self.hacker_name} $ ')
                if inputValue == 'Exit' or inputValue == 'exit':            # exit game if called
                    self.is_running = False
                else:
                    Command.send_command(string=inputValue, machine=self.connected_machine)                 # send the command


    def connect_to_machine(self, ip):
        connected_machine = MachineDatabase.get_machine(ip)

    def create_home_machine(self):
        home_machine = Machine('127.0.0.1', FileManager.create_random_file_system('127.0.0.1'))
        MachineDatabase.available_machines.append(home_machine)
        self.connected_machine = home_machine


main = Main()
main.run()
