import re

def parse_array_declaration(desc):
    # Define the regular expressions for parsing
    array_definition = re.compile(r'(?P<array_name>[A-Z][A-Z0-9]*)\s*:\s*array\s*\[\s*(?P<dimensions>.+?)\s*\]\s*of\s*(?P<type>integer|char|real|bool)\s*;')
    bounds = re.compile(r'(?P<lower_bound>\d+)\s*\.\.\s*(?P<upper_bound>\d+)')

    # Mach the array declaration pattern
    match = array_definition.match(desc)
    if not match:
        return None

    array_name = match.group('array_name')
    type_name = match.group('type')
    dimensions_str = match.group('dimensions')

    # Parse dimensions
    dimensions = []
    for dimension_str in re.split(r'\s*,\s*', dimensions_str):
        bounds_match = bounds.match(dimension_str)
        if not bounds_match:
            return None

        lower_bound = bounds_match.group('lower_bound')
        upper_bound = bounds_match.group('upper_bound')
        dimensions.append([lower_bound, upper_bound])

    # Determine if the array is one-dimensional or multidimensional
    dimenCount = len(dimensions)
    array_name  = "One-dimensional array" if dimenCount == 1  else "Multidimensional array"

    # Compile-time descriptor fields
    descriptor = [
        array_name ,
        type_name ,
        "Integer",  # Index type field
        str(dimenCount),
        dimensions,
        "1000"  # Address field
    ]

    return descriptor

# Get array declaration input from the user
array_declaration = input("Enter the array declaration: ")

# Parse and print the compile-time descriptor
descriptor = parse_array_declaration(array_declaration)
if descriptor:
    print(descriptor)
else:
    print("Invalid array declaration.")




