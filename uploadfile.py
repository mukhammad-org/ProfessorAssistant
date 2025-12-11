from importlib import resources

def load_questions():
    with resources.open_text("ProfessorAssistant", "QuestionsBank.txt") as f:
        return f.read()
    