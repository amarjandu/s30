import math


class Calculations:
    @classmethod
    def tire_circumference(cls,
                           tread_width: int,
                           aspect_ratio: int,
                           wheel_diameter: int) -> float:
        """
        225/50/r16
        :param tread_width: 225
        :param aspect_ratio: 50
        :param wheel_diameter: 16
        :return: 78.1
        """
        wall_height = (tread_width * (aspect_ratio / 100) * 2) / 25.4
        return wall_height + wheel_diameter

    @classmethod
    def mph_by_rpm(cls,
                   rpm: int,
                   tire_circumference: int,
                   final_drive_ratio: float,
                   gear_ratio: float) -> float:
        """
        :param rpm: desired RPM
        :param tire_circumference: in inches 
        :param final_drive_ratio: from the differential
        :param gear_ratio: gear ratio currently selected 
        :return: miles per hour
        """

        return (rpm * tire_circumference) / (final_drive_ratio * gear_ratio * 1056)
