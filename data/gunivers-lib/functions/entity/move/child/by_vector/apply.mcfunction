# NAME: Move Entity By Vector
# PATH: Gunivers-Lib:entity/location/child/move_by_vector/apply

# CHILD OF: gunivers-lib:entity/location/move_by_vector

# CODE:

function gunivers-lib:entity/location/accurate/get

execute store result entity @s Pos[0] double 0.001 run scoreboard players operation @s LocX += @s VectorX
execute store result entity @s Pos[1] double 0.001 run scoreboard players operation @s LocY += @s VectorY
execute store result entity @s Pos[2] double 0.001 run scoreboard players operation @s LocZ += @s VectorZ

