# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:
        allnodes=set()
        hasParent=set()
        for p,ch,isLeft in desc:
            allnodes.add(p)
            allnodes.add(ch)
            hasParent.add(ch)
        root=allnodes.difference(hasParent)
        root=root.pop()
        lim=2**len(allnodes)
        d={}
        for p,ch,isLeft in desc:
            if p in d:
                d[p][abs(isLeft-1)]=ch
            else:
                d[p]=[None,None]
                d[p][abs(isLeft-1)]=ch
        for x in allnodes:
            if x not in d:
                d[x]=[None,None]
        
        root=TreeNode(root)
        i=0
        q=deque()
        q.append(root)
        while q:
            cur=q.popleft()
            cur.left=TreeNode(d[cur.val][0])
            cur.right=TreeNode(d[cur.val][1])
            if cur.left.val!=None:
                q.append(cur.left)
            else:
                cur.left=None
            if cur.right.val!=None:
                q.append(cur.right)
            else:
                cur.right=None
        return root