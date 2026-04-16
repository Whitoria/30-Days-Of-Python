# 1. Create an Empty List
lst = list()

# 2. Declare a list with more than 5 items
lst = [1,2,3,4,5]
print(f"2. List output: {lst}")

# 3. Find the length of your list
length = len(lst)
print(f"3. Count: {length}")

# 4. Get the first item, the middle item, and the last item of the list
first, second, middle, *rest, last = lst #Tried unpacking, most likely not as efficient
print(f"First Value of the List: {first}")
print(f"Middle Value of the List: {middle}")
print(f"Last Value of the List: {last}")

# 5. Declare a list called mixed_data_types, put your (name, age, height, marital status, address)
mixed_data_types = ["McLoving", 21, "5'10\"", "Single", "832 Momona St."]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle, and Amazon
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
comp_len = len(it_companies)
print(f"Number of Companies in the list: {comp_len}")

# 9. Print the First, Middle, and Last company
print(it_companies[0])
print(it_companies[(comp_len//2)])
print(it_companies[-1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Anthropic"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Meta")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(3, "Tesla")
print(it_companies)

# 13. Change one of the it_companies
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '

joined_string = '#; '.join(it_companies)
print(joined_string)


# 15. Check if a certain company exists in the it_companies list.
t_f = "Apple" in it_companies
print(t_f)


# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)


# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[3:])


# 19. Slice out the last 3 companies from the list
print(it_companies[:6])


# 20. Slice out the middle IT company or companies from the list
print(it_companies.pop(comp_len//2))



# 21. Remove the first IT company from the list
it_companies.pop(0)


# 22. Remove the middle IT company or companies from the list
it_companies.pop(comp_len//2)



# 23. Remove the last IT company from the list
it_companies.pop(-1)



# 24. Remove all IT companies from the list
it_companies.clear()


# 25. Destroy the IT companies list
del it_companies


# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

lst2 = front_end.copy()