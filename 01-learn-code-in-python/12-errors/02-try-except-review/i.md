Try/Except Review
```python
try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"
```

The try block is executed until an exception is raised or it completes, whichever happens first. In this case, a "divide by zero" error is raised because division by zero is impossible. The except block is only executed if an exception is raised in the try block. It then exposes the exception as data (e in our case) so that the program can handle the exception gracefully without crashing.

## Fragen

If no exceptions are raised in the try block...


...the program crashes

...the except block won't execute (richtig)

...the except block executes with a 'None' exception

...a 'no exception' error is raised