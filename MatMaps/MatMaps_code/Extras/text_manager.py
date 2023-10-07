import json as js


class TextManager:

    def __init__(self):
        pass

    def json_reader(self, text_source: str):
        manager = self.JsonManager(text_source)
        return manager.reader()

    class JsonManager:

        def __init__(self, text_source: str):
            self._text_source = text_source
            print(self._text_source)

        def reader(self):
            with open(self._text_source, "r") as f:
                dictionary = js.load(f)
            f.close()
            return dictionary
