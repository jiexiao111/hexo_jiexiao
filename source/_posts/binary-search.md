---
title: 二分查找
date: 2017-11-30 22:35:33
categories: 编程语言
tags:
  - c 语言
---

{% note default %}
做 oj 时的常用函数
{% endnote %}

<!--more-->

---


# 二分查找
```c
int bin_find(int* nums, int numsSize, int target) {
    int hi = numsSize - 1;
    int low = 0;
    int mid;
    while (hi >= low) {
        mid = low + (hi - low) / 2;
        if (target == nums[mid]) {
            return mid;
        }
        else if (target > nums[mid]) {
            low = mid + 1;
        }
        else {
            hi = mid - 1;
        }
    }
    return -1;

}
