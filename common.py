import json
import struct
import os
import wmi 


def getBios():
	c = wmi.WMI() 
	for board in c.Win32_BaseBoard(): 
		print("主板序列号：", board.SerialNumber.strip())
		return  board.SerialNumber.strip()
		# break

def load_json(file_name):
	with open(file_name,'r',encoding='utf8')as fp:
		json_data = json.load(fp)
		return json_data

def readfile():
	with open('example.bin', 'rb') as file:
		data = file.read()

	# 解析二进制数据
	result = struct.unpack('ii', data)

	# 打印结果
	print(result)
 
def writeBinfile(string_data, file_name):
	# string_data = "Hello, World!"
	# file_name = "binary_file.bin"

	if not os.path.exists(file_name):
		try:
			with open(file_name, "wb") as file:
				file.write(string_data.encode())
		except:
			print("write file error")
	else:
		print("File already exists.")


def readBinfile(file_path):
	# file_path = "binary_file.bin"
	if os.path.exists(file_path):
		with open(file_path, "rb") as file:
			binary_data = file.read()
			string_data = binary_data.decode()
			print(string_data)
			return string_data
	else:
		print("File does not exist.")
		return  None

if __name__ == "__main__":
	string_data = "Hello, World!"
	file_name = "binary_file.bin"
	# writefile(string_data,file_name)
	# readfile(file_name)
	bios = getBios()
	print("bios" + bios)
    