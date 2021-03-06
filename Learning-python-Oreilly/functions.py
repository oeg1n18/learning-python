#============ Function basics ======================
# return sends a rest object back to the caller
# yield sends a result object back to the caller, but remembers 
# where it left of 
# nonlocal declares enclosing function variables that are to be assigned
#Arguments are passed by assignment (object reference)

import Statements #equivalent of include in c++
#if the module is treated as an object and you can access variables form is 
# using modulename.variablename syntax
# import module code will only be executed once. if you wish to re-run it 
# you must use reload
from imp import reload #actually import the reload 
reload(Statements)

""" Module statements run on the first import. 
    Top-level assignments create module attributes e.g. the imported module becomes
    a namespace and the import name an object.
"""


def name(arg1, arg2): 
    print('im a function and my args are', arg1, arg2)

def returnfunc(arg1):
    print('i am a returning function')
    return (arg1 + 1)
"""
func(value) Normal argument: matched by postition 
func(name=value) Keyword argument: matched by name
func(*iterable) pass all objects in iterable as individual positional arguments 
e.g. arg1, arge2, arg3

def func(name) Normal argument:matches any passed value by position or name
def func(name=value) Default argument value, if not passed in the call
def func(*name) Matches and collects remaining positional argumetns in a tuple
def func(**name) Matches and collects remaining keyword arguments in a dictionary
def func(*other, name) Arguments that must be passed by keyword only in calls
def func(*, name=value) Arguments that must be passed by keyword only in calls
"""
