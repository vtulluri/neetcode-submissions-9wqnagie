class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        parts=path.split("/")

        for c in parts:
            print(c)
            if c == "" or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "/"+"/".join(stack)

        # stack = []
        # parts = path.split("/")
        
        # for part in parts:
        #     if part == "" or part == ".":
        #         continue
        #     elif part == "..":
        #         if stack:
        #             stack.pop()
        #     else:
        #         stack.append(part)
        
        # return "/" + "/".join(stack)

