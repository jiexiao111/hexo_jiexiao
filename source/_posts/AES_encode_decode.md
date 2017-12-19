---
title: 通过 AES 加解密
date: 2017-12-17 21:18:37
categories: 编程语言
tags:
  - python
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
公司 IT 提出一个很奇葩的需求，他们要给我一个账户和密码，但是要求不给我明文密码，要我做一个密码输入框类似的东西，然后我自己加密保存，我着实不能理解，但是为了要到权限，我忍了......
{% endnote %}

<!--more-->

---

# 实现代码

```python
import getpass
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    #加密函数，如果 text 不是 16 的倍数【加密文本 text 必须为 16 的倍数！】，那就补足为 16 的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #这里密钥 key 长度必须为 16（AES-128）、24（AES-192）、或 32（AES-256）Bytes 长度。目前 AES-128 足够用
        length = 16
        count = len(text)
        if(count % length != 0) :
                add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为 AES 加密时候得到的字符串不一定是 ascii 字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为 16 进制字符串
        return b2a_hex(self.ciphertext)

    #解密后，去掉补足的空格用 strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')

if __name__ == '__main__':
    pc = prpcrypt('keyskeyskeyskeys')      #初始化密钥
    count = input('Input username: ')
    while(True):
        passwd = getpass.getpass('Input passwd: ')
        passwd_copy = getpass.getpass('Repeat Passwd: ')
        if passwd == passwd_copy:
            break
        else:
            print('Entered passwords inconsistent, please try again.')
    e = pc.encrypt(passwd)
    d = pc.decrypt(e)
    print('%s' % (e))
```

# 问题
运行提示如下：
```
ModuleNotFoundError: No module named 'Crypto'
```

估计是 ``crypto`` 和 ``pycrypto`` 存在冲突，全部卸载后，重装 ``pycrypto`` 即可
```
pip3 uninstall crypto
pip3 uninstall pycrypto
pip3 install pycrypto
```

# 参考
[使用 Python 进行 AES 加密和解密](http://blog.csdn.net/nurke/article/details/77267081)
[解决 python 种输入 from Crypto.Cipher import AES 报错 ImportError: No module named Crypto.Cipher](http://blog.csdn.net/adorkable_yu/article/details/75570790)
