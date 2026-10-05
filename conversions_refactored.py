class ConversionNotPossibleException(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperature_units = ["C", "F", "K"]
    distance_units = ["M", "Y", "MI"]

    fromUnit = fromUnit.upper()
    toUnit = toUnit.upper()

    # Temperature conversions
    if fromUnit in temperature_units and toUnit in temperature_units:

        # Same unit
        if fromUnit == toUnit:
            return float(value)

        # Celsius to Fahrenheit
        if fromUnit == "C" and toUnit == "F":
            return float((value * 9.0 / 5.0) + 32.0)

        # Celsius to Kelvin
        if fromUnit == "C" and toUnit == "K":
            return float(value + 273.15)

        # Fahrenheit to Celsius
        if fromUnit == "F" and toUnit == "C":
            return float((value - 32.0) * 5.0 / 9.0)

        # Fahrenheit to Kelvin
        if fromUnit == "F" and toUnit == "K":
            return float(((value - 32.0) * 5.0 / 9.0) + 273.15)

        # Kelvin to Celsius
        if fromUnit == "K" and toUnit == "C":
            return float(value - 273.15)

        # Kelvin to Fahrenheit
        if fromUnit == "K" and toUnit == "F":
            return float(((value - 273.15) * 9.0 / 5.0) + 32.0)

    # Distance conversions
    if fromUnit in distance_units and toUnit in distance_units:

        # Same unit
        if fromUnit == toUnit:
            return float(value)

        # Miles to Yards
        if fromUnit == "MI" and toUnit == "Y":
            return float(value * 1760.0)

        # Yards to Miles
        if fromUnit == "Y" and toUnit == "MI":
            return float(value / 1760.0)

        # Miles to Meters
        if fromUnit == "MI" and toUnit == "M":
            return float(value * 1609.344)

        # Meters to Miles
        if fromUnit == "M" and toUnit == "MI":
            return float(value / 1609.344)

        # Yards to Meters
        if fromUnit == "Y" and toUnit == "M":
            return float(value * 0.9144)

        # Meters to Yards
        if fromUnit == "M" and toUnit == "Y":
            return float(value / 0.9144)

    raise ConversionNotPossibleException(
        "Cannot convert from {} to {}".format(fromUnit, toUnit)
    )