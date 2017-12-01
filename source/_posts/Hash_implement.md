---
title: Hash 实现
categories: 编程语言
tags:
  - c 语言
---

{% note default %}
C 语言标准库中未实现 hashtable, 在编程练习时经常使用该数据结构，以备不时之需
{% endnote %}

<!--more-->

---

## 实现如下：

```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef unsigned char      u8_t;
typedef char               s8_t;
typedef unsigned short     u16_t;
typedef signed short       s16_t;
typedef unsigned int       u32_t;
typedef signed int         s32_t;
typedef long long          s64_t;
typedef unsigned long long u64_t;
typedef s32_t err_t;
typedef unsigned long ulong_t;

void* xxx_malloc(int size)
{
    void* ret = malloc(size);
    printf("malloc %p\n", ret);
    return ret;
}
void xxx_free(void* ptr)
{
    printf("free %p\n", ptr);
    free(ptr);
}

#define offset_of(type, member) ((unsigned long)&((type *)0)->member)

#define container_of(ptr, type, member)             \
        ((type *)((unsigned char *)ptr - offset_of(type,member)))

#define hlist_entry(ptr, type, member) container_of(ptr,type,member)

#define hlist_for_each(pos, head) for (pos = (head)->first; pos; pos = pos->next)

#define hlist_for_each_safe(pos, n, head) \
    for (pos = (head)->first; pos && (n = pos->next, 1); pos = n)

#define hlist_for_each_entry(type_pos, ptr, pos, head, member)             \
    for (pos = (head)->first; pos  && (ptr = hlist_entry(pos, type_pos, member), 1);  pos = pos->next)

#define hlist_for_each_entry_safe(type_pos, tpos, pos, n, head, member) 		 \
	for (pos = (head)->first;					 \
	     pos && ({ n = pos->next; 1; }) && 				 \
		({ tpos = hlist_entry(pos, type_pos, member); 1;}); \
	     pos = n)

#define INIT_HLIST_HEAD(ptr) ((ptr)->first = NULL)

struct hlist_head {
    struct hlist_node *first;
};

struct hlist_node {
    struct hlist_node *next, **pprev;
};


static inline void hlist_add_head(struct hlist_node *n, struct hlist_head *h)
{
    struct hlist_node *first = h->first;
    n->next = first;
    if (first)
        first->pprev = &n->next;
    h->first = n;
    n->pprev = &h->first;
}
static inline void INIT_HLIST_NODE(struct hlist_node *h)
{
    h->next = NULL;
    h->pprev = NULL;
}

static inline int hlist_unhashed(const struct hlist_node *h)
{
    return !h->pprev;
}

static inline int hlist_empty(const struct hlist_head *h)
{
    return !h->first;
}

static inline void __hlist_del(struct hlist_node *n)
{
    struct hlist_node *next = n->next;
    struct hlist_node **pprev = n->pprev;
    *pprev = next;
    if (next)
        next->pprev = pprev;
}

static inline void hlist_del_init(struct hlist_node *n)
{
	if (!hlist_unhashed(n)) {
		__hlist_del(n);
	}
}

typedef struct _xxx_hash_bucket_head {
    struct hlist_head chain;           // hash 桶的头结点
} xxx_hash_bucket_head;

typedef struct _xxx_hashtable {
    xxx_hash_bucket_head *tbl;         // hash 表中的 hash 桶
    s8_t *name;                        // hash 表的名称，未使用
    u32_t cnt;                         // 保存关键字 hash 后的最大值
    u32_t element_cnt;                 // 记录当前 hash 表中的元素数量
    u32_t offset;                      // hlist_node 成员与包含该成员结构体的地址偏移
    u32_t (*hash)(void *);             // 关键字的 hash 算法函数
    s32_t (*compare)(void *, void *);  // 元素的比较函数
    void (*destroy)(void *);           // 反初始化时对每个元素的反初始化操作函数
} xxx_hashtable_t;

void *hashtable_init(s8_t *name,
        u32_t cnt,
        u32_t offset,
        u32_t (*hash)(void *),
        s32_t (*compare)(void *, void *),
        void (*destroy)(void *))
{
    xxx_hashtable_t *tbl;
    u32_t i;
    u32_t size;

    assert(!(cnt & (cnt - 1)));
    assert(NULL != hash);
    assert(NULL != compare);

    if (NULL == (tbl = (xxx_hashtable_t*)xxx_malloc(sizeof(xxx_hashtable_t)))) {
        return NULL;
    }

    size = sizeof(xxx_hash_bucket_head) * cnt;
    if (NULL == (tbl->tbl = xxx_malloc(size))) {
        xxx_free(tbl);
        return NULL;
    }

    tbl->name = name;
    tbl->cnt = cnt;
    tbl->element_cnt = 0;
    tbl->offset = offset;
    tbl->hash = hash;
    tbl->compare = compare;
    tbl->destroy = destroy;


    for (i = 0; i < cnt; i++) {
        INIT_HLIST_HEAD(&(tbl->tbl[i].chain));
    }

    return tbl;
}

void hashtable_fini(void *tbl)
{
    u32_t i;
    struct hlist_node *pos, *n;
    xxx_hash_bucket_head *h;
    u32_t size;
    u32_t offset;

    if (NULL == tbl) {
        return;
    }

    offset = ((xxx_hashtable_t *)tbl)->offset;
    for (i = 0; i < ((xxx_hashtable_t *)tbl)->cnt; i++) {
        h = &((xxx_hashtable_t *)tbl)->tbl[i];
        hlist_for_each_safe(pos, n, &h->chain) {
            if (NULL != ((xxx_hashtable_t *)tbl)->destroy) {
                ((xxx_hashtable_t *)tbl)->destroy((void *)((u8_t *)pos - offset));
            }
        }
    }

    size = sizeof(struct hlist_head) * ((xxx_hashtable_t *)tbl)->cnt;
    xxx_free(((xxx_hashtable_t *)tbl)->tbl);
    xxx_free(tbl);
}

static inline void *hashtable_find(void *tbl, void *elem)
{
    struct hlist_node *pos;
    xxx_hash_bucket_head *h;
    u32_t hash;

    hash = ((xxx_hashtable_t *)tbl)->hash(elem);

    assert(hash < ((xxx_hashtable_t *)tbl)->cnt);

    h = &((xxx_hashtable_t *)tbl)->tbl[hash];
    hlist_for_each(pos, &h->chain) {
        if (!((xxx_hashtable_t *)tbl)->compare(elem, (u8_t *)pos - ((xxx_hashtable_t *)tbl)->offset)) {
            return (void *)((u8_t *)pos - ((xxx_hashtable_t *)tbl)->offset);
        }
    }

    return NULL;
}

static err_t hashtable_insert(void* hashtable, void* elem)
{
    struct hlist_node* pos;
    xxx_hash_bucket_head* bucket;
    u32_t hash;

    hash = ((xxx_hashtable_t *)hashtable)->hash(elem);
    assert(hash < ((xxx_hashtable_t *)hashtable)->cnt);

    bucket = &((xxx_hashtable_t *)hashtable)->tbl[hash];
    hlist_for_each(pos, &bucket->chain) {
        if (!((xxx_hashtable_t *)hashtable)->compare(elem, (u8_t *)pos - ((xxx_hashtable_t *)hashtable)->offset)) {
            return -1;
        }
    }

    hlist_add_head((struct hlist_node *)((u8_t *)elem + ((xxx_hashtable_t *)hashtable)->offset), &bucket->chain);
    ((xxx_hashtable_t *)hashtable)->element_cnt++;

    return 0;
}

static inline void hashtable_delete(void *hashtable, void *elem)
{
    xxx_hash_bucket_head *bucket;
    u32_t hash;

    hash = ((xxx_hashtable_t *)hashtable)->hash(elem);
    assert(hash < ((xxx_hashtable_t *)hashtable)->cnt);
    bucket = &((xxx_hashtable_t *)hashtable)->tbl[hash];
    hlist_del_init((struct hlist_node *)((u8_t *)elem + ((xxx_hashtable_t *)hashtable)->offset));
    if (NULL != ((xxx_hashtable_t *)hashtable)->destroy) {
        ((xxx_hashtable_t *)hashtable)->destroy(elem);
    }
    ((xxx_hashtable_t *)hashtable)->element_cnt--;
}

/* Hash map 实现 */
#define MAP_BUCKET_CNT (1 << 6)

typedef struct _str_map_t{
    int m_value;
    struct hlist_node hash_node;
} str_map_t;

/* 创建 str_map_t 对象 */
str_map_t* str_map_init();

/* 销毁 str_map_t 对象 */
void str_map_fini(str_map_t* p_str_map);

/* 插入元素 */
void str_map_insert(str_map_t* p_str_map);

/* 删除元素 */
void str_map_erase(str_map_t* p_str_map);

/* 查找元素 */
void str_map_erase(str_map_t* p_str_map);

/* 测试函数 */
typedef struct _hlist_demo_t{
    int m_value;
    struct hlist_node hash_node;
} hlist_demo_t;

static u32_t demo_hash(void *pkt)
{
    return (u32_t)(((hlist_demo_t*)pkt)->m_value) % BUCKET_CNT;
}

static s32_t demo_compare(void *pkt, void *pkt2)
{
    if (((hlist_demo_t*)pkt)->m_value == ((hlist_demo_t*)pkt2)->m_value) {
        return 0;
    }
    return -1;
}

static void demo_destroy(void *arg)
{
    xxx_free(arg);
}

int main()
{
}

```




