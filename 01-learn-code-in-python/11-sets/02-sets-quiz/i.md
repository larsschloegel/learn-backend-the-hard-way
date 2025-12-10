Sets Quiz
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

```python
fruits = {"apple", "banana", "grape"}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}
```

Add Values

```python
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}
```

No error will be raised if you add an item already in the set, and the set will remain unchanged.
Empty Set
Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

```python
fruits = set()
fruits.add("pear")
print(fruits)
# Prints: {'pear'}
```

Iterate Over Values in a Set (Order Is Not Guaranteed)

```python
fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
```

Removing Values
```python
fruits = {"apple", "banana", "grape"}
fruits.remove("apple")
print(fruits)
# Prints: {'banana', 'grape'}
```

## Fragen
How do I remove an item from a set?


my_set.remove("item") -> richtig

my_set.del("item")

delete my_set["item"]

del my_set["item"]