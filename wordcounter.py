def count_words(s,n):

    ss=s.split()

    counter=[]

    for i in ss:

        counter.append(ss.count(i))

    result = set(tuple(zip(ss,counter)))

    import operator

    sorted_alph = sorted(result, key = operator.itemgetter(0))

    finalsort = sorted(sorted_alph, key=operator.itemgetter(1), reverse=True)

    return finalsort[:n]


