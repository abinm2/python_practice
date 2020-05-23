        #      A
        #       /   \
        #      B     C
        #     / \   / \
        #    D   E F   G
        #   /     / \
        #  H     I   J
        #       /     \
        #      K       L
        #     / \     / \
        #    M   N   O   P
class NewNode: 
    def __init__(self, key): 
        self.key = key  
        self.left = self.right = None

class NearestLeaf:
    def __findLeafDown(self, root, lev, minDist,val):  
        if (root == None):  
            return
        if (root.left == None and root.right == None): 
            if (lev < (minDist[0])):  
                minDist[0] = lev
                val=root.key  
            return
        self.__findLeafDown(root.left, lev + 1, minDist)  
        self.__findLeafDown(root.right, lev + 1, minDist) 
  

    def __findThroughParent(self, root, x, minDist,val):  
        if (root == None): 
            return -1
        if (root == x): 
            return 0
   
        l = self.__findThroughParent(root.left, x, minDist)  
        if (l != -1): 
            self.__findLeafDown(root.right, l + 2, minDist)  
            return l + 1
  
        r = self.__findThroughParent(root.right, x, minDist)  
  
        if (r != -1): 
            self.__findLeafDown(root.left, r + 2, minDist)  
            return r + 1
  
        return -1

    def findNearestLeaf(self, root, x): 
        minDist = [999999999999]
        val='0'
        self.__findLeafDown(x, 0, minDist,val)  
        self.__findThroughParent(root, x, minDist,val)  
        return minDist[0],val 

    def createBT(self):
        root = NewNode('A')  
        root.left = NewNode('B')  
        root.right = NewNode('C')  

        root.left.left=NewNode('D')
        root.left.right=NewNode('E')
        root.right.left = NewNode('F')  
        root.right.right = NewNode('G')  
  
        root.left.left.left = NewNode('H')
        root.right.left.left = NewNode('I')  
        root.right.left.right = NewNode('J')   
  
        root.right.left.left.left = NewNode('K')   
        root.right.left.right.right = NewNode('L')  
        
        root.right.left.left.left.left=NewNode('M')
        root.right.left.left.left.right=NewNode('N')
        root.right.left.right.right.left=NewNode('O') 
        root.right.left.right.right.right=NewNode('P') 
        x = root.right.left
        return [root,x]

if __name__ == '__main__':   
  
    solClass = NearestLeaf()
    root_x=solClass.createBT()
    print("The closest leaf to the node with value", 
           root_x[1].key, "is at a distance of",  
           solClass.findNearestLeaf(root_x[0], root_x[1]))