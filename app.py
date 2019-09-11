def max2(x, y):
    if(x > y):
        return x
    else:
        return y

numbers = []

with open('bugtrk.in', 'r') as input:
    numbers = input.read().split()

items_number = int(numbers[0])
item_width =  int(numbers[1])
item_height = int(numbers[2])
items_number_width = 1
items_number_height = 1

while items_number_width*items_number_height < items_number:
    if((items_number_width + 1) * item_width < (items_number_height + 1) * item_height):
        items_number_width += 1
    else:
        items_number_height += 1

with open('bugtrk.out', 'w+') as output:
    output.write(str(max2(items_number_width*item_width, items_number_height*item_height)))
