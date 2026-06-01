def get_distinct_sorted(numbers: list) -> list:
    return sorted(set(numbers))


if __name__ == "__main__":
    numbers = [2, 20, 3, 7, 10, 4, 4, 7, 9, 12, 15, 14, 11, 10, 13, 10, 20, 16, 12, 16]
    result = get_distinct_sorted(numbers)
    print(result)# Q7: Remove duplicates and sort
