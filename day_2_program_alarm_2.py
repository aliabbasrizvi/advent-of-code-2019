"""
--- Part Two ---
"Good, the new computer seems to be working correctly! Keep it nearby during this mission - you'll probably use it again.
Real Intcode computers support many more features than your new one, but we'll let you know what they are as you need them."

"However, your current priority should be to complete your gravity assist around the Moon. For this mission to succeed,
we should settle on some terminology for the parts you've already built."

Intcode programs are given as a list of integers; these values are used as the initial state for the computer's memory.
When you run an Intcode program, make sure to start by initializing memory to the program's values.
A position in memory is called an address (for example, the first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode, if any,
are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4
are the parameters. The instruction 99 contains only an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction finishes,
the instruction pointer increases by the number of values in the instruction; until you add more instructions to the
computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions.
(The halt instruction would increase the instruction pointer by 1, but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what
pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before.
In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb.
Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of
inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other words,
don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
(For example, if noun=12 and verb=2, the answer would be 1202.)
"""

def generate_value(noun, verb):
  input_vals = [1,noun,verb,3,
                1,1,2,3,
                1,3,4,3,
                1,5,0,3,
                2,10,1,19,
                1,19,5,23,
                1,23,9,27,
                2,27,6,31,
                1,31,6,35,
                2,35,9,39,
                1,6,39,43,
                2,10,43,47,
                1,47,9,51,
                1,51,6,55,
                1,55,6,59,
                2,59,10,63,
                1,6,63,67,
                2,6,67,71,
                1,71,5,75,
                2,13,75,79,
                1,10,79,83,
                1,5,83,87,
                2,87,10,91,
                1,5,91,95,
                2,95,6,99,
                1,99,6,103,
                2,103,6,107,
                2,107,9,111,
                1,111,5,115,
                1,115,6,119,
                2,6,119,123,
                1,5,123,127,
                1,127,13,131,
                1,2,131,135,
                1,135,10,0,
                99,
                2,14,0,0]


  for idx in range(0, len(input_vals), 4):
    if input_vals[idx] == 1:
      input_vals[input_vals[idx + 3]] = input_vals[input_vals[idx + 1]] + input_vals[input_vals[idx + 2]]
    elif input_vals[idx] == 2:
      input_vals[input_vals[idx + 3]] = input_vals[input_vals[idx + 1]] * input_vals[input_vals[idx + 2]]
    elif input_vals[idx] == 99:
      break

  return input_vals[0]

for noun in range(99):
  for verb in range(99):
    val = generate_value(noun, verb)
    if val == 19690720:
      print(100 * noun + verb)
      break