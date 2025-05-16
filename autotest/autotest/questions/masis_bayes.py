import numpy as np
from scipy.stats import poisson
from scipy.stats import expon
from scipy.stats import norm
from scipy.stats import uniform


from ..autotest import question, QuestionInfo


@question
def bayes(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Sensytywność testu na ADHD wynosi {{sen}}, co oznacza zdolność do poprawnego zidentyfikowania pacjentów z ADHD.
Specyficzność testu, czyli zdolność do poprawnego wykluczenia ADHD u osób, które nie są dotknięte tym zaburzeniem, wynosi {{spe}}.
Zakładając, że w populacji występuje 1% osób z ADHD, jakie jest prawdopodobieństwo, że osoba, u której test wykazał ADHD, rzeczywiście jest dotknięta tym zaburzeniem?
Wynik podać w precyzji raportowanej z pythona.
"""

    sen = np.round(0.9 + np.random.uniform()/10, 2)
    spe = np.round(0.9 + np.random.uniform()/10, 2)
    info = info.render(spe=spe, sen=sen)

    answer = sen*0.01/(sen*0.01+(1-spe)*0.99)

    return info.replace(answer=answer, tolerance=0.05*answer)
