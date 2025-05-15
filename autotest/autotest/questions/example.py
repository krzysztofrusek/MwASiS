from autotest import question, QuestionInfo

@question
def przykladowe(seed:int, info:QuestionInfo)->QuestionInfo:
    """
Ile wynosi wynik obliczeń {{ data }}
    """
    this = info.render(data=f"2+{seed}")
    return this.replace(answer=2+seed)