# Basic Operation

## Empty Dict Initialization
```tcl
set fruits [dict create]
```

## Dict Initialization
```tcl
set fruits [dict create  fruit_1 [dict create name apple total 2] \
                         fruit_2 [dict create name grape total 10] \
                         fruit_3 [dict create name banana total 4] \
                         ]
puts $fruits
# fruit_1 {name apple total 2} fruit_2 {name grape total 10} fruit_3 {name banana total 4}
```

## Print Content
```tcl
set fruits [dict create  fruit_1 [dict create name apple total 2] \
                         fruit_2 [dict create name grape total 10] \
                         fruit_3 [dict create name banana total 4] \
                         ]
                         
foreach key [dict keys $fruits] {
    puts $key
    # fruit_1
    # fruit_2
    # fruit_3

    set value [dict get $fruits $key]
    puts $value
    # name apple total 2
    # name grape total 10
    # name banana total 4
    
    foreach key [dict keys $value] {
        puts $key
        # name
        # total
        # name
        # total
        # name
        # total
    }
    
    set fruit_name [dict get $value name]
    puts $fruit_name
    # apple
    # grape
    # banana
}
```

## Dict Verification
```tcl
# TODO: check if key in dict
# TODO: check if key in nested dict
# TODO: check if value in dict
# TODO: check if value in nested dict
```

## Dict Modification
```tcl
set fruits [dict create  fruit_1 [dict create name apple total 2] \
                         fruit_2 [dict create name grape total 10] \
                         fruit_3 [dict create name banana total 4] \
                         ]

dict lappend fruits fruits_4 name lemon total 6
puts $fruits
# fruit_1 {name apple total 2} fruit_2 {name grape total 10} fruit_3 {name banana total 4} fruits_4 {name lemon total 6}

# sort (increasing)
set fruits [lsort -integer -stride 2 -index {end end} $fruits]
puts $fruits
set fruits [lsort -integer -stride 2 -index {end 3} $fruits]
puts $fruits

# sort (decreasing)
set fruits [lsort -integer -decreasing -stride 2 -index {end end} $fruits]
puts $fruits
set fruits [lsort -integer -decreasing -stride 2 -index {end 3} $fruits]
puts $fruits

# TODO: delete dict
```
