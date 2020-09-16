import os
products = []

if os.path.isfile("cm.txt"):
	print("found it!")
	with open("cm.txt","r",encoding="utf8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
		s = line.strip().split(",")
		print(s)
		name = s[0]
		price = s[1]
		products.append([name,price])
else:
	print("cannot find...")

while True:
	name = input("請輸入名稱：")
	if name == "q":
		break
	price = input("請輸入價格：")
	products.append([name,price])
print(products)

for p in products:
	print(p[0],"的價格是",p[1])

with open("cm.txt","w") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")