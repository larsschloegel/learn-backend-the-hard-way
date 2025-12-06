def calculate_experience_points(level):
    pass


# solution
def calculate_experience_points(level):
    total_xp = 0
    for current_level in range(1, level):
        total_xp += current_level * 5
    return total_xp