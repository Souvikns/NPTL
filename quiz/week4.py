def mystery(l, v):
    # to see how to function is workiing
    # print(l)
    # print(v)
    if len(l) == 0:
        return v
    else:
        return mystery(l[:-1], l[-1] + v)


if __name__ == '__main__':
    print(mystery([22, 14, 19, 65, 82, 55], 1))
    triples = [(x, y, z) for x in range(2, 4) for y in range(2, 5) for z in range(5, 7) if 2 * x * y > 3 * z]
    print(triples)
    runs = {
        "Test": {
            "Rohul": [90, 14, 35],
            "Kohli": [3, 103, 73, 42],
            "Pujara": [53, 15, 133, 8]
        },
        "ODI": {
            "Sharma": [37, 99],
            "Kohli": [63, 47]
        }
    }
    runs["ODI"]["Rahul"] = [74]
    print(runs)
    actor = {}
    actor[("Star Wars", "Rey")] = "Ridley"
    print(actor)
