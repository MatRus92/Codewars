def past(h, m, s):
    MILISECOND = 1000

    hour_ms = 3600 * h * MILISECOND
    minute_ms = 60 * m * MILISECOND
    second_ms = int(s) * MILISECOND

    return hour_ms + minute_ms + second_ms