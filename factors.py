def factors(x):
    result = []
    # עוברים על כל המספרים מ-1 ועד x כולל
    for i in range(1, x + 1):
        if x % i == 0:
            result.append(i)
    return result
