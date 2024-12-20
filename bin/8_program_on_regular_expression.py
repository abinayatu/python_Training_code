from bin.web_log import log_file_content

print("Extract IP")
print("-" * 20)
# --------------

import re

for each_line in log_file_content:
    # match_result = re.match('\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3})(.*)', each_line)
    # br : b -> bytes r -> raw string
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode()  # Convert to string

        remaining = match_result.group(2)

        print("IP:", ip)
        print("remaining:", remaining, end="\n\n")

# COMMENT
# r-> raw string
r"""
put () to IP address pattern to capture
this is called grouping
each group has index number starting from 1
"""

print("#" * 40, end="\n\n")
################################