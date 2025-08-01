from enum import Enum
from datetime import datetime
from database import load_database


DB_PATH = "./tasks.json"

class Status(Enum):

    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'


class Task:

    def __init__(self,description):
        
        self.id = self.get_id()
        self.description = description
        self.status = Status.TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_id(self) -> int:

        tasks = load_database(DB_PATH)

        return len(tasks)
    
    def to_dict(self) -> dict:

        return {
            "description" : self.description,
            "status" : self.status.value,
            "created_at" : str(self.created_at),
            "updated_at" : str(self.updated_at)
        }
    