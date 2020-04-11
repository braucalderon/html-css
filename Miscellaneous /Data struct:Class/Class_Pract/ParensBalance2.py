# parensBalance2.py

from Stack import Stack

def parensBalance2(s):
    stack = Stack()
    for ch in s:
        if ch in "([{":      # push an opening marker
            stack.push(ch)
        elif ch in ")]}":    # match closing with top of stack
            if stack.size() < 1: # no pending open to match it
               return False
            else:
               opener = stack.pop()
               if opener+ch not in ["()", "[]", "{}"]:
                   # not a matching pair
                   return False
    return stack.size() == 0 # empty stack means everything matched up
