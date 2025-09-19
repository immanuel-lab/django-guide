# chain(): combines multiple iterables into one.
# combinations(): generates all possible combinations of a certain length.
# permutations(): generates all possible permutations.
# product(): generates cartesian product.
# cycle(): creates an infinite iterator.
# accumulate(): calculates cumulative sum.
# groupby(): groups consecutive items.



# my_list = [1, 2, 3]
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))


import itertools

# print(dir(itertools))

# chain
# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# chained = list2+list1
# chained=list(itertools.chain(list1,list2))
# print(chained)  # [1, 2, 3, 'a', 'b']




# combinations
# items = [1, 2, 3,4,5,6,7]
# combinations = list(itertools.combinations(items, 4))
# print(combinations)  
# # [(1, 2), (1, 3), (2, 3)]

# permutations
# items = [1, 2,3]
# permutations = list(itertools.permutations(items))
# print(permutations) 
#  # [(1, 2), (2, 1)]



# list1 = [1, 2]
# list2 = ['a', 'b', 'c']

# zip
# zipped = list(zip(list1, list2))
# print(zipped)  
# [(1, 'a'), (2, 'b')]

# itertools.product
# product = list(itertools.product(list1, list2))
# print(product) 
 # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]



# cycle
# import itertools
# arr=[1,2,3,4,5,6]
# iterators=itertools.cycle(arr)
# print(list(iterators))

# for _ in range(50):
#     print(next(iterators))




# import itertools

# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# grouped_numbers = itertools.groupby(numbers)

# for key, group in grouped_numbers:
#     print(key,list(group))



# arr=[1,2,3,4,5,6,7]
# print(sum(arr))

# accumulate

# import operator
# arr=[1,2,3,4,5,6,7]
# sum=list(itertools.accumulate(arr))
# product=list(itertools.accumulate(arr,operator.mul))
# print(product)


# arr=[1,2,3,4,5,6,7]
# product=list(itertools.accumulate(arr,lambda x,y:x*y))
# print(product)

