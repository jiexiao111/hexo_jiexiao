package main

import "fmt"

// 枚举
type Mytype int
const (
    _ Mytype = iota
    ONE
    TWO
    THREE
    _ // 如果想跳过某个值
    FIVE
)
func enum_demo(e Mytype) {
    fmt.Println(e)
}

// 位运算
type Shift_Type int
const (
    left_shift_1 = 1 << iota // 00000001
    left_shift_2 // 00000010
    left_shift_3 // 00000100
)
func shift_demo(s Shift_Type) {
    fmt.Println(s)
}

func main() {
    // 场景一: 申明枚举变量
    enum_demo(ONE)
    // 常量是一个弱类型，所以可以作为 Mytype 传入
    enum_demo(1)
    // 以下调用会发生错误，因为类型不匹配
    // var wrong_type int = 1
    // enum_demo(wrong_type)

    // 场景二: 跳过某个值
    enum_demo(FIVE)

    // 场景三：表达式
    shift_demo(left_shift_1)
    shift_demo(left_shift_2)
    shift_demo(left_shift_3)
}
