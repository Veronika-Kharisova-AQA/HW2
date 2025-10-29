print("Привет, README!")

text = (
    "Lorem Ipsum — это текст-«рыба», часто используемый в печати и веб-дизайне."
    " Lorem Ipsum"
)

print(text)


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


numbers = [1, 2, 3, 4, 5]

print(greet("мир"))  # вызов функции greet
print(add(2, 2))  # вызов функции add и вывод результата
