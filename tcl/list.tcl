# split string into list & ignore all whitespace
set stringA "This    is a       string"
set listA [regexp -all -inline {\S+} $stringA]
puts $stringA
puts $listA
