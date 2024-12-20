"""
Get data from web_server.log

then Extract

IP
DATE
PICS
URL

then write to log_report.txt

Expected Output in log_report.txt:
----------------
123.123.123.123     26/Apr/2000     wpaper.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star2000.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image      http://www.jafsoft.com/asctortf/
----------------
"""

print("Getting data from web_server.log")
print("-"*20)
# --------------

# Step-1: Connect to file
# --------------
# Absolute Path
# my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
# OR
# Relative Path
my_log_file_handle = open(r"../log/web_server.log", "rb")
# rb = r-> read only b-> binary file

# Step-2: Read
# --------------
log_file_content = my_log_file_handle.readlines()
print(log_file_content, end="\n\n")

# Step-3: Disconnect
# --------------
my_log_file_handle.close()

print("Checking type of one line:", type(log_file_content[0]), end="\n\n")

print("#"*40, end="\n\n")
################################