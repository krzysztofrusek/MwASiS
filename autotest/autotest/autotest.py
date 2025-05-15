import dataclasses
import os
from dataclasses import dataclass
from functools import wraps
from typing import Callable

import numpy as np
from jinja2 import Environment, select_autoescape, PackageLoader


@dataclass
class QuestionInfo:
    name: str
    text: str
    answer: float
    tolerance: float = dataclasses.field(default=0.1)

    replace = dataclasses.replace

    def render(self, **kwargs):
        env = Environment()
        t = env.from_string(self.text)
        txt = t.render(**kwargs)
        return self.replace(text=txt)


def question(f):
    info = QuestionInfo(name=f.__name__, text=f.__doc__, answer=np.nan)

    @wraps(f)
    def wrapper(*args, **kwds):
        return f(*args, **kwds, info=info)

    return wrapper

def gen_quiz(test_fn: Callable, output: str, n: int):
    if os.path.exists(output):
        return
    env = Environment(loader=PackageLoader('autotest'),
        autoescape=select_autoescape())

    dotpos = test_fn.__module__.rfind('.')
    category = test_fn.__module__[dotpos + 1:]

    template = env.get_template("quiz.xml")
    quiz = template.render(category=category,
                           questions=[test_fn(i) for i in range(n)])

    with open(output, 'wt') as f:
        f.write(quiz)