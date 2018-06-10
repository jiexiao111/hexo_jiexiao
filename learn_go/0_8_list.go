package main

import "fmt"
import "container/list"

func diplay_list(lst *list.List) {
    // Front 返回第一个节点，Next 正序的下一个节点
    for x := lst.Front(); x != nil; x = x.Next() {
        fmt.Print(x.Value)
    }
    fmt.Println()
}

func diplay_list_reverse(lst *list.List) {
    // Back 返回最后一个节点，Prev 倒序的下一个节点
    for x := lst.Back(); x != nil; x = x.Prev() {
        // NOTE 注意，x.Value 的类型转换
        var tmp int = x.Value.(int)
        fmt.Print(tmp)
    }
    fmt.Println()
}

func main() {
    // New 创建一个 list
    lst := list.New()
    
    fmt.Print("PushBack: ")
    for i := 0; i < 5; i++ {
        lst.PushBack(i)
    }
    diplay_list(lst)

    fmt.Print("Reverse display: ")
    diplay_list_reverse(lst)

    fmt.Println("Len: ", lst.Len())

    fmt.Print("PushFront: ")
    for i := 0; i < 5; i++ {
        lst.PushFront(i)
    }
    diplay_list(lst)

    fmt.Print("InsertAfter: ")
    node := lst.InsertAfter(6, lst.Front())
    diplay_list(lst)

    fmt.Print("InsertBefore: ")
    node2 := lst.InsertBefore(7, node)
    diplay_list(lst)

    fmt.Print("Remove: ")
    lst.Remove(node2)
    diplay_list(lst)

    fmt.Print("MoveAfter: ")
    lst.MoveAfter(node, lst.Front())
    diplay_list(lst)

    fmt.Print("MoveBefore: ")
    lst.MoveBefore(node, lst.Back())
    diplay_list(lst)

    fmt.Print("MoveToBack: ")
    lst.MoveToBack(node)
    diplay_list(lst)

    fmt.Print("MoveToFront: ")
    lst.MoveToFront(node)
    diplay_list(lst)

    fmt.Print("lst2: ")
    lst2 := list.New()
    for i := 7; i < 10; i++ {
        lst2.PushBack(i)
    }
    diplay_list(lst2)

    fmt.Print("PushBackList: ")
    lst.PushBackList(lst2)
    diplay_list(lst)

    fmt.Print("PushFrontList: ")
    lst.PushFrontList(lst2)
    diplay_list(lst)

    fmt.Print("Init: ")
    lst.Init()
    diplay_list(lst)
}
