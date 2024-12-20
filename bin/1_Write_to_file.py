print("Write to log_report.txt file")
print("-"*20)
# --------------

my_out_file_handle = open("log_report.txt", "w")

# Write Heading
# 1-WAY : Using write
# my_out_file_handle.write("IP\tPICS\n")
# 2-WAY: Using writelines
# my_out_file_handle.writelines(["IP\t", "PICS\n"])
# 3-WAY: Using print-function
print("IP", "PICS", sep="\t\t", file=my_out_file_handle)
my_log_file_handle = open("my_out_file.txt", "r")

log_file_content = my_log_file_handle.readlines()
for each_line in log_file_content:
    if each_line.startswith("123"):
        sp = each_line.split()
        if len(sp) > 6:
            # print("sp:",sp)
            ip = sp[0]
            ip = ip.decode()

            raw_img = sp[6] # b'/pics/wpaper.gif'
            if raw_img.startswith(b"/pics/"):
                img = raw_img[6:]
                img = img.decode()
            else:
                img = "No Image"
            print(ip, img, sep="\t\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
Created log_report.txt, Please check
""")

print("#"*40, end="\n\n")
################################