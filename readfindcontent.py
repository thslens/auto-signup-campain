
def joinNow():
  div.rules-info

myStr = "Mức % giảm voucher ≥ 20% (nghĩa là Giá trị voucher/ Giá trị đơn hàng tối thiểu ≥ 20%)\
- Giá trị giảm tối đa: 50k"
substring = "Giá trị đơn hàng tối thiểu ≥ 20%"
str_len = len(myStr)
sub_len = len(substring)
sub_indices = []
b = False
for i in range(str_len - sub_len):
	if myStr[i:i + sub_len] == substring:
		# sub_indices.append(i)
		joinNow()
		break
  
if b is True:
  print("ok")

