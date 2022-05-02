#Oliver Hugh 4/4/2022
#The functions in this file handle the logic behind the gear calculator
def calculate_center(gear_1_teeth: int, gear_2_teeth: int, dp):
    """
    This function calculates the center to center distance of 2 gears based on
    their diametric pitch and the number of teeth in the gears
    :param gear_1_teeth: number of teeth in gear 1
    :param gear_2_teeth: number of teeth in gear 2
    :param dp: diametric pitch of the 2 gears (same for both)
        (diametric pitch is the number of gears per inch)
    :return: the center distance
    """
    pitch_diameter_1 = calculate_pitch_diameter(gear_1_teeth, dp)
    pitch_diameter_2 = calculate_pitch_diameter(gear_2_teeth, dp)
    center_to_center = (pitch_diameter_2 + pitch_diameter_1)/2
    return float("{:.3f}".format(center_to_center))


def calculate_pitch_diameter(num_teeth: int, diametric_pitch):
    """
    This function calculates the pitch diameter (D) from
    a gear's number of teeth (N) and diametric pitch (P) using the
    formula D = N/P
    :param num_teeth: number of teeth of gear
    :param diametric_pitch: diametric pitch of the gear
    :return: float of the pitch diameter
    """
    return num_teeth / diametric_pitch
