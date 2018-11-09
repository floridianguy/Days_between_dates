"""This project counts the number of days between two dates."""

y1 = 1991
m1 = 8
d1 = 5
y2 = 2008
m2 = 1
d2 = 3

def leap_years(y1, y2):
    """Count the number of leap leap years between the two dates so
    that additional days can be included in our count."""
    leaps = []
    takeouts = []
    for y in range(y1, y2, 1):
        if y % 4 == 0:
            leaps.append(True)
        if y % 400 != 0 and y % 100 == 0:
            takeouts.append(True)
        else:
            leaps.append(False)
    return leaps.count(True) - takeouts.count(True)

d_i_m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,
    8:31, 9:30, 10:31, 11:30, 12:31}

def days_m_y(y1, m1, y2, m2):
    """Count the number of days in the month and year provided.
    This applies only to whole months."""
    day_count = []
    if y2 >= y1 and m2 >= m1:
        day_count.append((y2-y1)*365)
        while y2 >= y1 and m2 > m1:
            a = d_i_m.get(m2-1)
            day_count.append(a)
            m2 -= 1
    elif y2 > y1 and m1 > m2:
        day_count.append((y2-y1-1)*365)
        while m2 > 1:
            b = d_i_m.get(m2-1)
            day_count.append(b)
            m2 -= 1
        while m1 <= 12:
            c = d_i_m.get(m1)
            day_count.append(c)
            m1 += 1
    return sum(day_count)

extra_true1 = [y1==y2, y2%4==0, m1<=2, d1<=28, m2>=3]
extra_true2 = [y2>y1, y2%4==0, m2>=3]
if all(extra_true1):
    extra_day = 1
elif all(extra_true2):
    extra_day = 1
else:
    extra_day = 0

def days_between_dates(y1, m1, d1, y2, m2, d2):
    """Use the functions described above plus the number of additional
    days to obtain our final day count."""
    assert (days_m_y(y1, m1, y2, m2) + (d2-d1)) >= 0, \
        "date2 must be after date1"
    return days_m_y(y1, m1, y2, m2) + (d2-d1) + \
        leap_years(y1, y2) + extra_day

if extra_day + leap_years(y1, y2) == 1:
    print('Leaps years added one extra day.\n')
else:
    print('Leaps years added', (leap_years(y1, y2) + extra_day), \
    'extra days.\n')

print('Time elapsed:', days_between_dates(y1, m1, d1, y2, m2, d2), \
    'days\n')
