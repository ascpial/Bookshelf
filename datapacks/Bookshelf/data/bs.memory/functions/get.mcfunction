# NAME: Get Variable
# PATH: bs.memory:get

# AUTHOR: theogiraudet

# VERSION: 1.0
# MINECRAFT: 1.14

# INPUT:
# - @s ArmorItems[0].tag.Buffer1 ~ Variable Name (NBT)

# OUTPUT:
# - @s ArmorItems[0].tag.Output ~ Variable Value(NBT)

# NOTE:
# Returns the value associated with the variable name specified in input. If no variable has this name, the output NBT tag is removed.
# If the executing entity is not a valid Memory, do nothing.

#INIT:
function bs_child:default/core/memory/init

# CODE:
execute if entity @s[tag=Memory,tag=bs] if data entity @s ArmorItems[0].tag.Buffer1 run tag @s add Valid

data remove entity @s ArmorItems[0].tag.Output
data modify entity @s[tag=Valid] ArmorItems[0].tag.Buffer2 set from entity @s ArmorItems[0].tag.Memory
data modify entity @s ArmorItems[0].tag.Buffer3 set from entity @s ArmorItems[0].tag.Buffer1

execute if entity @s[tag=Valid] run function bs_child:default/core/memory/get_rec

tag @s remove Valid