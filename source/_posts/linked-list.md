---
title: 链表
date: 2017-11-30 22:37:47
categories: 编程语言
tags:
  - c 语言
---

{% note default %}
OJ 常用数据结构备份
{% endnote %}

<!--more-->

---

# 单向链表

```c
#include "stdafx.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

typedef int elemType;

struct Node{
    elemType element;
    Node *next;
};

// 1. 初始化线性表，即置单链表的表头指针为空
void initList(Node *pNode)
{
    pNode = NULL;
    printf("initList 函数执行，初始化成功、n");
}

//2. 创建线性表，此函数输入负数终止读取数据
Node *createList()
{
    Node *p1,*p2,*pNode;
    p1=p2=pNode=(Node *)malloc(sizeof(Node));
    memset(p1,0,sizeof(Node));

    scanf("%d",&p1->element);
    p1->next = NULL;  //
    while(p1->element > 0)
    {
        if(NULL == pNode)
        {
            pNode = p1;
        }
        else
        {
            p2->next = p1;
        }

        p2=p1;

        p1=(Node *)malloc(sizeof(Node));
        memset(p1,0,sizeof(Node));

        scanf("%d",&p1->element);
        p1->next = NULL;  //
    }

    return pNode;
}

//3. 打印链表，链表的遍历
void printList(Node *pNode)
{
    if(NULL == pNode)
    {
        printf("PrintList 函数执行，链表为空、n");
    }
    else
    {
        while(NULL != pNode)
        {
            printf("%d\t", pNode->element);
            pNode = pNode->next;
        }
    }
    printf("\n");
}

// 4. 清除线性表 L 中的所有元素，即释放单链表 L 中所有的结点，使之成为一个空表
int clearList(Node *pNode)
{
    Node *pNext;

    while(NULL != pNode)
    {
        pNext = pNode->next;
        free(pNode);
        pNode = pNext;
    }

    return 1;
    //printf("清空链表成功！\n");
}

// 5. 返回单链表的长度
int sizeList(Node *pNode)
{
    int i=0;

    while(NULL != pNode)
    {
        i++;
        pNode = pNode->next;
    }

    return i;
}

// 6. 检查单链表是否为空，若为空则返回 1，否则返回 0
int isEmptyList(Node *pHead)
{
    if(pHead == NULL)
    {
        printf("isEmptyList 函数执行，链表为空、n");
        return 1;
    }
    printf("isEmptyList 函数执行，链表非空、n");

    return 0;
}

//7. 返回单链表中第 pos 个结点中的元素，若 pos 超出范围，则停止程序运行
elemType getElement(Node *pNode,int pos)
{
    int i=0;

    if(pos < 1)
    {
        printf("getElement 函数执行，pos 值非法、n");
        return 0;
    }
    if(pNode == NULL)
    {
        printf("getElement 函数执行，链表为空、n");
        return 0;
    }

    while(pNode!= NULL)
    {
        i++;
        if(i == pos)
            return pNode->element;
        pNode = pNode->next;
    }
    // 上面的 while 循环也可用 for 循环来代替


    if(i < pos)                  // 链表长度不足则退出
    {
        printf("getElement 函数执行，pos 值超出链表长度、n");
    }
    return 0;
}

// 8. 从单链表中查找具有给定值 x 的第一个元素，若查找成功则返回该结点 data 域的存储地址，否则返回 NULL
elemType *getElemAddr(Node *pNode,elemType elemValue)
{
    if(elemValue <= 0)
    {
        printf("getElemAddr 函数执行，给定值不合法、n");
        return NULL;
    }
    if(pNode == NULL)
    {
        printf("getElemAddr 函数执行，链表为空、n");
        return NULL;
    }

    while(pNode!= NULL)
    {
        if(pNode->element == elemValue)
        {
            printf("getElemAddr 函数执行，元素 %d 的地址为 0x%x\n",elemValue,&(pNode->element));
            return &(pNode->element);   // 如果不直接 return 的话，一定记得用 break 跳出循环
        }
        pNode = pNode->next;
    }

    printf("getElemAddr 函数执行，在链表中未找到 %d 值、n",elemValue);

    return NULL;
}

//9. 把单链表中第 pos 个结点的值修改为 elemValue 的值，若修改成功返回 1，否则返回 0
int modifyElem(Node *pNode,int pos, elemType elemValue)
{
    printf("modifyElem 函数执行，即将把链表的第 %d 个元素的值改为 %d\n",pos,elemValue);
    if(NULL == pNode)
    {
        printf("modifyElem 函数执行，链表为空、n");
    }
    if(pos < 1)
    {
        printf("modifyElem 函数执行，pos 值非法、n");
        return 0;
    }
    if(elemValue < 1)
    {
        printf("modifyElem 函数执行，elemValue 值非法、n");
        return 0;
    }

    int i=0;
    while(pNode != NULL)
    {
        i++;
        if(i == pos)
        {
            pNode->element = elemValue;
            return 1;
        }
        pNode = pNode->next;
    }

    if(i < pos)                  // 链表长度不足则退出
    {
        printf("modifyElem 函数执行，pos 值超出链表长度、n");
        return 0;
    }

    return 0;
}

//10. 向单链表的表头插入一个元素
int insertHeadList(Node **pNode,elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertHeadList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertHeadList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pHead,*pLast;
    pLast = *pNode;

    pHead = (Node *)malloc(sizeof(Node));
    memset(pHead,0,sizeof(Node));
    pHead->element = elemInserted;
    pHead->next = pLast;

    *pNode = pHead;
    return 1;
}

// 11. 向单链表的末尾添加一个元素
int insertLastList(Node **pNode,elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertLastList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertLastList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pLast,*pTemp;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pLast = (Node *)malloc(sizeof(Node));
    memset(pLast,0,sizeof(Node));
    pLast->element = elemInserted;
    pLast->next = NULL;

    // 循环链表至最后一个节点
    while(pTemp->next != NULL)
    {
        pTemp = pTemp->next;
    }
    // 把新增节点加入到链表中
    pTemp->next = pLast;

    return 1;
}

//12. 向单链表中第 pos 个结点位置插入元素为 x 的结点，若插入成功返回 1，否则返回 0
int insertList(Node **pNode, int pos, elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertList 函数执行，elemInserted 值非法、n");
        return 0;
    }
    if(pos < 1)
    {
        printf("insertList 函数执行，pos 值非法、n");
        return 0;
    }

    Node *pInserted,*pTemp, *pLast;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pInserted = (Node *)malloc(sizeof(Node));
    memset(pInserted,0,sizeof(Node));
    pInserted->element = elemInserted;
    pInserted->next = NULL;  // 先赋值为 null

    // 循环链表至 pos 节点
    int i = 0;
    while(pTemp->next != NULL)
    {
        i = i + 1;
        if(i == pos)
        {
            pLast->next = pInserted;  // 让上一个节点的 next 指向插入节点
            pInserted->next = pTemp;  // 让插入节点的 next 指向下一节点
            break;
        }
        pLast = pTemp;  // 记住上一个节点的位置
        pTemp = pTemp->next;
    }

    return 1;
}

//13. 从单链表中删除表头结点，并把该结点的值返回，若删除失败则停止程序运行
int deleteHeadList(Node **pNode)
{
    int currVal;
    Node *pTemp;

    if(NULL == *pNode)
    {
        printf("DeleteHeadList 函数执行，链表为空、n");
        return 0;
    }

    pTemp = *pNode;
    currVal = (*pNode)->element;
    *pNode = (*pNode)->next;

    pTemp->next = NULL;  // 将头节点的 next 指针置为 NULL
    free(pTemp);

    return currVal;
}

//14. 从单链表中删除表尾结点并返回它的值，若删除失败则停止程序运行
int deleteLastList(Node **pNode)
{
    int currVal;
    Node *pTemp,*pLast;

    if(NULL == *pNode)
    {
        printf("DeleteLastList 函数执行，链表为空、n");
        return 0;
    }

    pTemp = *pNode;
    while(pTemp->next != NULL)
    {
        pLast = pTemp;
        pTemp = pTemp->next;
    }

    pLast->next = NULL;
    currVal = pTemp->element;

    free(pTemp);

    return currVal;
}
//15. 从单链表中删除第 pos 个结点并返回它的值，若删除失败则停止程序运行
int deleteList(Node **pNode, int pos)
{
    int currVal, i;
    Node *pTemp,*pLast,*pNext;

    if(NULL == *pNode)
    {
        printf("DeleteLastList 函数执行，链表为空、n");
        return 0;
    }
    if(pos < 1)
    {
        printf("DeleteList 函数执行，pos 值非法、n");
        return 0;
    }

    pTemp = *pNode;
    i = 0;
    while(pTemp != NULL)
    {
        i = i + 1;
        if(i == pos)
        {
            break;
        }
        pLast = pTemp;
        pTemp = pTemp->next;
    }
    pNext = pTemp;
    pNext = pNext->next;
    pLast->next = pNext;
    currVal = pTemp->element;

    free(pTemp);

    return currVal;
}

//16. 从单链表中删除值为 x 的第一个结点，若删除成功则返回 1, 否则返回 0
int deleteXList(Node **pNode, elemType elemVal)
{
    Node *pTemp,*pLast,*pNext;

    if(NULL == *pNode)
    {
        printf("DeleteXList 函数执行，链表为空、n");
        return 0;
    }
    if(elemVal < 1)
    {
        printf("DeleteXList 函数执行，elemVal 值非法、n");
        return 0;
    }

    pTemp = *pNode;
    int i = 0;
    while(pTemp != NULL)
    {
        if(pTemp->element == elemVal)
        {
            i = 1;
            break;
        }
        pLast = pTemp;
        pTemp = pTemp->next;
    }
    if(i == 0)
    {
        printf("DeleteXList 函数执行，链表中没有值为 %d 的节点、n",elemVal);
        return 0;
    }
    pNext = pTemp;
    pNext = pNext->next;
    pLast->next = pNext;

    free(pTemp);

    return 1;
}

//17. 交换 2 个元素的位置
int exchangeList(Node **pNode, int pos1, int pos2)
{
    if(NULL == *pNode)
    {
        printf("exchangeList 函数执行，链表为空、n");
        return 0;
    }
    if(pos1 < 1 || pos2 < 1)
    {
        printf("exchangeList 函数执行，pos 值非法、n");
        return 0;
    }

    Node *pTemp, *pFirst, *pSecond;
    pTemp = *pNode;
    int i = 0;
    while(pTemp != NULL)
    {
        i++;
        if(i == pos1)
            pFirst = pTemp;
        else if(i == pos2)
            pSecond = pTemp;

        pTemp = pTemp->next;
    }

    int p;
    p = pFirst->element;
    pFirst->element = pSecond->element;
    pSecond->element = p;
}

//18. 将单链表进行排序
int sortList(Node **pNode)
{
    if(NULL == *pNode)
    {
        printf("sortList 函数执行，链表为空、n");
        return 0;
    }

    Node *pTemp;
    pTemp = *pNode;

    int Listsize = sizeList(*pNode);

    // 循环：用 for 循环来取代指针循环，因为指针循环一次后，下次起始的指针将自动转到下一节点，而我们还想从第一个元素开始
    for(int i=0; i < Listsize; i++)
    {
        Node *pCurr, *pLast;
        pCurr = pLast = pTemp;

        for(int k=0; k < Listsize-i; k++)
        {
            int p = 0;

            if(pLast->element < pCurr->element)
            {
                p = pLast->element;
                pLast->element = pCurr->element;
                pCurr->element = p;
            }
            pLast = pCurr;
            pCurr = pCurr->next;
        }
    }
}

//19. 向有序单链表中插入元素 x 结点，使得插入后仍然有序 , 假设现在已知一个升序的单链表
int insertXList(Node **pNode, elemType elemInserted)
{
    if(NULL == *pNode)
    {
        printf("insertList 函数执行，链表为空、n");
        return 0;
    }
    if(elemInserted < 1)
    {
        printf("insertList 函数执行，elemInserted 值非法、n");
        return 0;
    }

    Node *pInserted,*pTemp, *pLast;
    pTemp = *pNode;   // 把*pNode 先赋值给 pTemp，后面的操作（例如循环链表到最后一个节点）主要是对 pTemp 进行操作，否则返回*pNode 的时候，将返回链表*pNode 在当前指针后面的部分，而不是整个链表。
    // 因为 pTemp 与*pNode 指向同一个链表，所以对 pTemp 进行节点改动即是对*pNode 作改动

    pInserted = (Node *)malloc(sizeof(Node));
    memset(pInserted,0,sizeof(Node));
    pInserted->element = elemInserted;
    pInserted->next = NULL;  // 先赋值为 null

    // 寻找该插入的节点
    while(pTemp->next != NULL)
    {
        if(pTemp->element > elemInserted)
        {
            pLast->next = pInserted;  // 让上一个节点的 next 指向插入节点，注意：如果该节点是第一节点，没有上一个节点呢？
            pInserted->next = pTemp;  // 让插入节点的 next 指向下一节点
            break;
        }
        pLast = pTemp;  // 记住上一个节点的位置
        pTemp = pTemp->next;
    }

    return 1;
}

void main()
{
    Node *pList=NULL;
    int length = 0;

    initList(pList);       // 链表初始化
    printList(pList);       // 遍历链表，打印链表

    pList=createList(); // 创建链表
    printList(pList);

    sizeList(pList);        // 链表的长度

    isEmptyList(pList);     // 判断链表是否为空链表

    elemType posElem;
    posElem = getElement(pList,3);  // 获取第三个元素，如果元素不足 3 个，则返回 0
    printf("getElement 函数执行，位置 3 中的元素为 %d\n",posElem);
    printList(pList);

    getElemAddr(pList,5);   // 获得元素 5 的地址

    modifyElem(pList,4,1);  // 将链表中位置 4 上的元素修改为 1
    printList(pList);

    insertHeadList(&pList,12);   // 表头插入元素 12
    printList(pList);

    insertLastList(&pList,10);  // 表尾插入元素 10
    printList(pList);

    insertList(&pList,2,11);  // 第 2 个节点插入元素 11
    printList(pList);

    deleteHeadList(&pList);  // 删除表头节点
    printList(pList);

    deleteLastList(&pList);  // 删除表尾节点
    printList(pList);

    deleteList(&pList,2);  // 删除第 2 个节点
    printList(pList);

    deleteXList(&pList,3);  // 删除值为 3 的第一个节点
    printList(pList);

    exchangeList(&pList,2,3);  // 第 2 个节点与第 3 个节点的值进行交换
    printList(pList);

    sortList(&pList);  // 对单链表进行冒泡排序
    printList(pList);

    insertXList(&pList,11);  // 向有序链表中插入一个元素 11，使得插入后的链表仍然有序
    printList(pList);

    clearList(pList);       // 清空链表
    //system("pause");
}
```
