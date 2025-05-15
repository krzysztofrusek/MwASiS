import numpy as np
from scipy.stats import poisson
from scipy.stats import expon
from scipy.stats import norm
from scipy.stats import uniform


from ..autotest import question, QuestionInfo


@question
def bayesconjugate(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Wysłano {{n}} pakietów. Do celu dotarło {{a}}.
Wyznaczyć średnią a posteriori współczynnika strat pakietów, jeżeli a priori zakładamy,
że ma on rozkład beta o średniej {{pm}} i parametry spełniają warunek `beta+alpha=10`.
"""

    n = np.random.randint(1, 1000)
    a = np.random.randint(1, n)

    pm = np.random.random()
    alpha = pm*10
    beta = 10-alpha

    alpha_prim = n-a+alpha
    beta_prim = a+ beta
    info = info.render(**locals())

    answer = alpha_prim/(alpha_prim+beta_prim)

    return info.replace(answer=answer, tolerance=0.05*answer)
