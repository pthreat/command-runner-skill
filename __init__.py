from mycroft import MycroftSkill, intent_file_handler


class CommandRunner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('runner.command.intent')
    def handle_runner_command(self, message):
        self.speak_dialog('runner.command')


def create_skill():
    return CommandRunner()

