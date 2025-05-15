import numpy as np

from ..autotest import question, QuestionInfo


@question
def fitmle(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Aplikacja wysyła dwa typy pakietów o długości `500B` i `1500B` przez łącze o szybkości `c={{c}}` (`B/s`).
Chcemy modelować aplikację jako system `M/M/1`. 
***Jaka powinna być szybkość obsługi
 `mu` jeżeli czas przesłania pakietu `t` modelujemy rozkładem wykładniczym o gęstości
 `f(t)=mu e^{-mu t}` i zaobserwowano następujące liczby pakietów?***
 
| `500B` | `1500B` |
|--------|---------|
| {{n5}} | {{n15}} |


## Wskazówki:

1. Dopasować rozkład wykładniczy do podanych danych
2. Pamiętać o przeliczeniu długości pakietu na czas transmisji

"""

    n = np.random.poisson(lam=1e4)
    lam = np.random.exponential(1e4)

    c = 2 ** np.round(np.log2(lam))

    pkt = np.random.exponential(lam, n)
    lens = np.asarray([500, 1500])

    # dpkt = np.argmin(np.abs(pkt-np.expand_dims(lens, 1)), 0)
    dpkt = np.asarray(pkt > 600, np.int32)
    dpkt = lens[dpkt]

    n5 = (dpkt == 500).sum()
    n15 = (dpkt == 1500).sum()

    mu_hat = (n5 + n15) / (n5 * 500. / c + n15 * 1500. / c)
    info = info.render(**locals())

    info = info.render(**locals())
    return info.replace(answer=mu_hat, tolerance=abs(0.1 * mu_hat))
