package main

import "fmt"

func main() {
    // 初始化
    var countryCaptialMap map[string]string
    countryCaptialMap = make(map[string]string)

    // 赋值
    countryCaptialMap["France"] = "Pairs"
    countryCaptialMap["Italy"] = "Roman"

    // 遍历
    for country := range countryCaptialMap {
        fmt.Println(country, countryCaptialMap[country])
    }

    // 判断是否存在
    captial, flag := countryCaptialMap["China"]
    fmt.Println("flag is:", flag, "\ncaptial is:", captial)

    // 删除
    delete(countryCaptialMap, "France")
    for country := range countryCaptialMap {
        fmt.Println(country, countryCaptialMap[country])
    }
}
