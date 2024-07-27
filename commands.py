from Applications.application import ApplicationDatabase
from Applications.application import Application

class Command:
    @staticmethod
    def send_command(string):
        cmdStr: list = string.split(' ')
        if cmdStr[0] == 'run':
            Command.run_cmd(application=cmdStr[1], kwords=cmdStr)

    def run_cmd(application: str, **kwargs):
        app: 'Application' = ApplicationDatabase.get_application(application)
        if app != None:
            app.run_app(kwargs)
        else:
            print(f'Application {application} does not exist')
        