# sort dict based on item
d = {'KEY1':{'name':'google','date':20100701,'downloads':0},
 'KEY2':{'name':'chrome','date':20071010,'downloads':100},
 'KEY3':{'name':'python','date':20100710,'downloads':90}}


d = sorted(d.items(), key = lambda tup: tup[1]["downloads"])
print(json.dumps(d, indent = 4))
