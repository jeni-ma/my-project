def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        # d: decimal, o: octal, X: hex (capitalized), b: binary
        # Each is right-aligned to 'width'
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=width))
