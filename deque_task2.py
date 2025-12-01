from collections import deque

def is_palindrome(s: str) -> bool:

    # готуємо рядок: прибираємо пробіли і робимо нижній регістр
    cleaned = ""
    for ch in s:
        if ch != " ":
            cleaned += ch.lower()

    # створюємо deque і додаємо символи
    d = deque()
    for ch in cleaned:
        d.append(ch)

    # порівнюємо символи з обох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True

def main():
    
    while True:
        s = input("Введіть рядок для перевірки: ")
    
        if is_palindrome(s):
            print("Це паліндром.")

        else:
            print("Це не паліндром.")


if __name__ == "__main__":
    main()
