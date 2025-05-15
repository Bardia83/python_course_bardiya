import re 

# 1-# .  
# a.c  ==> abc =!ac
# 2- ^
# ^hello
# 3-$ 
# $world
# 4- *
# ab*c  ==> abjkghjkgjhgbc ===>abc
# 5-+
# ab+c   => abbhgjhc !=abc 
# 6- ?
# ab?c 
# 7- {n}
# a{3}==> aaa
# 8- {n,}
# a{2,} [2:]
# aa,aaa,aaaaa
# 9-{n,m}
# a{2,4} ==>aa,aaa,aaaa !=aaaaa
# 10-[abc] ==> a,b,c [a-c]
# 11-[^abc] bardiya davo
# 12-[^0-9] 
# 13-\d [0-9]
# 14_\D
# 15-\w  [a-zA-Z0-9_]
# 16_ \W  [^a-zA-Z0-9_]
# 17_ \s \s+
# 18_\S