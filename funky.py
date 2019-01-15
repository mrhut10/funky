# generic fancy Function's
# trying to loosely follow principles of functional programming paradigm and Category theory within Math

# function -> function
def curry(fun:"function"):
  """
    implementation of a curry/currying function
    visit https://en.wikipedia.org/wiki/Currying for more information
  """
  def curried(*args, **kwargs):
    if len(args) + len(kwargs) >= fun.__code__.co_argcount:
      return fun(*args, **kwargs)
    return lambda *args2, **kwargs2: curried(*(args + args2), **dict(kwargs, **kwargs2))
  return curried


# function function -> function
def compose (*functions):
  """
  implementation of the compose / composition function for uniary functions (uni-ary as in 1 input variable)
  visit https://en.wikipedia.org/wiki/Function_composition_(computer_science)
  took me ages to get this to work for more than two functions
  """
  def composed(arg=None): # function that will be returned
    for f in reversed(functions):
      arg = f(arg)
    return arg
  return composed

#function -> [iterable] -> [iterable]
# will run a function over all elements and return result
map = lambda f, a: [f(x) for x in a] 


# idenity function visit https://en.wikipedia.org/wiki/Identity_function
# a -> a
idenity = lambda a : a


# a -> b -> bool
# will return true is a & b are equal
equal = curry(lambda a, b : a == b)

# fn1 -> fn2 -> a -> bool
equalfn = curry(lambda fn1,fn2,value: fn1(value)==fn2(value))

logicalNot = lambda a : (not a)
logicalOr = curry(lambda fn1, fn2, value: fn1(value) or fn2(value))
logicaland = curry(lambda fn1, fn2, value: all((fn1(value),fn2(value))))

str_lower = lambda value: value.lower()

gt = curry(lambda a,b: b > a)
lt = curry(lambda a,b: b < a)
et = curry(lambda a,b: a==b)

# String -> a
# will pull the property of an object
prop = curry(lambda prop, x: x[prop])

