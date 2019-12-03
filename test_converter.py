# encoding: utf-8
from converter import *


def test_decimal_to_degrees():
    assert DecimalDegreeConverter.decimal_to_degrees(30.56) == (30, 33, 36)
    assert DecimalDegreeConverter.decimal_to_degrees(30.429) == (30, 25, 44.4)
    assert DecimalDegreeConverter.decimal_to_degrees(50.429) == (50, 25, 44.4)


def test_degrees_to_decimal():
    assert DecimalDegreeConverter.degrees_to_decimal(30, 33, 36) == 30.560
    assert DecimalDegreeConverter.degrees_to_decimal(30, 25, 44.4) == 30.429
    assert DecimalDegreeConverter.degrees_to_decimal(50, 25, 44.4) == 50.429


def test_l_est97to_wgs_84():
    assert CoordinateConverter.l_est97to_wgs_84(6584329.4, 53769.4) == (16.18126153699928, 59.16318263878547)
    assert CoordinateConverter.l_est97to_wgs_84(6585357.3, 539175.7) == (24.689714139852164, 59.40432479193938)
    assert CoordinateConverter.l_est97to_wgs_84(6584352.8, 537699.6) == (24.663553211170424, 59.39544214334204)


def test_user_input_valid():
    assert CoordinateValidator.validate_user_input_is_valid("45.56363") is True
    assert CoordinateValidator.validate_user_input_is_valid("7") is True
    assert CoordinateValidator.validate_user_input_is_valid("dgdsh") is False
    assert CoordinateValidator.validate_user_input_is_valid("") is False
    assert CoordinateValidator.validate_user_input_is_valid("    ") is False


def test_l_est97_user_input_bounds():
    assert CoordinateValidator.l_est97_validate_user_input_in_bounds(True, 30.637) is False
    assert CoordinateValidator.l_est97_validate_user_input_in_bounds(False, 30.637) is False
    assert CoordinateValidator.l_est97_validate_user_input_in_bounds(True, 58.637) is False
    assert CoordinateValidator.l_est97_validate_user_input_in_bounds(False, 58.637) is True
    assert CoordinateValidator.l_est97_validate_user_input_in_bounds(True, 24.637) is True


def test_wgs_84_user_input_bounds():
    assert CoordinateValidator.wgs_84_validate_user_input_in_bounds(True, 170.47) is True
    assert CoordinateValidator.wgs_84_validate_user_input_in_bounds(False, 170.47) is False
    assert CoordinateValidator.wgs_84_validate_user_input_in_bounds(True, 58.637) is True
    assert CoordinateValidator.wgs_84_validate_user_input_in_bounds(False, 58.637) is True
    assert CoordinateValidator.wgs_84_validate_user_input_in_bounds(True, 190.47) is False


def test_wgs_84to_l_est97():
    assert CoordinateConverter.wgs_84to_l_est97(59.355, 24.4343) == (4472526.15192621, 3569554.3156291693)
    assert CoordinateConverter.wgs_84to_l_est97(59.355, 24.4343) == (4472526.15192621, 3569554.3156291693)
    assert CoordinateConverter.wgs_84to_l_est97(59.355, 24.4343) == (4472526.15192621, 3569554.3156291693)


def test_format_degrees():
    assert DecimalDegreeConverter.format_degrees(True, 11, 22, 33) == "11° 22' 33\" E"
    assert DecimalDegreeConverter.format_degrees(False, 30, 10, 23) == "30° 10' 23\" N"
    assert DecimalDegreeConverter.format_degrees(True, 24, 36, 18) == "24° 36' 18\" E"
