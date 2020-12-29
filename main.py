import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits=['1','2','3','4','5','6','7','8','9','0']
symbols=['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=','>','?', '@', '[', ']', '^', '_', '`', '{', '|', '}', ',', '~']
pass_len=int(input('Enter the length of password'))
digit_count=int(input('Enter the number of digits'))
symbol_count=int(input('Enter the number of symbols'))
char_count=pass_len-(digit_count+symbol_count)
passwd_list=[]
while char_count != 0:
    x = random.choice(letters)
    passwd_list.append(x)
    char_count-=1

while symbol_count!=0:
    x=random.choice(symbols)
    passwd_list.append(x)
    symbol_count-=1

while digit_count!=0:
    x=random.choice(digits)
    passwd_list.append(x)
    digit_count-=1
passwd=""
for num in range(0,pass_len):
    x=random.choice(passwd_list)
    passwd+=x
print(passwd)
