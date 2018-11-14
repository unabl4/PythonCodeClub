def elements_count(*lists):
    f = {}

    for l in lists:
        for n in l:
            f[n] = f.get(n,-1)+1

    # nums
    n = { k:v for (k,v) in f.items() if v > 0 }
    return { k:n[k] for k in sorted(n.keys()) } # sort by key
