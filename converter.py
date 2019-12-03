# encoding: utf-8
"""
Program that converts from WGS84 to L-Est97 coordinate system and vice versa.

:author: Sigrid Närep
"""
from pyproj import Proj
import math
import sys

# Check which python version is being used in order to import tkinter
if sys.version_info.major == 2:
    import Tkinter as Tk
else:
    import tkinter as Tk


class CoordinateConverter:
    """
    Coordinate Converter from WGS84 to L-Est97 coordinate system and vice versa using PyProj.
    """
    def __init__(self):
        pass

    EPSG3301 = Proj(init="EPSG:3301")

    @staticmethod
    def l_est97to_wgs_84(x_input_value, y_input_value):
        """
        Converting user input from l_est97 to wgs_84, and forwarding results to UI.

        :param x_input_value: in l_est97 format
        :param y_input_value: in l_est97 format
        :return: converted longitude and latitude values
        """
        CoordinateValidator.validate_user_input_is_valid(x_input_value)
        CoordinateValidator.validate_user_input_is_valid(y_input_value)

        x_value = float(x_input_value)
        y_value = float(y_input_value)

        wgs_84_longitude, wgs_84_latitude = CoordinateConverter.EPSG3301(y_value, x_value, inverse=True)

        CoordinateValidator.l_est97_validate_user_input_in_bounds(True, wgs_84_longitude)
        CoordinateValidator.l_est97_validate_user_input_in_bounds(False, wgs_84_latitude)

        longitude_degree, longitude_minute, longitude_second = \
            DecimalDegreeConverter.decimal_to_degrees(wgs_84_longitude)
        latitude_degree, latitude_minute, latitude_second = \
            DecimalDegreeConverter.decimal_to_degrees(wgs_84_latitude)

        longitude_in_degrees = \
            DecimalDegreeConverter.format_degrees(True, longitude_degree, longitude_minute, longitude_second)
        latitude_in_degrees = \
            DecimalDegreeConverter.format_degrees(False, latitude_degree, latitude_minute, latitude_second)

        Tk.Label(main, text=latitude_in_degrees).grid(row=0, column=3, padx=0, pady=10)
        Tk.Label(main, text=longitude_in_degrees).grid(row=1, column=3, padx=0, pady=10)
        return wgs_84_longitude, wgs_84_latitude

    @staticmethod
    def wgs_84to_l_est97(x_input_value, y_input_value):
        """
        Converting user input from wgs_84 to l_est97, and forwarding results to UI.

        :param x_input_value: in wgs_84 format
        :param y_input_value: in wgs_84 format
        :return: converted longitude and latitude values
        """
        CoordinateValidator.validate_user_input_is_valid(x_input_value)
        CoordinateValidator.validate_user_input_is_valid(y_input_value)
        CoordinateValidator.wgs_84_validate_user_input_in_bounds(True, x_input_value)
        CoordinateValidator.wgs_84_validate_user_input_in_bounds(False, y_input_value)

        x_value = float(x_input_value)
        y_value = float(y_input_value)

        l_est97_latitude, l_est97_longitude = CoordinateConverter.EPSG3301(x_value, y_value)

        Tk.Label(main, text=l_est97_latitude).grid(row=3, column=3, padx=0, pady=10)
        Tk.Label(main, text=l_est97_longitude).grid(row=4, column=3, padx=0, pady=10)
        return l_est97_latitude, l_est97_longitude


class CoordinateValidator(object):
    """
    Validates that coordinates are in given bounds and user input is valid.
    """
    @staticmethod
    def validate_user_input_is_valid(input_value):
        """
        Check whether user input is valid - if it is a string or left empty,
        catch exception and notify user through UI label.

        :param input_value:
        :return: bool is it a valid input
        """
        is_valid = True

        try:
            value = float(input_value)
        except ValueError:
            is_valid = False
            Tk.Label(main, text='Your input ' + input_value + ' was not valid because you entered letters '
                                                              'instead of numbers or left the input blank, try again!',
                     fg="red").grid(row=6, column=1, padx=50, pady=20)
            return is_valid

        return is_valid

    @staticmethod
    def wgs_84_validate_user_input_in_bounds(is_longitude, input_value):
        """
        Check whether user WGS_84 input is in  bounds, catch exception and notify user through UI label.

        :param is_longitude: if longitude, then min ja max valued different from latitude
        :param input_value: user input long or lat
        :return: bool whether input in bounds
        """

        in_bounds = True
        if is_longitude:
            if float(input_value) < -180 or float(input_value) > 180:
                in_bounds = False
                Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
                    .grid(row=7, column=1, padx=50, pady=20)
                return in_bounds
        else:
            if float(input_value) < -90 or float(input_value) > 90:
                in_bounds = False
                Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
                    .grid(row=7, column=1, padx=50, pady=20)
                return in_bounds

        return in_bounds

    @staticmethod
    def l_est97_validate_user_input_in_bounds(is_longitude, input_value):
        """
        Validate whether L_EST97 user input value is between allowed bounds

        :param is_longitude: if longitude, then min ja max valued different from latitude
        :param input_value: user input long or lat
        :return:
        """

        in_bounds = True

        if is_longitude:
            if float(input_value) < 21.84 or float(input_value) > 28:
                in_bounds = False
                Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
                    .grid(row=7, column=1, padx=50, pady=20)
                return in_bounds
        else:
            if float(input_value) < 57.57 or float(input_value) > 59.7:
                in_bounds = False
                Tk.Label(main, text='Your input ' + str(input_value) + ' is out of bounds!', fg="red")\
                    .grid(row=7, column=1, padx=50, pady=20)
                return in_bounds
        return in_bounds


