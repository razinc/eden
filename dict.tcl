# initialize empty dict
set fruits [dict create]

# initialize dict
set fruits [dict create  fruit_1 [dict create name apple total 2] \
    fruit_2 [dict create name grape total 10] \
    fruit_3 [dict create name banana total 4] \
    ]

# prints dict's info
foreach key [dict keys $fruits] {
    # print key
    puts $key
    
    # print value
    set value [dict get $fruits $key]
    puts $value
    
    # print nested value
    set fruit_name [dict get $value name]
    puts $fruit_name
}

# append dict
dict lappend fruits fruits_4 name lemon total 6
puts $fruits

# sort (increasing)
set fruits [lsort -integer -stride 2 -index {end end} $fruits]
puts $fruits
set fruits [lsort -integer -stride 2 -index {end 3} $fruits]

# sort (decreasing)
set fruits [lsort -integer -decreasing -stride 2 -index {end end} $fruits]
puts $fruits
set fruits [lsort -integer -decreasing -stride 2 -index {end 3} $fruits]
puts $fruits
