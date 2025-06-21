f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present in the content ")
else:
    print("twnkle is not  present in the content ")

f.close()