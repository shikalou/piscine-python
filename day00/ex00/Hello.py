ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list
ft_list[1] = "World!"

# tuple
x = list(ft_tuple)
x[1] = "France!"
ft_tuple = tuple(x)

# set
ft_set.discard("tutu!")
ft_set.add("Paris!")

# dict
ft_dict.update(Hello="42Paris!")
# ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
