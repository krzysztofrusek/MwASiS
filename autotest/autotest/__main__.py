from autotest.questions.masis_bayes import bayes
from autotest.questions.masis_bayes2 import bayesconjugate
from autotest.questions.masis_mle import fitmle
from autotest.questions.masis_normal import normalny

from autotest.autotest import gen_quiz

gen_quiz(normalny, "masis_normalny.xml", 64)
gen_quiz(fitmle, "masis_fitmle.xml", 64)
gen_quiz(bayes,"masis_bayes.xml", 64)
# gen_quiz(bayesconjugate,"masis_bayesconjugate.xml", 64)

...
