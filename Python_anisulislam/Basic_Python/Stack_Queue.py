'''books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn C#")
print(books)

# books.pop()
# print(books)
print("Now the top book is : ", books[-1])

# books.pop()
# print(books)
print("Now the top book is : ", books[-1])

if not books:
    print("No books found")'''

# Queues
from collections import deque

bank = deque(["anis", "karim", "Bijoy"])
bank.popleft()
print(bank)

if not books:
    print("No person left")
