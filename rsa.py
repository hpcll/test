# -*- coding: utf-8 -*-
from Crypto.Cipher import AES

# 秘钥和文本都是byte类型
# 拼接文本，文本长度需为16的倍数，不足则拼接空格
def splice(text):
    while len(text) % 16 != 0:
        text += b' '
    return text
# 拼接秘钥，秘钥长度需为16的倍数，不足则拼接空格
def splice_key(key):
    while len(key) % 16 != 0:
        key += b' '
    return key


if __name__ == '__main__':
    key = b'2'  # 秘钥
    aes = AES.new(splice_key(key), AES.MODE_ECB)  # 根据秘钥初始化加密器
    text = b'jiamiwenben'  # 加密文本

    encrypted_byte = aes.encrypt(splice(text))  # 使用加密器的加密方法对文本进行加密，返回加密结果(byte类型)
    print("encrypted_byte: ", encrypted_byte)

    decrypt_byte = aes.decrypt(encrypted_byte)  # 使用加密器的解密方法对文本进行解密，返回解密结果(byte类型)
    print("decrypt_str: ", str(decrypt_byte, encoding='utf-8', errors="ignore"))  # 将字节类型转为str类型，错误编码忽略不计