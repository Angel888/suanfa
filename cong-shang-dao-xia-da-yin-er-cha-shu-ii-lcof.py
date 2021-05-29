class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:  #todo 哪里有问题？
        #todo 到底打印的是节点还是节点的值
        if not root:
            return []
        layer=[root]
        res=[]
        while layer:
            res.append(layer)
            print("res---",res)
            new_layer=[]
            for i in layer:
                if not i:
                    continue
                if i.left:
                    new_layer.append(i.left)
                if i.right:
                    new_layer.append(i.right)
            layer=new_layer
        return res
