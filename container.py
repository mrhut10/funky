## import functional tools needed ( made for project )
from funky import curry



class container():
  """
    container it my implementation of a functor see https://en.wikipedia.org/wiki/Functor
  """
  ## internal State
  #   avoid accessing directly, good practise to use .map methods to do work on value, or mapContainer to pull out value.
  value = None
  
  ## container methods / functions
  #  value -> container(value)
  def __init__(self, *args):
    """will set value to the first argument"""
    self.value = args[0]
  # value -> container(value)
  def of(self, value):
    """returns new container with new value"""
    return container(value)
  #  function -> {value}
  def map(self, fun: "function"):
    """will run mapContainer over self and return it within a new container"""
    return self.of(mapContainer(fun,self))

# function -> container -> a
# this will run a function over a containers value
# often used to pull out a value out of a container safely
mapContainer = curry(lambda f, a: f(a.value))



class TestClass(object):
  commonTestCases = ['hello',True,False,3,-1,3.3,-3.3,None,[1,2,3]]
  def test_container__init__(self):
    testcases = self.commonTestCases
    for t in testcases:
      assert container(t).value == t
  def test_container_of(self):
    testcases = self.commonTestCases
    a = container(None)
    for t in testcases:
      b = a.of(t)
      assert isinstance(b,container)
      assert b.value == t
  def test_mapContainer(self):
    testcases = self.commonTestCases
    for t in testcases:
      firstContaienr = container(t)
      workedValue = mapContainer(lambda a:[a,a], firstContaienr)
      assert workedValue == [t,t]
  def test_container_map(self):
    testcases = self.commonTestCases
    fun = lambda a: [a,a]
    for t in testcases:
      firstContainer = container(t)
      workedContainer = firstContainer.map(fun)
      assert isinstance(workedContainer,container)
      assert workedContainer.value == [t,t]
  