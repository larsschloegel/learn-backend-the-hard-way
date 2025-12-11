Raising Exceptions Review
As you've noticed, there are many types of exceptions. Many specific exceptions are built into the language like IndexError and ZeroDivisionError, and (almost) all Exceptions count as the parent Exception type. What differentiates exceptions are their types, not their string descriptions. This is important to know when handling errors from imported modules.

If you're interested in the official documentation on all the built-in exceptions you can find a list here.

Refer to the Following Code for the Question
```python
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
```

## Frage
In the code sample, what will happen?


The program will crash with an uncaught exception (richtig)

It will print 'zero'