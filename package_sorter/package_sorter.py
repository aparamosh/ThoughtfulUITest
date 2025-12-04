
STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"


def _check_number(name, value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be > 0")


def sort(length, width, height, mass):
    """Decide package category.

    Returns one of STANDARD, SPECIAL or REJECTED.
    """
    # type and value validation
    _check_number("length", length)
    _check_number("width", width)
    _check_number("height", height)
    _check_number("mass", mass)

    # rejection by mass
    if mass > 20:
        return REJECTED

    volume = length * width * height

    # bulky by volume
    if volume >= 1_000_000:
        return SPECIAL

    return STANDARD
# package_sorter/sorter.py

STANDARD = "STANDARD"
SPECIAL = "SPECIAL"
REJECTED = "REJECTED"


def sort(width, height, length, mass):
    # Validate inputs
    for name, value in {
        "width": width,
        "height": height,
        "length": length,
        "mass": mass,
    }.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value <= 0:
            raise ValueError(f"{name} must be a positive value")

    # Determine bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Determine heavy
    is_heavy = mass >= 20

    # Classification
    if is_bulky and is_heavy:
        return REJECTED
    elif is_bulky or is_heavy:
        return SPECIAL
    else:
        return STANDARD
