#Ananta Alief R 
#MI 2020 B 
#20051397074
  

class Stack(list):
    push = list.append

def modify_stack(symbolString):
    stack=Stack()
    result = []
    for character in symbolString:
        if character != '*':
            stack.push(character)
        else:
            result.append(stack.pop())
    return ''.join(result)
print(modify_stack('EAS*Y*QUE***ST***IO*N***'))
