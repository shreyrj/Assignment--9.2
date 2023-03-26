def is_balanced(delimiters):
 stack = []
 for char in delimiters:
 if char in "([{":
 stack.append(char)
 elif char in ")]}":
 if not stack:
 return False
 if (char == ")" and stack[-1] == "(") or \
 (char == "]" and stack[-1] == "[") or \
 (char == "}" and stack[-1] == "{"):
 stack.pop()
 else:
 return False
 return not stack
print(is_balanced("()[]{}")) 
print(is_balanced("([{}])")) 
print(is_balanced("([]{})")) 
print(is_balanced("([)]")) 
print(is_balanced("([{}]")) 
print(is_balanced("[]{}[")) 