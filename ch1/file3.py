s = input("Εισάγετε έναν θετικό ακέραιο: ")

if not s.strip().isdigit() or int(s) <= 0:
    print("Μη έγκυρη είσοδος.")
else:
    n = int(s)
    with open("out.txt", "w") as f:
        while True:
            f.write(f"{n}\n")
            if n == 1:
                break
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
    print("Η ακολουθία Collatz γράφτηκε στο out.txt")
