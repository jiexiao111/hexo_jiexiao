package main
 
import "fmt"


func main() {
    arr := []string{"a", "b", "c"}

    for i := 0; i < len(arr); i++ {
        fmt.Println(arr[i])
    }

    for idx, val := range arr {
        // 注意 val 的地址不会变化
        fmt.Println(idx, val, &val)
    }

    for idx := range arr {
        fmt.Println(idx)
    }
}
