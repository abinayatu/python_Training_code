print("Extract info and print only")
print("-"*20)
# --------------
my_log_file_handle = open("my_out_file.txt", "r")

log_file_content = my_log_file_handle.readlines()
print(log_file_content, end="\n\n")
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
            print(ip, img)

print("#"*40, end="\n\n")
################################