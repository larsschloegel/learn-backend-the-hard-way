def calculate_base_power(level, magic):
    return level + magic


def apply_element_bonus(base_power, element_power):
    base_power = base_power + element_power


def cast_spell(level, magic, element_power):
    total_power = apply_element_bonus(element_power, calculate_base_power(level, magic))
    return level + magic + element_power
