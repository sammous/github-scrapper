#Reformating list proxy address from "123.143.63.76 8080" to "http://123.143.63.76:8080"

f = open("list_proxy.txt",'r')

newfile = open("list_proxy2.txt","w")

for line in f:
	l = line.split()
	address = "http://" + l[0] + ":" + l[1]
	newfile.write(address+"\n")

