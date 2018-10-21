package main

import "fmt"
import "sort"

func main() {
    arr_1 := []int{3, 1, 2}
    sort.Ints(arr_1)
    fmt.Println(arr_1)

    arr_2 := [][]int{{3, 1}, {1, 1}, {2, 1}}
    sort.Slice(arr_2, func(i, j int) bool {return arr_2[i][0] < arr_2[j][0]})
    fmt.Println(arr_2)
}
