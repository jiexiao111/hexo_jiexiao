// 源文件中非注释的第一行必须指定当前文件属于哪个包
package main

// 导入 "fmt" 包
import "fmt"

// 常量使用示例
func const_demo() {
    // 显式类型定义
    const CST_1 = 1
    // 隐式类型定义
    const CST_2 int = 2
    // 多重赋值
    const CST_3, CST_4, CST_5 = 3, false, "abc"
    // 枚举
    const (
        Unknown = 0
        Female = 1
        Male = 2
    )
    fmt.Println(CST_1, CST_2, CST_3, CST_4, CST_5)
}

// 每一个可执行程序必须包含 main 函数
func main() {
    const_demo()
}
