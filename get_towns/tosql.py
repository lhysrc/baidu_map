import json

with open("d:/sql.txt","w+") as w:
    with open("towns.txt") as f:
        lines = f.readlines()
        for s in lines:
            # s = f.readline()
            s = f"[{s}]".replace("'",'"')
            arr = json.loads(s)
            for i in arr:
                w.write(f"insert t_data ([FBillno],[FSortNm],[FName],[FSort],[FTrantype]) values ({i[0]},4,'{i[1]}',{i[2]},76)\n")
                print(f"{i[0]} end.")
print("ok")