from system.kernel import getter

class TrainslateApi:
    def __init__(self):
        chdriver_path = './chromedriver'
        self.getter = getter.Crawler(chdriver_path)

    def get_text(self, text):
        result = self.getter.get_text(text=text)
        return result