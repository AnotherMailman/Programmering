letters=["q","y","u","p","a","h","c"]

ord=input().lower()
for x in ord:
    for y in letters:
        if y == x:
            letters.remove(y)


print(letters)