weights = [ values[0] - values[1]  for values in petrolpumps ]

    start = 0
    current = 0
    total = 0
    final_sum = sum(weights)
    while True:
        if total < 0 and start == current:
            current = (len(weights) + current + 1)%len(weights)
            start = current
            total = 0

        if total >= 0:
            total += weights [ current ]
            current = (len(weights) + current + 1)%len(weights)
        else:
            total -= weights [ start ]
            start = (len(weights) + start + 1)%len(weights)

        if total == final_sum: 
            break

    
    # print(start,current,total)
    return start
