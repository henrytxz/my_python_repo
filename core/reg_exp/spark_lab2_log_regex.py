import re
import datetime

month_map = {'Jan': 1, 'Feb': 2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7,
    'Aug':8,  'Sep': 9, 'Oct':10, 'Nov': 11, 'Dec': 12}

def parse_apache_time(s):
    """ Convert Apache time format into a Python datetime object
    Args:
        s (str): date and time in Apache time format
    Returns:
        datetime: datetime object (ignore timezone for now)
    """
    return datetime.datetime(int(s[7:11]),
                             month_map[s[3:6]],
                             int(s[0:2]),
                             int(s[12:14]),
                             int(s[15:17]),
                             int(s[18:20]))

def parseApacheLogLine(logline):
    """ Parse a line in the Apache Common Log format
    Args:
        logline (str): a line of text in the Apache Common Log format
    Returns:
        tuple: either a dictionary containing the parts of the Apache Access Log and 1,
               or the original invalid log line and 0
    """
    match = re.search(APACHE_ACCESS_LOG_PATTERN, logline)
    if match is None:
        return (logline, 0)
    size_field = match.group(9)
    if size_field == '-':
        size = long(0)
    else:
        size = long(match.group(9))

    host          = match.group(1),
    client_identd = match.group(2),
    user_id       = match.group(3),
    date_time     = parse_apache_time(match.group(4)),
    method        = match.group(5),
    endpoint      = match.group(6),
    protocol      = match.group(7),
    response_code = int(match.group(8)),
    content_size  = size

    return ((
        host,
        client_identd,
        user_id,
        date_time,
        method,
        endpoint,
        protocol,
        response_code,
        content_size
    ), 1)

APACHE_ACCESS_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*([\S\s]*)" (\d{3}) (\S+)'

failed_line = 'ix-sac6-20.ix.netcom.com - - [08/Aug/1995:14:43:39 -0400] "GET / HTTP/1.0 " 200 7131'
succeeded_line = '127.0.0.1 - - [01/Aug/1995:00:00:01 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1839'
print parseApacheLogLine(failed_line)
print parseApacheLogLine(succeeded_line)

PART_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) ([\S\s]+)\s*(\S*)"'
print re.search(PART_LOG_PATTERN, failed_line).group()