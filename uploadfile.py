from importlib import resources

def load_questions():
    with resources.open_text("professor-assistant", "questions.txt") as f:
        return f.read()
    