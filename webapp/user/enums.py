from enum import Enum

class Profession(Enum):
    brewer = 'brewer'
    assistant = 'assistant'
    admin = 'admin'

    def get_translated_value(self):
        translated_value = None

        if self == Profession.brewer:
            translated_value = 'Пивовар'
        elif self == Profession.assistant:
            translated_value = 'Ассистент'
        elif self == Profession.admin:
            translated_value = 'Админ'
        return translated_value