# 声明一个函数 将电话进行加密 返回加密后的内容
# 解密函数：传入加密后的内容 返回的是电话号码
# 电话号码不固定

import hashlib

# 加密
def encryption(number):
    
    #content = input("请输入您的电话号码： ")
    content = str(number)#"13510681710"
    md = hashlib.md5()
    # md.update(content.encode())
    # md_result = md.hexdigest()
    # print(md_result)
    if len(content) == 11:
        phone = '0123456789'
        # password = 'abcdefghij'
        password = ')!@#$%^&*('
        encryption_tab = str.maketrans(phone, password)
        res1 = content.translate(encryption_tab)
        md.update(content.encode())
        md_result = md.hexdigest()
        print(md_result)
        print("请保管好您的licence:", md_result)
        return md_result
    else:
        print("请检查你的手机号是否输入正确！")
        return "erro"


#res1 = encryption()


# 解密
def decrypt():
    content = input("请输入您的密码： ")
    if len(content) == 11:
        phone = '0123456789'
        # password = 'abcdefghij'
        password = ')!@#$%^&*('
        decrypt_tab = str.maketrans(password, phone)
        res2 = content.translate(decrypt_tab)
        print("这是您的电话号码： ", res2)
        return res2
    else:
        print("请检查你的密码是否输入正确！")


#res2 = decrypt()


if __name__ == '__main__':
    number = "13510681710"
    encryption(number)