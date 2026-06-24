start = int(input("Enter start: "))
end = int(input("Enter end: "))

while start <= end:

    if start > 1:
        divisor = 2
        is_prime = True

        while divisor < start:
            if start % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            print(start)

    start += 1