

class Loader(object):
    def __init__(self, db):
        self.db = db
        self.model = {}

    def load(self, model_path):
        if model_path in self.model.keys():
            return self.model[model_path]
        __import__(model_path)