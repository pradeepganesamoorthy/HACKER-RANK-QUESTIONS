def merge_intervals(intervals):
    intervals.sort()
    res=[intervals[0]]
    for i in intervals[1:]:
        if res[-1][1] >= i[0]:
            res[-1][1] = max(res[-1][1],i[1])
        else:
            res.append(i)
    return res

print(merge_intervals([[1,3],[2,6],[8,10]]))
