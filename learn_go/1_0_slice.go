package main

import "fmt"

func main() {
    // 定义空切片
    var nums []int
    fmt.Println("len:", len(nums))

    // 通过 make 创建切片
    nums_make := make([]int, 10)
    fmt.Println("nums_make:", nums_make)

    // 直接初始化
    nums_init := []int{1, 2, 3}
    fmt.Println("nums_init:", nums_init)

    // 数组初始化
    arr := [3]int{4, 5, 6}
    fmt.Println("arr:", arr)
    nums_arr := arr[1:]
    fmt.Println("nums_arr:", nums_arr)

    // 截取 [start, end)
    fmt.Println("nums_init[0:2]:", nums_init[0:2])

    // NOTE append 不会改变原始 slice
    fmt.Println("append(nums, 1):", append(nums, 1))
    fmt.Println("append(nums, 1, 2, 3):", append(nums, 1, 2, 3))
    fmt.Println("nums:", nums)

    // 合并切片
    fmt.Println("append(nums_make, nums_init...)):", append(nums_make, nums_init...))

    // 多维切片
    numRows := 3
    buf := make([][]rune, numRows)
    buf[0] = append(buf[0], 1)
    fmt.Println("multislice", buf)
}
