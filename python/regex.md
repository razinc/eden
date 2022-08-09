# Resources
* [RegExr](https://regexr.com/)
* [regex101](https://regex101.com/)

# Pattern Cheatsheet
* `b.*d` will match everything from `b` to `d`
```python
S = "abcdef"
print(re.findall("b.*d", S))
# ["bcd"]
```

* To check if pattern is in the string
```python
S = "abcdef"
print(bool(re.search("b.*d", S)))
# True
```

* `1.*?4_` will match first occurence from `1` to `4_`
```python
S = "0_1_2_3_4_5"
print(re.findall("1.*?4_", S))
# ["1_2_3_4_"]
```

* To get last occurence, reverse the string first before using the same regex as above.
