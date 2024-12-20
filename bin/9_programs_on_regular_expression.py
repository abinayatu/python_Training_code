from bin.web_log import log_file_content

print("Extract IP, DATE")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)

   # (br'(\d\d\d\.\d{3}\..\d{1,3}\.[0-9]{3}).*'
   #  br'(\d{2}/[a-zA-Z]){3}/\d{4}).*'

    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        dt = match_result.group(2)
        dt = dt.decode()

        print(ip, dt)

# COMMENT
# r-> raw string
r"""

26/Apr/2000

26
---
\d\d # Strictly 2 digits
\d{2} # Strictly 2 digits
[0-9][0-9] # Strictly 2 digits
[0-9]{2} # Strictly 2 digits
\d[0-9] # Strictly 2 digits
[0-9]\d # Strictly 2 digits

\d{1,2} # minimum 1, maximum 2
[0-9]{1,2} # minimum 1, maximum 2
\d?\d # minimum 1, maximum 2
[0-9]?[0-9] # minimum 1, maximum 2
[0-9]?\d # minimum 1, maximum 2
\d?[0-9] # minimum 1, maximum 2
---

Apr
---
[a-zA-Z][a-zA-Z][a-zA-Z]
[a-zA-Z]{3}
[A-Z][a-z][a-z]
[A-Z][a-z]{2}
(Jan|Feb|Mar|Apr)
---

"""

print("#"*40, end="\n\n")
################################