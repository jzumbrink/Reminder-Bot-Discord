import datetime

from dateutil.relativedelta import relativedelta
from .time_formats import *

time_periods = {
    'year': 'y',
    'month': 'm',
    'week': 'w',
    'day': 'd',
    'hour': 'h',
    'minute': 'min',
    'second': 's'
}


def extract_time_shortcuts(text: str):
    time_periods_found = {value: 0 for value in time_periods.values()}
    new_msg = []
    for word in text.split(' '):
        for time_period in time_periods.values():
            if len(word) > len(time_period):
                if time_period == word[-len(time_period):] and word[:-len(time_period)].isdigit():
                    time_periods_found[time_period] += int(''.join(filter(lambda c: c.isdigit(), word)))
                    break
        else:
            new_msg.append(word)
    return ' '.join(new_msg), time_periods_found


def add_time_shortcuts_to_datetime(time_shortcuts: dict, given_datetime: datetime.datetime):
    return given_datetime + relativedelta(
        years=time_shortcuts[time_periods['year']],
        months=time_shortcuts[time_periods['month']],
        weeks=time_shortcuts[time_periods['week']],
        days=time_shortcuts[time_periods['day']],
        hours=time_shortcuts[time_periods['hour']],
        minutes=time_shortcuts[time_periods['minute']],
        seconds=time_shortcuts[time_periods['second']],
    )


def add_time_shortcuts_to_now(time_shortcuts: dict):
    return add_time_shortcuts_to_datetime(time_shortcuts, datetime.datetime.now())


def extract_explizit_time_specification(text: str) -> list:
    new_datetime = datetime.datetime.now()
    for time_format_class in date_time_formats:  # TODO use real time formats
        for time_format in time_format_class:
            found_values = re.findall(time_format[0], text)
            if len(found_values) > 0:
                text = re.sub(time_format[0], '', text)
                new_datetime = time_format[1](new_datetime, found_values[0])
                break

    return text, new_datetime
