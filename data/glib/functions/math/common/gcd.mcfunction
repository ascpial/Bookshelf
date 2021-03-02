#__________________________________________________
# INFO     Copyright © 2020 Gunivers.

# Authors: Leirof
# Contributors:
# MC Version: 1.13
# Last check:

# Original path: glib:math/gcd
# Documentation: https://project.gunivers.net/projects/gunivers-lib/wiki/math
# Parallelizable: <true/false/global>
# Note: Calculates the Greatest Common Divisor of 2 given numbers.

#__________________________________________________
# PARAMETERS

#__________________________________________________
# INIT







#__________________________________________________
# CONFIG

#__________________________________________________
# CODE

scoreboard players operation @s glib.var2 = @s glib.var0
scoreboard players operation @s glib.var2 -= @s glib.var1

scoreboard players operation @s[scores={glib.var2=1..}] glib.res0 = @s glib.var1
scoreboard players operation @s[scores={glib.var2=1..}] glib.var2 = @s glib.var0

scoreboard players operation @s[scores={glib.var2=..-1}] glib.res0 = @s glib.var0
scoreboard players operation @s[scores={glib.var2=..-1}] glib.var2 = @s glib.var1

tag @s[scores={glib.var2=0}] add PGCDfound

execute at @s[tag=!PGCDfound] run function glib:math/child/gcd-loop

tag @s remove PGCDfound
