from app import app, db
from models import Task

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Task=Task)