def isValidBracketSequence(inputString):
    stack = []
    bracketMapping = {')': '(', '}': '{', ']': '['}
    
    if not inputString:
      return False

    for char in inputString:
        if char in bracketMapping.values():
            stack.append(char)
        else:
            if stack and stack[-1] == bracketMapping.get(char):
                stack.pop()
            else:
                return False
    return not stack
  
  
inputString1 = "([)]" 
output1 = isValidBracketSequence(inputString1)

inputString2 = "()[]{}"
output2 = isValidBracketSequence(inputString2)

inputString3 = '{[()]}'
output3 = isValidBracketSequence(inputString3)


inputs = [inputString1, inputString2, inputString3]
outputs = [output1, output2, output3]

for i in range(0, 3):
  print(f'Input: "{inputs[i]}"')
  print(f"Output: {outputs[i]}")
  print()
  
  
