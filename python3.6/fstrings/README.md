# fstrings

fstrings (formatted String literals) in python were introduced in python in version 3.6 in order to make string formatting during printing more concise and less prone to error

Before this feature was introduced you had to use the following code to print variables when it was concatenated with strings

```
name = "Maximus"
age = 120
print("My name is {} and age is {}".format(name, age))
```

After this feature was introduced, you could simply do this

```
name = "Maximus"
age = 120
print(f"My name is {name} and my age is {age}")
```

this made things more concise and less prone to error - essentially because it's harder to mess up the order of the variables

you could also add python functions in the print statements with fstrings

```
name = "Maximus"
age = 120
print(f"My name is {name} and my age would be {age+30} in 30 years")
```

Since python 3.8 you could also use a helpful debugging feature where you could simply append the variable with = to see both the variable name and it's contents

```
name = "Maximus"
age = 120
print(f"{name=},{age=}")
```