from pathlib import Path

CIR_HISTORY = set()
CIR = 0
PROGRAM = []
ACCUMULATOR = 0

with Path(__file__).parent.joinpath("data.txt").open() as f:
    for line in f.readlines():
        opcode, operand = line.strip().split(" ")
        PROGRAM.append((opcode, int(operand)))


def run_program(program):
    cir = 0
    cir_history = set()
    accumulator = 0

    while cir not in cir_history:
        cir_history.add(cir)
        try:
            opcode, operand = program[cir]
        except IndexError:
            break

        if opcode == "jmp":
            cir += operand
            continue

        cir += 1

        if opcode == "acc":
            accumulator += operand
    else:
        return accumulator, False

    return accumulator, True


print(1, run_program(PROGRAM)[0])


for i, (opcode, operand) in enumerate(PROGRAM):
    if opcode == "acc":
        continue

    new_program = PROGRAM.copy()

    if opcode == "jmp":
        new_program[i] = ("nop", operand)
    elif opcode == "nop":
        new_program[i] = ("jmp", operand)

    acc, terminate_success = run_program(new_program)
    if terminate_success:
        print(2, acc)
        break
