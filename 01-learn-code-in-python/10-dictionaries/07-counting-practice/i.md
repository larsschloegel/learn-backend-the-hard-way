Counting Practice
Checking for Existence
If you're unsure whether a key exists in a dictionary, use the in keyword.

```python
cars = {
    "ford": "f150",
    "toyota": "camry"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False
```

Assignment
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Fix the count_enemies function. It accepts as input:

enemy_names: a list of strings.
It should return a dictionary where:

The keys are all the enemy names from the list
The values are the counts of how many times each enemy appeared in the list.
Run the code in its current state. It will raise a KeyError.
Fix the code by checking if a key is in the dictionary before trying to update its value. If it isn't, set it to 1.