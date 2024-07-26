from Machines.machine_objects import Machine

class MachineDatabase:
    available_machines = []

    @staticmethod
    def get_machine(self, ip) -> Machine:
        for machine in self.available_machines:
            if machine.machine_ip == ip:
                return machine
        return None;