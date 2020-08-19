### Implementing and simulating multiplexers in PyRTL ###

import pyrtl

# Now, it is time to build and simulate (for 16 cycles) a 3-bit 5:1 MUX.
# You can develop your design using either Boolean gates as above or PyRTL's
# conditional assignment.

# Declare data inputs
# < add your code here >
a, b, c, d, e = pyrtl.Input(3, 'a'), pyrtl.Input(3, 'b'), pyrtl.Input(3, 'c'), pyrtl.Input(3, 'd'), pyrtl.Input(3, 'e')

# Declare control inputs
s = pyrtl.Input(bitwidth=3, name='s')

# Declare outputs 
result = pyrtl.Output(3, 'result')
# < add your code here >

# Describe your 5:1 MUX implementation
# < add your code here >
with pyrtl.conditional_assignment:
 with s == 000:
 result |= a
 with s == 001:
 result |= b
 with s == 010:
 result |= c
 with s == 011:
 result |= d
 with s == 100:
 result |= e
 with s == 101:
 result |= e
 with s == 110:
 result |= e
 with s == 111:
 result |= e

# Simulate and test your design for 16 cycles using random inputs
# < add your code here >


sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

import random
for cycle in range(16):
    # Call "sim.step" to simulate each clock cycle of the design
    sim.step({
        'a': random.choice([000, 001, 010, 011, 100, 101, 110, 111]),
        'b': random.choice([000, 001, 010, 011, 100, 101, 110, 111]),
        'c': random.choice([000, 001, 010, 011, 100, 101, 110, 111]),
        'd': random.choice([000, 001, 010, 011, 100, 101, 110, 111]),
        'e': random.choice([000, 001, 010, 011, 100, 101, 110, 111]),
        's': random.choice([000, 001, 010, 011, 100, 101, 110, 111])
        })

# Print the trace results to the screen.
print('--- 3-bit 5:1 MUX Simulation ')
sim_trace.render_trace()
