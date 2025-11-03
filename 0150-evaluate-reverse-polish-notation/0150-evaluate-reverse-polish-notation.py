class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))

            elif i == "+":
                val1=stack.pop()
                val2=stack.pop()
                stack.append(int(val1)+int(val2))
            elif i == "-":
                val1=stack.pop()
                val2=stack.pop()
                stack.append(int(val2)-int(val1))
            elif i == "/":
                val1=stack.pop()
                val2=stack.pop()
                stack.append(int(val2)/int(val1))
            elif i == "*":
                val1=stack.pop()
                val2=stack.pop()
                stack.append(int(val2)*int(val1))
            
        return int(stack[-1])
                

        
        