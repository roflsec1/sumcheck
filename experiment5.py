#Sender
#10011001111000100010010010000100
#100110011110001000100100
#1001100111100010 
#0010010010000100
#_Author_: wh1t3-h4t

m = 8
data = input("Enter data whose size is a multiple of {}: ".format(m))

while len(data)%m!=0 and len(data)<=m:
	data = input("INVALID! Please enter data whose size is a multiple of 8: ")

k = len(data)//m
data_list = [data[i:i+m] for i in range(0, len(data), m)]
bin_sum1 = 0b0
for i in range(k):
	bin_sum1 = bin_sum1 + int(data_list[i], 2)
	print(bin(bin_sum1))
	if len(bin(bin_sum1)) > m+2 and bin(bin_sum1)[2] == '1':
		bin_sum1 = bin_sum1 + 0b1
		bin_sum1 = bin(bin_sum1)[0:2] + bin(bin_sum1)[3:] #cutting msb
		bin_sum1 = int(bin_sum1, 2)

if len(bin(bin_sum1)) < len(bin(int(data_list[1], 2))):
	_sum = "0" * (m+2-len(bin(bin_sum1))) + bin(bin_sum1)[2:]

print("Sum: " + _sum)

checksum = ['0','b'] #writing checksum
for i in range(len(_sum)):
	if _sum[i] == "1":
		checksum.append("0")
	else:
		checksum.append("1")

checksum = ''.join(checksum)
print("Checksum: " + checksum[2:])

#Receiver
sum_ = bin(int(_sum, 2) + int(checksum, 2))[2:]
complement = ['0', 'b'] 
for i in range(len(sum_)): #complement
	if sum_[i] == "1":
		complement.append("0")
	else:
		complement.append("1")

complement = ''.join(complement)
print("Complement: " + complement[2:])
if int(complement, 2) == 0:
	print("Data Accepted")
else:
	print("Data Rejected")