package main

import "fmt"

type Phone interface {
    call()
}

type NokiaPhone struct {
    name string
}

type IPhone struct {
    name string
}

func (nokia NokiaPhone) call() {
    fmt.Printf("I am %s.\n", nokia.name)
}

func (iphone IPhone) call() {
    fmt.Printf("I am %s.\n", iphone.name)
}

func (nokia NokiaPhone) set_name() {
    nokia.name = "My nokia."
}

func (iphone *IPhone) set_name() {
    iphone.name = "My IPhone."
}

func main() {
    // 展示多态
    var phone Phone
    phone = NokiaPhone{"Nokia"}
    phone.call()
    phone = IPhone{"IPhone"}
    phone.call()

    // 类的方法引用传参的方法，可以看到 IPhone 改变了而 Nokia 未改变
    nphone := NokiaPhone{"Nokia"}
    iphone := IPhone{"IPhone"}
    nphone.set_name()
    iphone.set_name()
    fmt.Println(iphone.name)
    fmt.Println(nphone.name)
}
