def remove_duplicates(data):
    seen_first = set()
    seen_second = set()
    result = []

    for sublist in data:
        first_element = sublist[0]
        second_element = sublist[1]

        if first_element[0] not in seen_first and second_element[0] not in seen_first:
            if first_element[1] not in seen_second and second_element[1] not in seen_second:
                result.append(sublist)
                seen_first.add(first_element[0])
                seen_second.add(first_element[1])

    return result

data = [[[1, 3], [2, 3]], [[1, 3], [1, 2]], [[1, 3], [1, 4]], [[0, 7], [0, 6]]]
filtered_data = remove_duplicates(data)
print(filtered_data)
