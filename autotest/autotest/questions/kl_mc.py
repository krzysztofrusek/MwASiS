import jax
import jax.numpy as jnp
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions


from ..autotest import question, QuestionInfo


@question
def kl(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Wyznaczyć numerycznie dywergencję Kullbacka-Leiblera `KL(q|p)` pomiędzy

- `q(x)  = N(mu, sigma^2)` i
- `p(x) = Exp(lam)`

__Obliczenia wykonać dla min 50000 punktów__

## Parametry

- `mu = {{mu}}`
- `sigma = {{sigma}}`
- `lam = {{lam}}`


"""

    N=100000
    qfun = lambda mu, sigma: tfd.Sample(tfd.Normal(loc=mu, scale=sigma), N)
    pfun = lambda lam: tfd.Sample(tfd.Exponential(rate=lam), N)

    joint = tfd.JointDistributionNamed(dict(
        mu = tfd.Normal(loc=0.0, scale=1.0),
        sigma = tfd.Exponential(rate=1),
        lam = tfd.Exponential(rate=1),
        q = qfun,
        # p = pfun
    ))

    s = joint.sample(seed=seed)
    q = qfun(s['mu'], s['sigma'])
    p = pfun(s['lam'])
    kl = (q.log_prob(s['q']) - p.log_prob(s['q']))/N

    mu = float(s['mu'].numpy())
    sigma = float(s['sigma'].numpy())
    lam = float(s['lam'].numpy())
    answer = float(kl.numpy())
    tolerance = 0.1
    ...

    info = info.render(**locals())

    return info.replace(answer=answer)
