from datetime import datetime

class Task:
    def __init__(self,title , description='',done=False,created_at = None):
        self.title = title
        self.description = description
        self.done = done
        self.created_at = created_at or datetime.now().isoformat()
    def to_dict(self):
        return {
            'title':self.title,
            'description':self.description,
            'done':self.done,
            'created_at':self.created_at
        }
    @staticmethod
    def from_dict(data):
        return Task(
            title = data['title'],
            description= data.get('description',''),
            done= data.get('done', False),
            created_at=data.get('created_at')
        )