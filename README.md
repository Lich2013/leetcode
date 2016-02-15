# Leetcode


### Set Matrix Zeroes
    
   - 第一种
    
     - 通过一次遍历记录所有为0的索引(Python中`enumerate()`输出当前列表的索引)
     - 再遍历一次, 根据记录的索引进行置0
     
   - 第二种
    
     - 通过一次遍历所有为0的索引, 设置当前索引的行列的第一个数为0, 作为标记, 如`a[9][9]`为0, 所以设置`a[0][9]`,`a[9][0]`为0
     - 再遍历一次, 根据标识的索引进行置0
     
### Min Stack

   - 数据结构为两个栈, 一个记录最小值的栈, 一个是存放正常压栈数据
    
   - 入栈的时候判断新加入的数是否**小于或等于**最小值栈里的top
    
   - 出栈时判断出栈数字和最小栈里的是否相等
    
### Evaluate Reverse Polish Notation

   - 逆波兰的后半截实现
    
### Linked List Cycle

   - 快慢指针
   
### Linked List Cycle II

   - 快慢指针再加个初始指针
   
   - 慢指针到链表开始位置时, 快指针总是比他快k步(每次移动快1步, 移动k次), 第一次相遇的时候快慢指针位置距离链表起始位置差k步即在n-k的位置(链表环长度为n)
   
### Majority Element

   - 多数投票算法
    
   - 出现超过n/2次, 说明**最多**只有一个数(题中已假设一定存在这个数)

   - 两个变量记录出现次数和当前值, 遍历到相同值就++, 不同就--, 为0就重新赋值, 超过n/2次的数存在的话出现次数一定大于0
   
### Majority Element II

   - 类似前一题
   
   - 出现超过n/3次, 说明**最多**只有两个数(**题中不一定存在这些数!**)
   
   - 类似前面, 不过注意赋值时两个变量存的数不一样才赋值
   
### Jump Game II

   - 贪心算法
   
   - 一边遍历, 一边比较取最大的, 好像懂了....
   
### Reverse Linked List II

   - 反转链表
   
   - 把链表看成三部分, 中间的部分反转, 然后和前面后面连起来
   
   - 第一个节点作为pre节点(上一次操作节点), 第二个节点作为当前current节点, 然后可以拿到next节点, 将第二个节点(current)指向第一个节点(pre), 然后第二个节点就变成了pre节点了, next节点就是current节点了, 同理继续向下操作, 最后的时候, 注意头指针是指向反转后的链表的最后一个节点, 把头指针指向当前pre节点(反转前最后一个节点), 链表反转完成
   
   - 注意特殊处理从第一个位置就开始反转的情况 
   
### Climbing Stairs

   - 斐波那契数列的for循环实现
    
### Minimum Path Sum

   - 动态规划问题
   
   - 先求得第一行和第一列到达每个位置的总和, 再计算每个其他a[i][j] + min(a[i-1][j], a[i][j-1]), 递推到最后即为最短路径
   
### Merge Sorted Array

   - 本质上两个指针, 倒着找, 这样把时间降为O(n)
   
### Add Digits

   - 数根
   
### Invert Binary Tree

   - 反转二叉树
   
   - 非递归方式
   
   - 先pop当前节点, 交换当前节点的左右子节点, 如果左右子节点存在, 将左右子节点压入栈利用栈来保存这些还没遍历的节点

### Power of Three

   - 题中给出的是int类型, 可知长度为4个字节, 即32位, 除去符号位, 还剩31位, 2^30 < 3^19 < 2^31, 所以3^19总是3的幂的倍数
   
### Minimum Depth of Binary Tree

   - 二叉树的最小深度
   
   - 非递归
   
   - 类似层次遍历, 每层作为一个数组来进行遍历, 所以每层+1不会多
   
   
### Verify Preorder Serialization of a Binary Tree

   - 根据二叉树的性质来计算
   
           设节点: 度为0为n0, 度为1为n1, 度为2为n2, 总节点为n, #个数为n#
           
           n = n0 + n1 + n2
           n0 = n2 + 1
           n# = 2 * n0 + n1
           n# = n0 + n2 + n1 + 1
           n# = n + 1
           
           
   
   - 按照构建二叉树的顺序, 因为开始时是空树, 所以初始化为空节点个数为1, 增加一个非#节点, 相当于减少一个空节点, 同时增加两个空节点, 增加一个#节点就相当于减少一个空节点, 所以最后总是满足结果为0 
   
### Reverse Nodes in k-Group

   - 把一个链表分成几部分进行反转, 每次记录每部分的尾部, 下一次尾部连接头部
   
### Length of Last Word

   - 自己想到个巧妙的方法, tmp既做计数器又做flag           
           
           
           
           
           
           
           
           
           
           
