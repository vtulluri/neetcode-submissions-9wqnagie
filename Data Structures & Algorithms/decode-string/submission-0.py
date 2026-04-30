class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in s:
            if i !=']':
               stack.append(i)
            else:
                substr=""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                nums=""

                while stack and stack[-1].isdigit():
                    nums=stack.pop()+nums
                
                k=int(nums)

                stack.append(substr*k)

        return ''.join(stack)


                    