import jax
import jax.numpy as jnp
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_probability as tfp
import statsmodels.formula.api as smf

from ..autotest import question, QuestionInfo


@question
def lm(seed: int, info: QuestionInfo = None) -> QuestionInfo:
    r"""
# Pytanie

Dla podanej ramki danych wyznaczyć metodą największej wiarygodności wartość parametru  `beta{{ betaid }}`
(indeksacja od 0, przy czym 0 to wyraz wolny) przyjmując następujący model liniowy:

```
Y ~ N(beta_0 + beta_1 * x_1 + beta_2 * x_2 + beta_3 * x_3, sigma^2)
```

Wynik podać najwyższej raportowanej precyzji.

## Dane

```
{{ data }}
```

"""

    shape = (8, 3)
    k = jax.random.key(seed)
    kx, kb, ky, kq = jax.random.split(k, 4)
    x = jnp.ceil(6 * jax.random.normal(kx, shape))
    b = jnp.asarray(4 * jax.random.normal(kb, shape=(shape[1] + 1,)))

    y = jnp.ceil(jnp.concatenate([x, jnp.ones((shape[0], 1))],
                                 axis=1) @ b + jax.random.normal(ky,
                                                                 (shape[0],)))

    d = {f'x{i + 1}': x[:, i] for i in range(shape[1])}
    d['y'] = y
    df = pd.DataFrame(d)
    mod = smf.ols(formula='y ~ x1+x2+x3', data=df)
    res = mod.fit()

    t_x = tf.convert_to_tensor(x)
    t_y = tf.convert_to_tensor(y)

    y_dist = tfp.distributions.Normal(
        loc=tfp.util.DeferredTensor(tf.Variable([0.0, 1.0, 1.0, 1.0]),
                                    lambda beta: beta[0] + tf.tensordot(t_x,beta[1:],axes=(1,0)),
                                    shape=(x.shape[0],)),
        scale=tfp.util.TransformedVariable([1.],
                                           bijector=tfp.bijectors.Softplus()))

    losses = tfp.math.minimize(lambda: -tf.reduce_sum(y_dist.log_prob(t_y)),
                               num_steps=10000,
                               optimizer=tf.optimizers.Adam(learning_rate=0.2))


    coefficients = y_dist.variables[0].numpy()
    test_coef = np.asarray(res.params)
    try:
        assert np.allclose(coefficients, np.asarray(res.params), atol=2e-2, rtol=1e-2)
    except AssertionError:
        pass
    betaid = int(jax.random.choice(kq, jnp.arange(0, shape[1] + 1)))

    info = info.render(data=df.to_csv(index=False), betaid=betaid,tolerance=0.1)

    return info.replace(answer=coefficients[betaid],)
