---
title: 双向链表
date: 2017-11-30 22:39:16
categories: 编程语言
tags:
  - c 语言
---

{% note default %}
OJ 常用数据结构备份
{% endnote %}

<!--more-->

---

# 双向链表
```c
#include <stdio.h>

#define prefetch(X) X
#define offset_of(type, member) ((size_t)&((type *)0)->member)
#define container_of(ptr, type, member) ((type *)((unsigned char *)ptr - offset_of(type,member)))

/* XXX list 结构体定义 */
struct list_head {
    struct list_head *next, *prev;
};

#define LIST_HEAD_INIT(name) { &(name), &(name) }

/* XXX 局部、全局 list 初始化接口 */
#define LIST_HEAD(name) struct list_head name = LIST_HEAD_INIT(name)

/* XXX 初始化已经存在的 list 头节点对象 */
static inline void INIT_LIST_HEAD(struct list_head *list)
{
    list->next = list;
    list->prev = list;
}

/* 插入元素的内部实现 */
static inline void __list_add(struct list_head *nnew,
        struct list_head *prev,
        struct list_head *next)
{
    next->prev = nnew;
    nnew->next = next;
    nnew->prev = prev;
    prev->next =nnew;
}

/* XXX 将元素插入链表头部 */
static inline void list_add(struct list_head *nnew, struct list_head *head)
{
    __list_add(nnew, head, head->next);
}

/* XXX 将元素插入链表尾部 */
static inline void list_add_tail(struct list_head *nnew, struct list_head *head)
{
    __list_add(nnew, head->prev, head);
}

/* 删除元素的内部实现 */
static inline void __list_del(struct list_head * prev, struct list_head * next)
{
    next->prev = prev;
    prev->next = next;
}

/* XXX 删除指定元素 */
static inline void list_del(struct list_head *entry)
{
    __list_del(entry->prev, entry->next);
}

/* XXX 判断该节点是否为尾节点 */
static inline int list_is_last(const struct list_head *list,
        const struct list_head *head)
{
    return list->next == head;
}

/* XXX 判断链表是否为空，仅检查后向指针 */
static inline int list_empty(const struct list_head *head)
{
    return head->next == head;
}

/* XXX 判断链表中是否仅有一个元素 */
static inline int list_is_singular(const struct list_head *head)
{
    return !list_empty(head) && (head->next == head->prev);
}

#define list_entry(ptr, type, member) container_of(ptr, type, member)

#define list_first_entry(ptr, type, member) list_entry((ptr)->next, type, member)

#define list_last_entry(ptr, type, member) list_entry((ptr)->prev, type, member)

#define list_for_each_entry(type_pos, pos, head, member)                  \
    for (pos = list_entry((head)->next, type_pos, member);                \
            &pos->member != (head);                                       \
            pos = list_entry(pos->member.next, type_pos, member))

#define list_for_each_entry_safe(type_pos, pos, ptr, head, member)        \
    for (pos = list_entry((head)->next, type_pos, member),                \
            ptr = list_entry(pos->member.next, type_pos, member);         \
            &pos->member != (head);                                       \
            pos = ptr, ptr = list_entry(ptr->member.next, type_pos, member))

#define list_for_each_entry_reverse(type_pos, pos, head, member)          \
        for (pos = list_entry((head)->prev, type_pos, member);            \
                &pos->member != (head);                                   \
                pos = list_entry(pos->member.prev, type_pos, member))

#define list_for_each_entry_safe_reverse(type_pos, pos, n, head, member)  \
    for (pos = list_entry((head)->prev, type_pos, member),                \
            n = list_entry(pos->member.prev, type_pos, member);           \
            &pos->member != (head);                                       \
            pos = n, n = list_entry(n->member.prev, type_pos, member))

/* 示例 */
#include <stdlib.h>

typedef struct _list_demo_t{
    int value;
    struct list_head node;
} list_demo_t;

int main()
{
    LIST_HEAD (local_list);
    printf("list_empty [%d]\n", list_empty(&local_list));

    list_demo_t* list_node_1 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_1->value = 1;
    list_demo_t* list_node_2 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_2->value = 2;
    list_demo_t* list_node_3 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_3->value = 3;
    list_demo_t* list_node_4 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_4->value = 4;
    list_demo_t* list_node_5 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_5->value = 5;
    list_demo_t* list_node_6 = (list_demo_t*)malloc(sizeof(list_demo_t));
    list_node_6->value = 6;
    list_add(&list_node_1->node, &local_list);
    list_add(&list_node_2->node, &local_list);
    list_add(&list_node_3->node, &local_list);
    list_add_tail(&list_node_4->node, &local_list);
    list_add_tail(&list_node_5->node, &local_list);
    list_add_tail(&list_node_6->node, &local_list);
    printf("list_empty [%d]\n", list_empty(&local_list));

    list_demo_t* tmp;
    list_demo_t* for_safe;
    printf("list_for_each_entry\n");
    list_for_each_entry(list_demo_t, tmp, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }

    printf("list_first_entry [%d]\n", list_first_entry(&local_list, list_demo_t, node)->value);
    list_del(&list_first_entry(&local_list, list_demo_t, node)->node);
    printf("list_first_entry [%d]\n", list_first_entry(&local_list, list_demo_t, node)->value);
    printf("list_last_entry [%d]\n", list_last_entry(&local_list, list_demo_t, node)->value);
    list_del(&list_last_entry(&local_list, list_demo_t, node)->node);
    printf("list_last_entry [%d]\n", list_last_entry(&local_list, list_demo_t, node)->value);

    printf("list_for_each_entry_safe\n");
    list_for_each_entry_safe(list_demo_t, tmp, for_safe, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }
    printf("list_for_each_entry_safe_reverse\n");
    list_for_each_entry_safe_reverse(list_demo_t, tmp, for_safe, &local_list, node)
    {
        list_del(&tmp->node);
        printf("[%d]\n", tmp->value);
        free(tmp);
    }
    printf("list_for_each_entry_reverse\n");
    list_for_each_entry_reverse(list_demo_t, tmp, &local_list, node)
    {
        printf("[%d]\n", tmp->value);
    }
}
```

