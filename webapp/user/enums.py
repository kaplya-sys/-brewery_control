from enum import Enum

class Profession(Enum):
    brewer = 'brewer'
    assistant = 'assistant'
    admin = 'admin'

    def get_translated_value(self):
        translated_value = None

        if self == self.brewer:
            translated_value = 'Пивовар'
        elif self == self.assistant:
            translated_value = 'Ассистент'
        elif self == self.admin:
            translated_value = 'Админ'
        return translated_value