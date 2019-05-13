from .system.kernel import getter

class TranslateApi:
    def __init__(self, chdriver_path):
        self.getter = getter.Crawler(chdriver_path)

    def get_text(self, text):
        result = self.getter.get_text(text=text)
        return result