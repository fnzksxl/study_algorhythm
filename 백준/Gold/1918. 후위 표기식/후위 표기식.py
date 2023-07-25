lst=list(input())
stack=[]
result=''

# A*(B+C+D)
# ABC+D+*

# A*(B*C/D/E)
# ABC*D/E/*

for cur in lst:
    if cur.isalpha():
        result+=cur
    else:
        if cur == '(':
            stack.append(cur)
        elif cur == '*' or cur == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result+=stack.pop()
            stack.append(cur)
        elif cur == '+' or cur =='-':
            while stack and stack[-1] != '(':
                result+=stack.pop()
            stack.append(cur)
        elif cur==')':
            while stack and stack[-1] != '(':
                result+=stack.pop()
            stack.pop()

while stack:
    result+=stack.pop()
    
print(result)
