class Main:
    def __init__(self):
        self.hacker_name = 'H4CK3R'
        self.is_running = True

    def run(self):
        while self.is_running:
            input_data = input(f"{self.hacker_name} $ ")
            if input_data == 'Exit' or input_data == 'exit':
                self.is_running = False
            else:
                print(">>> ", input_data)

main = Main()
main.run()