
class GameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def to_dict(self):
        return {"error": self.message}
