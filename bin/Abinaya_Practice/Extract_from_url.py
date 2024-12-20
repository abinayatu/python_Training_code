#Extract Date, Pics and URL in 1_program

url='123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)'

sp = url.split()
print("sp:", sp, sep="\n", end="\n\n")

####Getting ip
print(sp[0])

##get date

date=sp[3]
fdate=date[1:12]
print(date)
print("Date is ", fdate)