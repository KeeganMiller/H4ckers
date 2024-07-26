from Machines.machine_objects import Machine
from Machines.machine_database import MachineDatabase

class Main:
    def __init__(self):
        self.hacker_name = 'H4CK3R'                     # name of the hacker
        self.is_running = True                          # If the game is running
        self.connected_machine: Machine = None          # reference to the machine connected
        self.hacker_name_set = False

    # Main update loop
    def run(self):
        while self.is_running:
            if not self.hacker_name_set:
                name = input(f'Enter your hacker name: ')
                self.hacker_name = name;
                self.hacker_name_set = True
            else:
                inputValue = input(f'{self.hacker_name} $ ')
                if inputValue == 'Exit' or inputValue == 'exit':
                    self.is_running = False

    def connect_to_machine(self, ip):
        connected_machine = MachineDatabase.get_machine(ip)

main = Main()
main.run()
