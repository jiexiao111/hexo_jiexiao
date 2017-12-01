---
title: 修改 CapsLock 为 Ctrl
date: 2017-11-30 23:20:48
categories: 操作系统
tags:
  - Mac
  - Windows
---

{% note default %}
CapsLock 比 Ctrl 容易按，修改一下还是挺方便的
{% endnote %}

<!--more-->

---

# MAC
* 选取苹果菜单 >“系统偏好设置”，然后点按“键盘”。
* 点按“修饰键”按钮。
* 从想要更改的修饰键旁边的弹出式菜单中选取一项操作，然后点按“好”。

# Win7
* 点击 Win+R 键

* 在输入框键入 regedit，打开注册表

* 进入 HKEY_LOCAL_MACHINE -> System -> CurrentControlSet -> Control -> KeyBoard Layout。记住，一定是 keyBoard Layout，而不是 KeyBoard Layouts

* 右键菜单，然后选择 New -> Binary value

* 重命名 New Value #1 -> Scancode Map

* 右键菜单 Scancode Map -> Modify

输入如下值，保存

0000 00 00 00 00 00 00 00 00
0008 03 00 00 00 1D 00 3A 00
0010 3A 00 1D 00 00 00 00 00
0018

前两行和最后一行，都是固定的，全部为 0。第三行，表示你修改了几个键，其实我们只是改了两个键，不过最后那一行也要算进去，所以是 3。
重点是在第四行和第五行。3A00，代表 Caps Lock， 1D00，代表 Ctrl。这一行，意思即为，将 Caps Lock 映射为 Ctrl
第五行，就不用说了，意思刚好相反。
修改完毕后，重新登录 Windows 即可生效！
下面附上各个键位值的参考：

```
Escape 01 00
Tab 0F 00
Caps Lock 3A 00
Left Alt 38 00
Left Ctrl 1D 00
Left Shift 2A 00
Left Windows 5B E0
Right Alt 38 E0
Right Ctr l1D E0
Right Shift 36 00
Right Windows 5C E0
Backspace 0E 00
Delete 53 E0
Enter 1C 00
Space 39 00
Insert 52 E0
HOME 47 E0
End 4F E0
Num Lock 45 00
Page Down 51 E0
Page Up 49 E0
Scroll Lock 46 00
```

