#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_expression(tokens):
    # Step 1: Convert all numbers to float
    for i in range(0, len(tokens), 2):
        tokens[i] = float(tokens[i])

    # Step 2: Handle *, /
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == "*":
            tokens[i-1] = tokens[i-1] * tokens[i+1]
            del tokens[i:i+2]
        elif tokens[i] == "/":
            if tokens[i+1] == 0:
                print("Error: Cannot divide by zero.")
                return None
            tokens[i-1] = tokens[i-1] / tokens[i+1]
            del tokens[i:i+2]
        else:
            i += 2

    # Step 3: Handle +, -
    i = 1
    while i < len(tokens) - 1:
        if tokens[i] == "+":
            tokens[i-1] = tokens[i-1] + tokens[i+1]
            del tokens[i:i+2]
        elif tokens[i] == "-":
            tokens[i-1] = tokens[i-1] - tokens[i+1]
            del tokens[i:i+2]
        else:
            i += 2

    return tokens[0]


while True:
    user_input = input("Enter calculation (e.g. 2 + 3 * 4) or type 'exit' to quit: ").strip()

    if user_input.lower() == "exit":
        print("Exiting program.")
        break

    tokens = user_input.split()

    # Validate input
    if len(tokens) < 3 or len(tokens) % 2 == 0:
        print("Invalid expression format. Use format like: 2 + 3 * 4")
        continue

    result = calculate_expression(tokens)

    if result is not None:
        print("Result:", result)

