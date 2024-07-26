from Machines.machine_objects import Machine

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

main = Main()
main.run()
