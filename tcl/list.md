# Basic Operation

## String Splitting
```tcl
set my_string "this   is a       string"
set my_list [regexp -all -inline {\S+} $my_string]
puts $my_list
# this is a string
```
