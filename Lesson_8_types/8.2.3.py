def mult_tuple(tuple1, tuple2):
    list_tuples = []
    for i in tuple1:
        for j in tuple2:
            list_tuples.append((i, j))
    for i in tuple2:
        for j in tuple1:
            list_tuples.append((i, j))
    return tuple(list_tuples)


# Course solution:


# def mult_tuple(tuple1, tuple2):
#     """Builds all possible couples of the given 2 tuples
#     :params: tuple1, tuple2: input tuples
#     :return: tuple contains all the couples. Order not mandatory
#     :rtype: tuple
#     """
#     calc = tuple([(t1, t2) for t1 in tuple1 for t2 in tuple2])
#     return calc + tuple([p[::-1] for p in calc])
