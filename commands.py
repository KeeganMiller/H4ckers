from Applications.application import ApplicationDatabase
from Applications.application import Application
from Machines.machine_objects import Machine
from FileSystem.file_manager import FileManager

class Command:
    @staticmethod
    def send_command(string, machine: Machine):
        cmdStr: list = string.split(' ')
        match(cmdStr[0]):
            case 'run':
                Command.run_cmd(application=cmdStr[1], kwords=cmdStr)
            case 'list':
                Command.list_cmd(machine=machine)
            
    # Handles running an application
    def run_cmd(application: str, **kwargs):
        app: 'Application' = ApplicationDatabase.get_application(application)
        if app != None:
            app.run_app(kwargs)
        else:
            print(f'Application {application} does not exist')

    def list_cmd(**kwargs):
        if 'machine' in kwargs:
            kwargs['machine'].file_system.list_folders()
        else:
            print(f'Failed to list folder, machine not connected')
            
