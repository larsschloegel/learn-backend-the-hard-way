Deleting Dictionary Values
You can delete existing keys using the del keyword.

```python
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}
```

Deleting Keys That Don't Exist
Notice that if you try to delete a key that doesn't exist, you'll get an error.

```python
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["unknown"]
# ERROR HERE, key doesn't exist
```

# Fragen
What happens if you try to 'del' a key that doesn't exist in the dictionary?


The existing value is returned

Nothing

Error (richtig)