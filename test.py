# Write a function that takes a year and returns its corresponding century.
# Examples
# century_from_year(2005) ➞ 21
# century_from_year(1950) ➞ 20
# century_from_year(1900) ➞ 19

# def century_from_year(year):
#     return int((year - 1)/100) + 1


# print(century_from_year(2005))
# print(century_from_year(1950))
# print(century_from_year(1900))



# Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
# Examples
# list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
# list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
# Notes
# Notice that num is also included in the returned list.

# def list_of_multiples(num, length):
#     return [num * i for i in range(1, length + 1)]

# print(list_of_multiples(7, 5))
# print(list_of_multiples(12, 10))
# print(list_of_multiples(17, 6))


# Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
# Examples
# majority_vote(["A", "A", "B"]) ➞ "A"
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
# Notes
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.

def majority_vote(votes):
    target = len(votes)/2

    for i in votes:
        if votes.count(i) > target:
            return i
    else:
        return None

print(majority_vote(["A", "A", "B"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))