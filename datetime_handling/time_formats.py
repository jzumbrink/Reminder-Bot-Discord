import datetime
import re

month_abbreviations = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    #'Sept', TODO add support für Sept as Abbreviation and as "13th month" and need support for 4 char long abbreviations
    'Oct',
    'Nov',
    'Dec',
]

month_abbreviations_with_dot = [month_abr+r'\.' for month_abr in month_abbreviations]

month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]


def get_month_number(month_str: str) -> int:
    return month_names.index(month_str) if month_str in month_names else month_abbreviations.index(month_str[:3])


"""
Priorities Time (from highest to lowest)
0. re_time_seconds (23:19:35)
1. re_time_am_pm (11:19 pm)
2. re_time (23:19)
"""
regex_hour = r"(\d|1\d|2[0-3])"
regex_hour_half = r"(\d|1[01])"
regex_minute = r"([0-5]\d)"
regex_second = regex_minute
regex_am_pm = r"(am|pm|AM|PM|a.m.|p.m.)"

re_time = r"{hour}:{minute}".format(hour=regex_hour, minute=regex_minute)
re_time_am_pm = r"{hour}:{minute}\s{ampm}".format(hour=regex_hour, minute=regex_minute, ampm=regex_am_pm)
re_time_seconds = r"{hour}:{minute}:{second}".format(hour=regex_hour, minute=regex_minute, second=regex_second)


def apply_re_time_seconds(datetime_obj: datetime.datetime, values: list):
    return datetime_obj.replace(hour=values[0], minute=values[1], second=values[2])


time_formats = [
    [re_time_seconds, lambda datetime_obj, values: datetime_obj.replace(
        hour=int(values[0]),
        minute=int(values[1]),
        second=int(values[2])
    )],
    [re_time_am_pm, lambda datetime_obj, values: datetime_obj.replace(
        hour=int(values[0]) + (0 if values[2].lower() == 'am' else 12),
        minute=int(values[1])
    )],
    [re_time, lambda datetime_obj, values: datetime_obj.replace(
        hour=int(values[0]),
        minute=int(values[1])
    )]
]

"""
Priorities Date (from highest to lowest)
0. Date written with month as word or abrreviation (25 Feb. 2022)
1. ISO 8601 (2022-02-25)
2. European Date with year (25.02.2022)
3. European Date without year (25.02.)
4. US Date with year (02/25/2022)
5. US Date without year (02/25)
"""
# Be careful, because re finds 99.01. for example TODO handle verification of day because not possible in regex
# Add whitespace to string and to every regex, before performing operations
regex_day_short_allowed = r"(\d|\d\d)"
regex_day = r"(\d\d)"
regex_month = r"(0?\d|1[0-2])"
# TODO ignore case for month names
regex_month_name = "(" + "|".join([expr for expr in month_names+month_abbreviations+month_abbreviations_with_dot]) + ")"
regex_year = r"(\d{4})"

re_date_european_short = r"{day}\.{month}\.".format(day=regex_day_short_allowed, month=regex_month)
re_date_european = r"{date_short}{year}".format(date_short=re_date_european_short, year=regex_year)
re_date_iso_8601 =r"{year}-{month}-{day}".format(year=regex_year, month=regex_month, day=regex_day)
re_date_us_short = r"{month}/{day}".format(month=regex_month, day=regex_day)
re_date_us = r"{month}/{day}/{year}".format(month=regex_month, day=regex_day, year=regex_year)
re_date_abbreviation_english = r"{day}\s{month_abr}\s{year}".format(day=regex_day, month_abr=regex_month_name, year=regex_year)

date_formats = [
    [re_date_abbreviation_english, lambda datetime_obj, values: datetime_obj.replace(
        day=int(values[0]),
        month=get_month_number(values[1]),
        year=int(values[2])
    )],
    [re_date_iso_8601, lambda datetime_obj, values: datetime_obj.replace(
        year=int(values[0]),
        month=int(values[1]),
        day=int(values[2])
    )],
    [re_date_european, lambda datetime_obj, values: datetime_obj.replace(
        day=int(values[0]),
        month=int(values[1]),
        year=int(values[2])
    )],
    [re_date_european_short, lambda datetime_obj, values: datetime_obj.replace(
        day=int(values[0]),
        month=int(values[1])
    )],
    [re_date_us, lambda datetime_obj, values: datetime_obj.replace(
        month=int(values[0]),
        day=int(values[1]),
        year=int(values[2])
    )],
    [re_date_us_short, lambda datetime_obj, values: datetime_obj.replace(
        day=int(values[1]),
        month=int(values[0]),
    )],
]

#TODO test every time format precisely
date_time_formats = [time_formats, date_formats]

