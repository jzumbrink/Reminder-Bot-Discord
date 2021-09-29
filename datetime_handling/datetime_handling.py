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
    time_periods_found = {}
    new_msg = []
    for word in text.split(' '):
        for time_period in time_periods.values():
            if len(word) > len(time_period):
                if time_period == word[-len(time_period):] and word[:-len(time_period)].isdigit():
                    if time_period not in time_periods_found.keys():
                        time_periods_found[time_period] = 0
                    time_periods_found[time_period] += int(''.join(filter(lambda c: c.isdigit(), word)))
                    break
        else:
            new_msg.append(word)
    return ' '.join(new_msg), time_periods_found


print(extract_time_shortcuts("1w dsanjdfj dfdkjnfdn34w 45min 3d"))
