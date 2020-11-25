from datetime import datetime

class Time:
    def __init__(self):
        self.now = datetime.now()
    
    def time(self):
        diff = datetime.now() - self.now
        total_sec = round(diff.total_seconds())
        return (total_sec // 60, total_sec % 60)
    
    def reset(self):
        self.now = datetime.now()

