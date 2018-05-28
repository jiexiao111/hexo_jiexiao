// 源文件中非注释的第一行必须指定当前文件属于哪个包
package main

// 导入 "fmt" 包
import "fmt"
import "reflect"

// 定义全局变量
var(
    v4 int = 3
    v5 bool
)

// 不能用这种格式申明全局变量
// v6 := 1

// 定义函数，用于打印变量
func variable_demo() {
    // 指定类型，不赋初值
    var v1 int
    fmt.Println("v1 =", v1)
    v1 = 2
    fmt.Println("v1 =", v1)

    // 根据值自行判断类型
    var v2 = "1"
    fmt.Println("Type of v2:", reflect.TypeOf(v2))

    // 省略 var，但是需要注意 := 左侧的变量不能是已经申明了的
    v3 := 10
    fmt.Println("v3 =", v3)
    // 以下语句提示: no new variables on left side of :=
    // v3 := 10

    fmt.Println(v4, v5)

    // 多变量申明，仅指定类型
    var v7, v8 int
    v7, v8 = 7, 8
    fmt.Println(v7, v8)

    // 多变量申明，仅指定值
    var v9, v10 = 9, "10"
    fmt.Println("Type of v9/v10:", reflect.TypeOf(v9), reflect.TypeOf(v10))

    // 多变量申明，省略 var 关键字
    v11, v12 := "11", 12
    fmt.Println("Type of v11/v12:", reflect.TypeOf(v11), reflect.TypeOf(v12))
}

// 每一个可执行程序必须包含 main 函数
func main() {
    // 调用自定义函数
    variable_demo()
}
