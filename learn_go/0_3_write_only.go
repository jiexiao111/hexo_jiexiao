// 源文件中非注释的第一行必须指定当前文件属于哪个包
package main

// 导入 "fmt" 包
import "fmt"

// 函数返回多个值
func write_only_demo(a int) (int, int) {
    return a, 13
}

// 每一个可执行程序必须包含 main 函数
func main() {
    // 展示 _ 的作用，在 go 中这是一个只写变量，表示我们要抛弃这个值
    _, v13 := write_only_demo(2)
    fmt.Println(v13)
}
