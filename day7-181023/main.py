# import module as test

# print(test.calculate(10, 5))
# print(test.testVar)
# test.Trial('Derta')

# import pkgmodule.module1 as greeting

# greeting.test()

import sys
sys.path.append('/mnt/e/code/day6/pkgmodule/')

# Now, you can import the module
import module1 as greeting

greeting.test()


class Classification:
    def __init__(self, )