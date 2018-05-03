"""Solution for HackerRank challenge: Time Conversion
"""

def time_conversion(hh, mm, ss, XM):
    """Convert time from hh:mm:ssXM format to HH:mm:ss format
        Where:
            01 <= hh <= 12
            00 <= HH <= 23
            X = A | P
    """
    new_time = [hh, mm, ss]
    if XM == 'PM':
        new_time[0] = (int(new_time[0]) + 12) % 24
        new_time[0] = '{:02d}'.format(new_time[0])
    if hh == '12':
        new_time[0] = (int(new_time[0]) + 12) % 24
        new_time[0] = '{:02d}'.format(new_time[0])
    result = ''
    for i in new_time:
        result += str(i) + ':'
    return result[:-1]

def main():
    """Receives input from stdin, provides output to stdout.
    """
    h12_time = raw_input().split(':')
    print time_conversion(h12_time[0], h12_time[1], h12_time[2][0:2], h12_time[2][2:4])

if __name__ == '__main__':
    main()
