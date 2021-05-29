# https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
from nltk import collections


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        一个节点一直一直往下寻找next或random，直到最后一层返回
        vistied 是记录新旧两表的对应关系
        :param head:
        :return:
        """
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)  #todo 如果random是None
            return copy
        visited = {}
        return dfs(head)

    def copyRandomList1(self, head: 'Node') -> 'Node':
        """
        广度遍历即处理一个一个节点时，先创造节点并利用哈希表存储该节点应有的关系，然后再关联
        :param head:
        :return:
        """
        visited = {}

        def bfs(head):
            if not head: return head
            clone = Node(head.val, None, None)  # 创建新结点
            queue = collections.deque()
            queue.append(head)
            visited[head] = clone
            while queue:
                tmp = queue.pop()
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return clone

        return bfs(head)

    def copyRandomList2(self, head: 'Node') :  #todo 为啥要使用队列而不是一个节点一个节点地处理？
        """
        广度优先
        :param head:
        :return:
        """
        if not head:
            return None
        a={}
        b=None
        while head:
            a[head] = Node(head.val)
            a[head.next]=Node(head.next.val) if head.next else None
            if not b:
                b = a[head]
            head = head.next
        for k in a.keys():
            a[k].next=a.get(k.next,None)
            a[k].random=a.get(k.random,None)
        return b
#todo 深度优先怎么做
    def copyRandomList3(self, head: 'Node'):
        """
        深度优先
        :param head:
        :return:
        """

        def dfs(n):
            if not n:
                return None
            a=Node(n.val)
            a.next=dfs(n.next)
            a.random=dfs(n.random)
            return a
        return dfs(head)  # todo   #

