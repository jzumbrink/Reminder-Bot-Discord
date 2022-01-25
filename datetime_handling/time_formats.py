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
    'Sept',
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

"""
Priorities Time (from highest to lowest)
0. re_time_seconds (23:19:35)
1. re_time_am_pm (11:19 pm)
2. re_time (23:19)
"""
re_time = r"(\d|1\d|2[0-3]):([0-5]\d)\s"
re_time_am_pm = r"(\d|1[01]):([0-5]\d)\s(am|pm|AM|PM|a.m.|p.m.)\s"
re_time_seconds = r"(\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)\s"


"""
Priorities Date (from highest to lowest)
0. Date written with month as word or abrreviation (25 Feb. 2022)
1. ISO 8601 (2022-02-25)
2. European Date with year (25.02.2022)
3. US Date with year (02/25/2022)
4. European Date without year (25.02.)
5. US Date without year (02/25)
"""
# Be careful, because re finds 99.01. for example TODO handle verification of day because not possible in regex
# Add whitespace to string and to every regex, before performing operations
regex_day = r"(\d|\d\d)"
regex_month = r"(0?\d|1[0-2])"
# TODO ignore case for month names
regex_month_name = "(" + "|".join([expr+r'\s' for expr in month_names+month_abbreviations+month_abbreviations_with_dot]) + ")"
regex_year = r"(\d{4})"
re_date_european_short = r"{day}\.{month}\.".format(day=regex_day, month=regex_month)
re_date_european = r"{date_short}{year}".format(date_short=re_date_european_short, year=regex_year)
re_date_iso_8601 =r"{year}-{month}-{day}".format(year=regex_year, month=regex_month, day=regex_day)
re_date_us_short = r"{month}/{day}".format(month=regex_month, day=regex_day)
re_date_us = r"{date_us_short}/{year}".format(date_us_short=re_date_us_short, year=regex_year)



print(re.findall(regex_month_name,
                 """1:43 2022-02-23 2022-1-1 02/23 12/12 8/11/2022 May  MaY sept.
                 1.1. 23.12. 23.11. 02.10. 3.10. 24.05.0000 29.11.1945 1.1.2022 
           Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   
              23:12 34:12 12:60 13:1334 13:13 1:45  01:11 23:34 11:34 pm 1:34 pm 23:12:34 12:12:34 10:23 am 1:45 a.m. 8:00 AM
Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet,
           23:12 """)
      )
