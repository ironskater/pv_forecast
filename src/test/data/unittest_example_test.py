import main.data.unittest_example as ut

def testIncrement_Normal():
    assert ut.increment(3) == 4

def testDecrement_Normal():
    assert ut.decrement(3) == 2
