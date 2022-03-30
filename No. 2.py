#Ananta Alief R 
#MI 2020 B 
#20051397074


class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def IsEmpty(self):
        return self.items == []

    def peek (self):
        if not self.IsEmpty():
            return self.items[-1]

    def get_stack (self):
        return self.items

def konvert(stack, input_int):
    for i in range(len(input_int)):
        stack.push(input_int[i])

    rev_int = ""
    while not stack.IsEmpty():
        rev_int += stack.pop()

    return rev_int

stack = stack()
input_int = 100
desimal = input_int
biner = bin(desimal).replace("0b","")
oktal = oct(desimal).replace("0o","")
hexa = hex(desimal).replace('0x',"")

print (f"Bilanga Desimal yang dimasukkan adalah : {desimal}")
print(f"Konversi ke Biner : {biner}")
print(f"Konversi ke Oktal : {oktal}")
print(f"Konversi ke Hexa  : {hexa}")
