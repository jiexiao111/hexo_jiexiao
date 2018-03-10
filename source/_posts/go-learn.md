---
title: Go 语言学习
date: 2018-03-10 11:20:36
categories: 编程语言
tags:
  - Go
---

<!-- 文章开头都用它了，整齐才好看 -->
{% note default %}
公司技能鉴定可以选择的语言有 C/C++/Java/Go，我只对 C 比较熟悉，但是 C 的基本数据结构不方便做技能鉴定，所以在剩下三种语言中选择了比较年轻的 Go
{% endnote %}

<!--more-->

---

# 第一个 Go 程序
* 将以下内容保存至 ``/tmp/hello.go``
``` go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```
* 运行
```shell
$ go run /tmp/hello.go
Hello, World.
```
* 调试
	首先要编译成执行文件
```shell
$ go build -gcflags "-N -l" /tmp/hello.go
```
	使用 gdb 调试
```shell
$ gdb hello
(gdb) l
1       package main
2
3       import "fmt"
4
5       func main(){
6           fmt.Println("Hello, World.")
7       }
(gdb) b 6
Breakpoint 1 at 0x48319d: file /tmp/hello.go, line 6.
(gdb) r
Starting program: /root/jupyter/hexo_jiexiao/hello
Thread 1 "hello" hit Breakpoint 1, main.main () at /tmp/hello.go:6
6           fmt.Println("Hello, World.")
```
# Go 语言数据类型
<style>
table th:nth-of-type(1) {
    width: 80px;
}
table th:nth-of-type(2) {
    width: 500px;
}
table th {
    font-weight: bold; /*加粗*/
    font-size: 12pt;
    text-align: center !important; /*内容居中，加上 !important 避免被 Markdown 样式覆盖*/
    background: rgba(158,188,226,0.2); /*背景色*/
}
</style>

| 类型      | 描述                                                    |
| ----      | ----                                                    |
| byte      | 类似于 uint8                                            |
| rune      | 类似于 int32                                            |
| uint      | 32 / 64 无符号                                          |
| int       | 与 uint 一样，有符号                                    |
| uintptr   | 无符号整型，用于存指针                                  |
| uint8     | [0, 255]                                                |
| uint16    | [0, 65535]                                              |
| uint32    | [0, 4 294 967 295]                                      |
| uint64    | [0, 18 446 744 073 709 551 615]                         |
| int8      | [-128, 127]                                             |
| int16     | [-32768, 32767]                                         |
| int32     | [-2 147 483 648, 2 147 483 647]                         |
| int64     | [-9 223 372 036 854 775 808, 9 223 372 036 854 775 807] |
| float32   | 32 位浮点                                               |
| float64   | 64 位浮点                                               |
| complex32 | 32 位实数和虚数                                         |
| complex64 | 64 位实数和虚数                                         |

# 变量
``` go
package main

// 常用于申明全局变量
var (
    a int
    b bool
)

// var v_name v_type
var x, y int
// var v_name v_type = value
var c, d int = 1, 2
// var v_name = value
var e, f = 123, "hello"

// 不能用这种方式声明全局变量
// g, h := 123, "hello"

func main(){
	// v_name := value
    g, h := 123, "hello"
    println(x, y, a, b, c, d, e, f, g, h)
}
```
# 常量
``` go
package main

import "fmt"

func main() {
   const LENGTH int = 10
   fmt.Printf("%d\n", LENGTH)
}
```

# 条件语句
## if ...
``` go
package main

import "fmt"

func main() {
	/* 定义局部变量 */
	var a int = 10

	/* 使用 if 语句判断布尔表达式 */
	if a < 20 {
		/* 如果条件为 true 则执行以下语句 */
		fmt.Printf("a 小于 20\n" )
	}
	fmt.Printf("a 的值为 : %d\n", a)
}
```

