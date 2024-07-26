from machine_objects import Machine

class MachineDatabase:
    def __init__(self):
        self.available_machines = ['127.0.0.1']

    @staticmethod
    def get_machine(self, ip) -> Machine:
        for machine in self.available_machines:
            if machine.machine_ip == ip:
                return machine
        return None;