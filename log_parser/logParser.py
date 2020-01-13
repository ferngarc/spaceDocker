
# https://regex101.com/r/zGpfgw/7
import re
import logging

# A nice big fat regex that parses your entire log lines
regex = re.compile(
    r"\[(?P<wday>\w+)\s(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>[0-9]{0,4}:[0-9]{0,4}:[0-9]{0,4})\s+(?P<tzone>\w+)\s+(?P<year>\d+)\] Ping=\"(?P<ping>[0-9]{1,5}.?[0-9]{0,5})\sms\" Download=\"(?P<download>[0-9]{0,6}.?[0-9]{0,6})\s?Mbit\/s\" Upload=\"(?P<upload>[0-9]{0,6}.?[0-9]{0,6})\s?Mbit\/s\"")

filename = 'speedtest.log'

# We open the file here and iterate through it.

with open(filename, 'r') as file_handle:
    file_data = file_handle.read()
    for line in file_data.split("\n"):
        line_data = regex.search(line)
        if line_data is None:
            if line is not '':
                # Here's some nice logging so that you can narrow down if your regex failed.
                logging.error('Regex failed on: %s' % line)
            continue
        else:
            # Let's create a group dictionary of each field so that we can individually call them out.
            line_data = line_data.groupdict()
            for field in ['wday', 'month', 'day', 'time', 'tzone', 'year', 'ping', 'download', 'upload']:
                line_data[field] = line_data[field]
                if float(line_data['download']) > 500:
                    print("on " + line_data['month'], line_data['day'], line_data['year'], " at ", line_data['time'], "Download speed is ",
                          line_data['download'])
