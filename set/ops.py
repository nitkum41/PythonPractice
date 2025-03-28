numbers1 = frozenset([1, 2, 3, 4, 5])
numbers2 = frozenset([2, 3, 4, 5])

# Combining both of them using "|" operator
# You can also use union() method
combined = numbers1 | numbers2
print("Combined set:", combined)

# Selecting common elements using "&" operator
# You can also use intersection() method
intersect = numbers1 & numbers2
print("Intersected set:", intersect)

# Selecting elements which are not common using "-" operator
# You can also use difference() method
difference = numbers1 - numbers2
print("Difference set:", difference)

# Membership testing

# It returns True if sets (frozenset) have no common items otherwise False
Disjoint = numbers1.isdisjoint(numbers2)
print("Disjoint:", Disjoint)

# It returns True if all the items of a set (frozenset) are common in another set (frozenset)
Subset = numbers1.issubset(numbers2)
print("Subset:", Subset)

# It returns True if a set (frozenset) has all items present in another set (frozenset)
Superset = numbers1.issuperset(numbers2)
print("Superset:", Superset)