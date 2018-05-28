package main

import "fmt"
import "reflect"

func single_switch_demo(n int) {
    grade := "D"
    switch n {
        case 90: grade =  "A"
        case 60, 70: grade = "B"
        default: grade = "NA"
    }
    fmt.Println(grade)
}

func cond_switch_demo(n int) {
    // 可以看到 go 语言的 switch 自带 break
    switch {
    case n < 60:
        fmt.Println("不及格")
    case n < 80:
        fmt.Println("良好")
    default:
        fmt.Println("优秀")
    }
}

// 展示 type switch 用法
type Bag_1 struct {
    key string
}
type Bag_2 struct {
    key int
}
func type_switch_demo(b interface{}) {
    switch t := b.(type) {
    case Bag_1:
        fmt.Println("b1.(type):", reflect.TypeOf(t.key))
    case Bag_2:
        fmt.Println("b2.(type):", reflect.TypeOf(t.key))
    default:
        fmt.Println("NA")
    }
}

func main() {
    // switch 条件为单个值
    single_switch_demo(61)
    single_switch_demo(60)
    single_switch_demo(70)
    single_switch_demo(90)

    // switch 条件为表达式
    cond_switch_demo(59)
    cond_switch_demo(60)
    cond_switch_demo(70)
    cond_switch_demo(90)

    // type switch
    var x1 interface{}
    var x2 interface{}
    x1 = Bag_1{key: "1"}
    x2 = Bag_2{key: 2}
    type_switch_demo(x1)
    type_switch_demo(x2)
}
