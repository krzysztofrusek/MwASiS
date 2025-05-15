import numpy as np
from scipy.stats import norm

from ..autotest import question, QuestionInfo


@question
def normalny(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Grupa {{n}} użytkowników generuje ruch.
Każdy użytkownik osobno generuje średnio {{m}} Mb/s z odchyleniem standardowym {{s}}.
Oszacować wartość przepustowości, która przez {{p}} nie będzie przepełniona.

"""

    n = np.ceil(np.random.normal(loc=10000, scale=1000))
    m = np.random.exponential(1)
    s = np.random.exponential(10)

    p = norm.cdf(np.random.normal(loc=1.0, scale=0.2))
    assert p
    assert not np.isnan(p)
    c=norm(loc=n*m, scale= np.sqrt(n*s**2)).ppf(p)

    info = info.render(**locals())

    info = info.render(**locals())
    return info.replace(answer=c, tolerance=abs(0.05 * c))
