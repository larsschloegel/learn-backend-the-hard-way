Set Subtraction
You can use some of the "normal" mathematical operations on sets. For example, you can subtract one set from another. It removes all the values in the second set from the first set.

```python
set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2

print(set3)
# Prints: {'grape'}
```

Assignment
Complete the find_missing_ids function. It accepts two lists as input, and returns a new set of all the IDs that are in the first list but are not in the second.

Naturally, there will be no duplicates in the resulting set.

Tips
You can convert a List to a Set using the set() function.
You can subtract the elements in one Set from another Set using the - operator.