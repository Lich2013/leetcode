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

### Power of Two

   - 理同下题
   - 可以尝试用位运算优化 

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

### Reverse Linked List

   - 反转单链表

### Construct Binary Tree from Preorder and Inorder Traversal

   - 递归
   
        - 由于前序遍历的第一个点是树根, 所以根据树根在中序遍历中来区分左/右子树
        - 把左子树看作单独的🌲, 然后按照第一步进行判断
    
   - 非递归
   
        - 利用栈来来保存遍历前序遍历的数组, 遍历一个就加入栈, 下一个循环的时候和中序遍历的数组比较来判断是否是右子树, 相同的就pop, 因为这些已经构建了, 每次pop循环完后的, 第一次不同的时候
        - 从左向右扫描先序和中序序列，先将先序的结点入栈，以备后面要建立右结点用；然后用栈顶元素和中序扫描所在位置的值进行比较，1.如果相等，就说明后面还有右子树的结点，并设置标志，使其之后走右子树方向; 2.如果不等，就判断标志，是创建左子树还是右子树，创建之后，并让他自身进栈。

### Remove Element

   - 不用删除函数的话就用双指针一个赋值, 一个遍历
  
   - py的删除函数使用后后面所有的数据会自动前移, [1,2,3]的索引为0,1,2, 删除2就变为[1,3], 索引0,1

### Compare Version Numbers

   - 根据'.'分成几部分, 然后int比较, 理论上如果版本号超过了int, 感觉就比较难处理了, 不过实际上版本号还是没那么长...

### Binary Tree Level Order Traversal

   - 自从非递归反转了二叉树, 徒手层次遍历二叉树一次AC😂

### Bitwise AND of Numbers Range

   - 很考基础的一道题, 对位运算的认识, 学了计算机组成原理, 数电之类的就很容易做了, 就是求[m, n]的化为二进制后相同的前缀, 最多循环判断31次 //todo 可以试试按字符串的方式来比较看看和位运算来谁更快?

### Simplify Path

   - 感觉这道题应该放到easy去, 一个栈就能解决问题, 一次AC, 终端用多了还是有点好处2333

### Sqrt(x)

   - 牛顿法求平方根 
           

### Permutations

   - 全排列, 非递归, 把一个数插入每个间隔

### Search Insert Position


   - 给排序好的数组按顺序插入一个值, 实际上是类似于二分法查找相同的数, 利用二分法提高效率


### Palindrome Linked List


  - 判断是否是回文链表

  - 利用快慢指针找到中间节点(注意奇偶), 反转后半部分, 然后进行比较

### Path Sum

  - 有点DP问题和层次遍历结合的感觉, 把上一个节点的值加给它的子节点, 叶子节点存进数组里, 最后判断下就好了, 2次AC, 修改了下先判断是否是叶子节点速度就快多了

### Number of Matching Subsequences
  - 就这个实现本身O(m*n)来说还有优化空间：比如判断str的长度
  - 查了下还有其他更优雅的解决方案，复杂度是O(m+n), 当然不是类似打表这种trick的方式

### LRU Cache
  - 附上之前写的LRU，画完图来写比较清晰，口述起来真的一言难尽

### Delete Columns to Make Sorted II      
  - 删去最少的列数，让剩下的字符串以英文字典里单词的顺序排列
  - 思路是：
      	- 针对每一列，如果符合字典序，那么就保存下来，可以记为变量tmp
      	- 对于当前列，因为tmp里是按字典序保存的， 所以先比较tmp里前一列，如果不相等，因为符合字典序，那么没必要校验后面的了；如果相等，又因为符合字典序，就必须比较当前列了； 综上所述，这里其实只需要考虑前一列相等并且当前列的前者大于后者这种情况，即仅这种情况需要删除，其余的通过校验后执行第一步操作
      	- 对于第一列，我们可以假设一个空字符串作为dummy beginning，就能够不做特殊处理了