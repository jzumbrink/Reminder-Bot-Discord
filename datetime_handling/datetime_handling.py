import datetime
from dateutil.relativedelta import relativedelta

time_periods = {
    'year': 'y',
    'month': 'm',
    'week': 'w',
    'day': 'd',
    'hour': 'h',
    'minute': 'min',
    'second': 's'
}

time_formats = {

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

print(add_time_shortcuts_to_now(extract_time_shortcuts("1w dsanjdfj dfdkjnfdn34w 45min 3d 23y 3w 3m")[1]))
