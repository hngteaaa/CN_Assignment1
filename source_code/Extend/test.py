str = "<socket.socket fd=412, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.11', 3750), raddr=('192.168.1.11', 49622)>"
str1 = ""
count = 0
count1 = 0

for i in range(len(str)):
    if str[i] == '(':
        count1 += 1
    if str[i] == ',' and count1 == 1:
        count += 1
    if count == 1 and str[i] != ',' and str[i] != ' ':
        if str[i] == ')':
            break
        str1 += str[i]
        
print(str1)

