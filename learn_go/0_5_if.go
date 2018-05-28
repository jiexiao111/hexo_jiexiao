package main

import "fmt"

func if_demo(n int) {
    if n < 3 {
        fmt.Println("condition 1")
    } else {
        if n < 5 {
            fmt.Println("condition 2")
        } else {
            fmt.Println("condition 3")
        }
    }
}
func main() {
    // if 示例
    if_demo(2)
    if_demo(4)
    if_demo(6)
}
