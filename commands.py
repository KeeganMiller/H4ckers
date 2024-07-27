from Applications.application import ApplicationDatabase
from Applications.application import Application

class Command:

    def send_command(self, **kwargs):
        match(kwargs['action']):
            case 'run':
                self.run_cmd(kwargs)

    def run_cmd(self, **kwargs):
        if 'application' in kwargs:
            app: 'Application' = ApplicationDatabase.get_application(kwargs['application'])
            if app != None:
                app.run_app(kwargs)
            else:
                print(f'Application {kwargs['application']} does not exist')
        else:
            print(f"Application does not exist: {kwargs['application']}")
        