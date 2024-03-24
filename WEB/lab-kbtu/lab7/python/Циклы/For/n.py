binary_str=input()

decimal_num=0

length=len(binary_str)

for i in range(length):
    decimal_num+=int(binary_str[i])*(2**(length-i-1))
print(decimal_num)
