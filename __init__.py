from mycroft import MycroftSkill, intent_file_handler


class WiolinkWionodeVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voice.wionode.wiolink.intent')
    def handle_voice_wionode_wiolink(self, message):
        self.speak_dialog('voice.wionode.wiolink')


def create_skill():
    return WiolinkWionodeVoice()

