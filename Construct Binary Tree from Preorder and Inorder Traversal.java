public TreeNode buildTreeRecursive(int[] preorder, int[] inorder) {
        if(preorder == null || inorder == null || inorder.length == 0 || preorder.length == 0) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[0]);
        if (preorder.length == 1) {
            return root;
        }
        int index = -1;
        for (int i = 0; i < inorder.length; i++) {
            if(preorder[0] == inorder[i]) {
                index = i;
                break;
            }
        }
        int[] new_left_pre = Arrays.copyOfRange(preorder, 1, index+1);
        int[] new_left_ino = Arrays.copyOfRange(inorder, 0, index);
        int[] new_rigth_pre = Arrays.copyOfRange(preorder, index + 1, preorder.length);
        int[] new_rigth_ino = Arrays.copyOfRange(inorder, index + 1, inorder.length);
        root.left = buildTreeRecursive(new_left_pre, new_left_ino);
        root.right = buildTreeRecursive(new_rigth_pre, new_rigth_ino);
        return root;
    }
    
public TreeNode buildTreeIteration(int[] preorder, int[] inorder) {
    if(preorder == null || inorder == null || inorder.length == 0 || preorder.length == 0) {
        return null;
    }
    TreeNode root = new TreeNode(preorder[0]);
    if (preorder.length == 1) {
        return root;
    }
    int pr = 1, in = 0;
    Stack<TreeNode> s;
    s = new Stack<TreeNode>();
    s.add(root);
    while (pr < preorder.length) {
        TreeNode cur = null;
        TreeNode tmp = new TreeNode(preorder[pr]);
        while (!s.empty() && s.peek().val == inorder[in]) {
            cur = s.pop();
            ++in;
        }
        if(cur != null) {
            cur.right = tmp;
        } else {
            s.peek().left = tmp;
        }
        s.add(tmp);
        ++pr;
    }
    return root;
}
