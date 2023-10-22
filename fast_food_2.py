from collections import deque

capacity_food = int(input())
numbers_food = input().split()
stack = deque()
max_number = max([int(num) for num in numbers_food])
for nums in numbers_food:
    stack.append(int(nums))

    while stack:
        current_order = stack[0]
        if current_order < capacity_food:
            capacity_food -= current_order
            stack.popleft()
        else:
            break

if not stack:
    print(max_number)
    print("Orders complete")
else:
    print(max_number)
    print(f"Orders left: {', '.join(map(str, stack))}")
