def es_primo(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
for a in range(1, 101):
    if es_primo(a):
        print(a)