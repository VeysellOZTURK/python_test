inputs = []
while True:
    inputStr = input()
    if inputStr == "":
        break
    inputs.append(int(inputStr))

max = inputs[0]
for i in range(len(inputs)):
    if inputs[i] > max:
        max = inputs[i]

print(max)
