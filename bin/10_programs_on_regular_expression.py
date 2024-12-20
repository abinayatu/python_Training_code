from bin.web_log import log_file_content

print("Extract IP, DATE, PICS")
print("-"*20)
# --------------

import re

for each_line in log_file_content:
    # Provided less information here, so NOT WORKING
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(\w+\.[a-z]{3}).*', each_line)

    # Below pattern not matching lines which is not having image names
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|PATCH|DELETE)\s/pics/(\w+\.(gif|jpg)).*',each_line)

    # Making (pics/wpaper.gif) portion optional so that
    # lines which are not having image name also matched
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(GET|POST|PUT|PATCH|DELETE)\s/(pics/(\w+\.(gif|jpg)))?.*', each_line)

    if match_result is not None:

        ip = match_result.group(1)
        ip = ip.decode() # Convert to string

        dt = match_result.group(2)
        dt = dt.decode()

        img = match_result.group(5)
        if img is None:
            img = "No Image"
        else:
          #  print ("The imge is",img)
            img = img.decode()
        print(ip, dt, img)

# COMMENT
# r-> raw string
r"""

\w -> [a-zA-Z_0-9]
\W -> [^a-zA-Z_0-9] # ^ -> excluding

\s -> One SPACE
\S -> any character except SPACE

"""

print("#"*40, end="\n\n")
################################