import json

with open("./sql2.txt","w+") as w:
    with open("./towns2.txt") as f:
        lines = f.readlines()
        for s in lines:
            # s = f.readline()
            s = f"[{s}]".replace("'",'"')
            arr = json.loads(s)
            for i in arr:
                w.write(f"insert address (code,name,parentcode,citylevel) values ('{i[0]}','{i[1]}','{i[0][0:6]}','4')\n")
                print(f"{i[0]} end.")
print("ok")