class DecimalDegreeConverter:
    """
    Convert decimals into degrees and vice versa.
    """

    def __init__(self):
        pass

    @staticmethod
    def decimal_to_degrees(decimal_degree):
        """
        Converting decimal longitude and latitude values into degrees minutes and seconds.

        :param decimal_degree: longitude or latitude
        :return:  longitude and latitude degrees minutes and seconds in string format
        """

        # math.modf() splits whole number and decimal into tuple
        # eg 53.3478 becomes (0.3478, 53)
        split_degx = math.modf(decimal_degree)

        # the whole number [index 1] is the degrees
        degrees = int(split_degx[1])

        # multiply the decimal part by 60: 0.3478 * 60 = 20.868
        # split the whole number part of the total as the minutes: 20
        # abs() absoulte value - no negative
        minutes = abs(int(math.modf(split_degx[0] * 60)[1]))

        # multiply the decimal part of the split above by 60 to get the seconds
        # 0.868 x 60 = 52.08, round excess decimal places to 2 places
        # abs() absoulte value - no negative
        seconds = abs(round(math.modf(split_degx[0] * 60)[0] * 60, 2))

        # abs() remove negative from degrees, was only needed for if-else above
        return degrees, minutes, seconds

    @staticmethod
    def degrees_to_decimal(degrees, minutes, seconds):
        """
        Converting coordinates degree, minutes and seconds to decimal

        :param degrees:
        :param minutes:
        :param seconds:
        :return: the decimal value
        """

        return round(degrees + minutes / 60. + seconds / 3600., 3)

    @staticmethod
    def format_degrees(is_longitude, degrees, minutes, seconds):
        if is_longitude:
            if degrees < 0:
                e_or_w = "W"
            else:
                e_or_w = "E"

            return str(abs(degrees)) + "° " + str(minutes) + "' " + str(seconds) + "\" " + e_or_w
        else:
            if degrees < 0:
                n_or_s = "S"
            else:
                n_or_s = "N"

            # abs() remove negative from degrees, was only needed for if-else above
            return str(abs(degrees)) + "° " + str(minutes) + "' " + str(seconds) + "\" " + n_or_s


# GUI for getting user input

main = Tk.Tk()
main.title("L_Est97 <-- CONVERTER --> WGS_84")
main.geometry('1200x700')

L_Est97x = Tk.StringVar()
L_Est97y = Tk.StringVar()

WGS_84x = Tk.StringVar()
WGS_84y = Tk.StringVar()


L_Est97xLabel = Tk.Label(main, text='Enter L_Est X value:').grid(row=0, column=0, padx=50, pady=30)
L_Est97xEntry = Tk.Entry(main, textvariable=L_Est97x).grid(row=0, column=1)

L_Est97yLabel = Tk.Label(main, text='Enter L_Est Y value:').grid(row=1, column=0, padx=50, pady=10)
L_Est97yEntry = Tk.Entry(main, textvariable=L_Est97y).grid(row=1, column=1)

L_Est97xPrint = Tk.Label(main, text='X in degrees and minutes:').grid(row=0, column=2, padx=50, pady=20)
L_Est97yPrint = Tk.Label(main, text='Y in degrees and minutes:').grid(row=1, column=2, padx=50, pady=20)

L_Est97btn = Tk.Button(main, text='L_Est97 to WGS_84', command=lambda: CoordinateConverter
                       .l_est97to_wgs_84(L_Est97x.get(), L_Est97y.get())).grid(row=2, column=1, padx=0, pady=50)

WGS_84xLabel = Tk.Label(main, text='Enter WGS_84 X value:').grid(row=3, column=0, padx=50, pady=30)
WGS_84xEntry = Tk.Entry(main, textvariable=WGS_84x).grid(row=3, column=1)

WGS_84yLabel = Tk.Label(main, text='Enter WGS_84 Y value:').grid(row=4, column=0, padx=50, pady=10)
WGS_84yEntry = Tk.Entry(main, textvariable=WGS_84y).grid(row=4, column=1)

WGS_84xPrint = Tk.Label(main, text='X:').grid(row=3, column=2, padx=50, pady=20)
WGS_84yPrint = Tk.Label(main, text='Y:').grid(row=4, column=2, padx=50, pady=20)

WGS_84ybtn = Tk.Button(main, text='WGS_84 to L_Est97', command=lambda: CoordinateConverter
                       .wgs_84to_l_est97(WGS_84x.get(), WGS_84y.get())).grid(row=5, column=1, padx=0, pady=50)

main.mainloop()
