def is_symmetric_brackets(s: str) -> bool:

    stack = []

    opening = "([{"
    closing = ")]}"
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for ch in s:
        if ch in opening:
            stack.append(ch)          # кладемо відкриту дужку в стек
        elif ch in closing:
            if not stack:
                return False          # закриваюча без пари
            top = stack.pop()
            if top != pairs[ch]:
                return False          # тип дужок не збігається

    return len(stack) == 0            # стек має бути порожній

def main():
    
    while True:
        expr = input("Введіть вираз: ")

        if is_symmetric_brackets(expr):
            print("Симетрично")
        else:
            print("Несиметрично")


if __name__ == "__main__":
    main()
