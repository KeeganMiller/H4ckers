class ApplicationDatabase:
    available_applications: list = []                # Applications we can use

    @staticmethod
    def get_application(name: str) -> 'Application':
        for app in ApplicationDatabase.available_applications:
            if(app.name == name):
                return app
            
        return None


class Application:
    def __init__(self, name: str):
        self.application_name: str = name

    def run_app(self, **kwargs):
        pass

class TestApplication(Application):
    def __init__(self, name: str):
        super().__init__(name)

    def run_app(self, kwargs):
        print("Hello World!")