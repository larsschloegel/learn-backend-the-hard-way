Quest Status
Fantasy Quest stores each character's progress in a nested dictionary structure. Here's what it looks like:

```python
{
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {
            "status": "In Progress",
        },
        "talk_to_syl": {
            "status": "Completed",
        },
    },
}
```

The values can change of course, but the structure will always be the same. For example, another character's progress might look like this:

```python
{
    "character_name": "Shallan",
    "quests": {
        "bridge_run": {
            "status": "Completed",
        },
        "talk_to_syl": {
            "status": "In Progress",
        },
    },
}
```

Assignment
Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and returns the character's status in the "bridge_run" quest.

Note, you can chain dictionary keys to access a dictionary inside another dictionary:

```python
outer_dictionary["outer_key"]["inner_key"]
```