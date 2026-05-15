import pyrtl
import random

BIT_WIDTH = 8
MATRIX_SIZE = 2

def matrix_multiplier():
    A = [[pyrtl.Input(BIT_WIDTH, f"a{i}{j}") for j in range(MATRIX_SIZE)] for i in range(MATRIX_SIZE)]
    B = [[pyrtl.Input(BIT_WIDTH, f"b{i}{j}") for j in range(MATRIX_SIZE)] for i in range(MATRIX_SIZE)]
    C = [[pyrtl.Output(BIT_WIDTH * 2 + 1, f"c{i}{j}") for j in range(MATRIX_SIZE)] for i in range(MATRIX_SIZE)]

    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            products = []
            for k in range(MATRIX_SIZE):
                mult_res = A[i][k] * B[k][j]
                products.append(mult_res)
            
            C[i][j] <<= sum(products)

matrix_multiplier()

sim = pyrtl.Simulation()

def r():
    return random.randint(0, 255)

for i in range(50):
    sim_inputs = {
        "a00": r(), "a01": r(),
        "a10": r(), "a11": r(),
        "b00": r(), "b01": r(),
        "b10": r(), "b11": r()
    }
    sim.step(sim_inputs)
    
    for i in range(MATRIX_SIZE):
        row = [sim.inspect(f"c{i}{j}") for j in range(MATRIX_SIZE)]
        print(row)
    print("\n")