## if ... else ...
``` go
package main

import "fmt"

func main() {
   /* 定义局部变量 */
   var a int = 10

   /* 使用 if 语句判断布尔表达式 */
   if a < 20 {
       /* 如果条件为 true 则执行以下语句 */
       fmt.Printf("a 小于 20\n" )
   }
   fmt.Printf("a 的值为 : %d\n", a)
}
```
## switch
``` go
package main

import "fmt"

func main() {
   /* 定义局部变量 */
   var grade string = "B"
   var marks int = 90

   switch marks {
      case 90: grade = "A"
      case 80: grade = "B"
      case 50,60,70 : grade = "C"
      default: grade = "D"
   }

   switch {
      case grade == "A" :
         fmt.Printf("优秀！\n" )
      case grade == "B", grade == "C" :
         fmt.Printf("良好、n" )
      case grade == "D" :
         fmt.Printf("及格、n" )
      case grade == "F":
         fmt.Printf("不及格、n" )
      default:
         fmt.Printf("差、n" );
   }
   fmt.Printf("你的等级是 %s\n", grade );
}
```
## type switch
```go
package main

import "fmt"

type Bag_1 struct{
    key string
}

type Bag_2 struct{
    key int
}

func print_type(x1 interface{}) {
    switch v := x1.(type) {
    case Bag_1:
        fmt.Println("b1.(type):", "Bag_1", v)
    case Bag_2:
        fmt.Println("b2.(type):", "Bag_2", v)
    default:
        fmt.Println("Unknown.")
    }
}

func main() {
	var x1 interface{}
	var x2 interface{}

    x1 = Bag_1{key: "1"}
    x2 = Bag_2{key: 2}

    print_type(x1)
    print_type(x2)
}
```
## select
TODO

# 循环
## for ...
``` go
package main

import "fmt"

func main() {
	var b int = 15
	var a int

	numbers := [6]int{1, 2, 3, 5}

	for a := 0; a < 10; a++ {
		fmt.Printf("循环 1：a 的值为：%d\n", a)
		break
	}

	for a < b {
		a++
		fmt.Printf("循环 2：a 的值为：%d\n", a)
	}

	for i, x := range numbers {
		fmt.Printf("第 %d 位 x 的值 = %d\n", i, x)
	}
}
```
## continue/break
TODO

## goto
TODO

# 数组
``` go
package main

import "fmt"

func main() {
   var n [10]int /* n 是一个长度为 10 的数组 */
   var i,j int

   /* 为数组 n 初始化元素 */
   for i = 0; i < 10; i++ {
      n[i] = i + 100 /* 设置元素为 i + 100 */
   }

   /* 输出每个数组元素的值 */
   for j = 0; j < 10; j++ {
      fmt.Printf("Element[%d] = %d\n", j, n[j] )
   }
}
```
# Map
``` go
package main

import "fmt"

func main() {
   var countryCapitalMap map[string]string
   /* 创建集合 */
   countryCapitalMap = make(map[string]string)

   /* map 插入 key-value 对，各个国家对应的首都 */
   countryCapitalMap["France"] = "Paris"
   countryCapitalMap["Italy"] = "Rome"
   countryCapitalMap["Japan"] = "Tokyo"
   countryCapitalMap["India"] = "New Delhi"

   /* 使用 key 输出 map 值 */
   for country := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",countryCapitalMap[country])
   }

   /* 查看元素在集合中是否存在 */
   captial, ok := countryCapitalMap["United States"]
   /* 如果 ok 是 true, 则存在，否则不存在 */
   if(ok){
      fmt.Println("Capital of United States is", captial)
   }else {
      fmt.Println("Capital of United States is not present")
   }
}
```
# Range
``` go
package main
import "fmt"
func main() {
	// 这是我们使用 range 去求一个 slice 的和。使用数组跟这个很类似
	nums := []int{2, 3, 4}
	sum := 0
	for _, num := range nums {
		sum += num
	}
	fmt.Println("sum:", sum)
	// 在数组上使用 range 将传入 index 和值两个变量。上面那个例子我们不需要使用该元素的序号，所以我们使用空白符"_"省略了。有时侯我们确实需要知道它的索引。
	for i, num := range nums {
		if num == 3 {
			fmt.Println("index:", i)
		}
	}
	//range 也可以用在 map 的键值对上。
	kvs := map[string]string{"a": "apple", "b": "banana"}
	for k, v := range kvs {
		fmt.Printf("%s -> %s\n", k, v)
	}
	//range 也可以用来枚举 Unicode 字符串。第一个参数是字符的索引，第二个是字符（Unicode 的值）本身。
	for i, c := range "go" {
		fmt.Println(i, c)
	}
}
```
