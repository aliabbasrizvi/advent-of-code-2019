"""
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets!
To accurately calculate his position in space, safely align his warp drive,
and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel
needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

def get_fuel(val):
  return val / 3 - 2

input_vals = [
  72713,
  93795,
  64596,
  99366,
  124304,
  122702,
  105674,
  94104,
  144795,
  109412,
  138753,
  71738,
  62172,
  149671,
  88232,
  145707,
  82617,
  123357,
  63980,
  149016,
  130921,
  125863,
  119405,
  77839,
  140354,
  135213,
  130550,
  131981,
  149301,
  68884,
  52555,
  121036,
  75237,
  64339,
  60612,
  132912,
  63164,
  145198,
  109252,
  130024,
  100738,
  74890,
  89784,
  134474,
  68815,
  117283,
  144774,
  138017,
  149989,
  111506,
  119737,
  65330,
  52388,
  69698,
  124990,
  84232,
  58016,
  142321,
  119731,
  86914,
  68524,
  87708,
  60776,
  119259,
  73429,
  79486,
  120369,
  57007,
  91514,
  87226,
  131770,
  78170,
  52871,
  149060,
  73804,
  60034,
  72519,
  98065,
  132526,
  99660,
  74854,
  111912,
  51232,
  71499,
  127629,
  83807,
  91061,
  60988,
  133493,
  95170,
  110661,
  54486,
  63241,
  141111,
  142244,
  93120,
  137257,
  79822,
  95849,
  69878
]

total_sum = 0
for val in input_vals:
  total_sum += get_fuel(val)

print(total_sum)

