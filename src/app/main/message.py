import json

class Message(object):

    def __init__(self):
        self.__raw_json = None
        self.body = None
        self.destination_number = None
        self.source_number = None

    def parse_json(self, message_json):
        self.__raw_json = json.loads(message_json)
        self.body = self.__raw_json.get('body', None)
        self.destination_number = self.__raw_json.get('to', None)
        self.source_number = self.__raw_json.get('from', None)

    def is_valid_message(self):
        valid = True
        if self.body is None:
            valid = False
        if self.destination_number is None:
            valid = False
        if self.source_number is None:
            valid = False

        return valid

