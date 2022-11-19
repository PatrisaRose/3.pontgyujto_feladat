november = [0, 12, 13, 9, 2, 7]


def a():
    i = 1
    while i < len(november):
        if (november[i] - november[i - 1]) < 3:
            print(f"{i + 2} napon csökkent az előző naphoz képest a hőmérséklet több, mint 3 fokot.")

        i += 1


def a1():
    i = 0
    while i < len(november):
        if (november[i] - november[i + 1] > 3):
            print(f"{i + 2} napon csökkent az előző naphoz képest a hőmérséklet több, mint 3 fokot.")

        i += 1


def a2():
    i = 0
    while (i < len(november) - 1) and (november[i] - november[i + 1] <= 3):
        i += 1
    if (i < len(november) - 1):
        print(f"{i + 2} napon csökkent az előző naphoz képest a hőmérséklet több, mint 3 fokot.")
    else:
        print("Nem volt ilyen nap")


def a3():
    i = 0
    while i < len(november):
        if (november[i - 1] - 3 > november[i]):
            print(f"{i + 2} napon csökkent az előző naphoz képest a hőmérséklet több, mint 3 fokot.")

        i += 1