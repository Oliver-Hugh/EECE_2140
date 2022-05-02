#Oliver Hugh 4/1/2022
import math

#The functions in this file handle the logic for the unit convertor

# list of equivalent values for [seconds, minutes, hours, days]
time_constants = [3600, 60, 1, 1 / 24]
# list of their corresponding unit names
time_units = ['sec', 'min', 'hours', 'days']
# list of equivalent values for [inch, feet, yards, mile, mm, cm, m, km]
distance_constants = [39.37, 3.28, 1.09, .00062137, 1000, 100, 1, .001]
# list of their corresponding unit names
distance_units = ['inch', 'feet', 'yards', 'mile', 'mm', 'cm', 'm', 'km']
# list of orders of magnitude for [nano, micro, milli, centi, base, kilo, mega, giga]
prefix_constants = [-9, -6, -3, -2, 0, 3, 6, 9]
# list of their corresponding unit names
prefix_units = ['nano', 'micro', 'milli', 'centi', 'base', 'kilo', 'mega', 'giga']
# list of equivalent values for [radians, degrees]
angle_constants = [360, 2 * math.pi]
# list of their corresponding unit names
angle_units = ['degrees', 'radians']
# list of equivalent values for [oz, lb, ton, kg, g]
w_m_constants = [16, 1, .0005, .4536, 453.6]
# list of their corresponding unit names
w_m_units = ['oz', 'lb', 'ton', 'kg']


def conversion(type_to_convert, orig_unit, converted_unit, value_to_convert):
    """
    this function takes the type of conversion that will be happening
    :param type_to_convert: the type of conversion that will happen
    :param value_to_convert: the value the user would like to convert
    :param orig_unit: the unit of the initial value
    :param converted_unit: the desired unit the value user would like to convert to
    :return: the initial value converted to the correct units
    """
    #make variable names easier to use
    t = type_to_convert
    if t == "Time":
        converted_value = time_conversion(orig_unit, converted_unit, value_to_convert)
    elif t == 'Distance':
        converted_value = distance_conversion(orig_unit, converted_unit, value_to_convert)
    elif t == 'Weight/Mass':
        converted_value = weight_mass_conversion(orig_unit, converted_unit, value_to_convert)
    elif t == 'Angle':
        converted_value = angle_conversion(orig_unit, converted_unit, value_to_convert)
    elif t == 'Metric Prefixes':
        converted_value = prefix_conversion(orig_unit, converted_unit, value_to_convert)
    else:
        converted_value = '-'
    converted_value = float(converted_value)
    return float("{:.5f}".format(converted_value))


def time_conversion(original_unit, new_unit, original_value):
    """
    This function converts between 2 units of time
    :param original_unit: the original unit that needs to be converted
    :param new_unit: what unit the original value should be converted to
    :param original_value: the value that needs to be converted
    :return: what the equivalent of the original value is in terms of the new unit
    """
    #set defaults so that you can raise error later
    original_unit_index = -1
    new_unit_index = -1
    for i in range(len(time_units)):
        if original_unit == time_units[i]:
            original_unit_index = i
        if new_unit == time_units[i]:
            new_unit_index = i
    if original_unit_index == -1 or new_unit_index == -1:
        raise Exception("Unknown time units used")
    new_value = (original_value/time_constants[original_unit_index])*time_constants[new_unit_index]
    return new_value


def distance_conversion(original_unit, new_unit, original_value):
    """
    This function converts between 2 units of distance
    :param original_unit: the original unit that needs to be converted
    :param new_unit: what unit the original value should be converted to
    :param original_value: the value that needs to be converted
    :return: what the equivalent of the original value is in terms of the new unit
    """
    # set defaults so that you can raise error later
    original_unit_index = -1
    new_unit_index = -1
    for i in range(len(distance_units)):
        if original_unit == distance_units[i]:
            original_unit_index = i
        if new_unit == distance_units[i]:
            new_unit_index = i
    if original_unit_index == -1 or new_unit_index == -1:
        raise Exception("Unknown distance units used")
    new_value = (original_value / distance_constants[original_unit_index]) * distance_constants[new_unit_index]
    return new_value


def weight_mass_conversion(original_unit, new_unit, original_value):
    """
    This function converts between 2 units of weight/mass
    :param original_unit: the original unit that needs to be converted
    :param new_unit: what unit the original value should be converted to
    :param original_value: the value that needs to be converted
    :return: what the equivalent of the original value is in terms of the new unit
    """
    # set defaults so that you can raise error later
    original_unit_index = -1
    new_unit_index = -1
    for i in range(len(w_m_units)):
        if original_unit == w_m_units[i]:
            original_unit_index = i
        if new_unit == w_m_units[i]:
            new_unit_index = i
    if original_unit_index == -1 or new_unit_index == -1:
        raise Exception("Unknown time units used")
    new_value = (original_value / w_m_constants[original_unit_index]) * w_m_constants[new_unit_index]
    return new_value


def angle_conversion(original_unit, new_unit, original_value):
    """
    This function converts between 2 units of angular displacement
    :param original_unit: the original unit that needs to be converted
    :param new_unit: what unit the original value should be converted to
    :param original_value: the value that needs to be converted
    :return: what the equivalent of the original value is in terms of the new unit
    """
    #set defaults so that you can raise error later
    original_unit_index = -1
    new_unit_index = -1
    for i in range(len(angle_units)):
        if original_unit == angle_units[i]:
            original_unit_index = i
        if new_unit == angle_units[i]:
            new_unit_index = i
    if original_unit_index == -1 or new_unit_index == -1:
        raise Exception("Unknown time units used")
    new_value = (original_value/angle_constants[original_unit_index])*angle_constants[new_unit_index]
    return new_value


def prefix_conversion(original_unit, new_unit, original_value):
    """
     This function converts between 2 generic metric units/ 2 different prefixes
     :param original_unit: the original unit that needs to be converted
     :param new_unit: what unit the original value should be converted to
     :param original_value: the value that needs to be converted
     :return: what the equivalent of the original value is in terms of the new unit
     """
    # set defaults so that you can raise error later
    original_unit_index = -1
    new_unit_index = -1
    for i in range(len(prefix_units)):
        if original_unit == prefix_units[i]:
            original_unit_index = i
        if new_unit == prefix_units[i]:
            new_unit_index = i
    if original_unit_index == -1 or new_unit_index == -1:
        raise Exception("Unknown time units used")
    new_value = (original_value / (10**prefix_constants[new_unit_index])) * (10**prefix_constants[original_unit_index])
    return new_value


def get_unit_list(type_to_convert):
    """
    This function gets the proper list of units that needs to be displayed based on the conversion type
    :param type_to_convert: Either "Time", "Distance", "Weight/Mass", "Angle", or "Metric Prefixes".
    :return: None
    """
    t = type_to_convert
    if t == "Time":
        return ['sec', 'min', 'hours', 'days']
    elif t == 'Distance':
        return ['inch', 'feet', 'yards', 'mile', 'mm', 'cm', 'm', 'km']
    elif t == 'Weight/Mass':
        return ['oz', 'lb', 'ton', 'kg']
    elif t == 'Angle':
        return ['degrees', 'radians']
    elif t == 'Metric Prefixes':
        return ['nano', 'micro', 'milli', 'centi', 'base', 'kilo', 'mega', 'giga']
    else:
        raise ValueError("Improper input passed to function")
