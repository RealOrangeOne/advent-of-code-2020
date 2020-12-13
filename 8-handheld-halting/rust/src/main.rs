use std::collections::HashSet;
use std::convert::TryInto;

#[derive(Debug, PartialEq, Clone)]
enum Opcode {
    JUMP,
    ACCUMULATE,
    NOOP,
}

impl From<&str> for Opcode {
    fn from(opcode: &str) -> Opcode {
        match opcode {
            "nop" => Opcode::NOOP,
            "jmp" => Opcode::JUMP,
            "acc" => Opcode::ACCUMULATE,
            _ => unreachable!(),
        }
    }
}

#[derive(Debug, Clone)]
struct Instruction {
    pub opcode: Opcode,
    pub operand: i16,
}

fn run_program(program: &Vec<Instruction>) -> (i16, bool) {
    let mut cir: u16 = 0;
    let mut cir_history: HashSet<u16> = HashSet::new();
    let mut accumulator: i16 = 0;
    let mut success = false;

    while !cir_history.contains(&cir) {
        cir_history.insert(cir);

        let instruction = match program.get(usize::from(cir)) {
            Some(i) => i,
            None => {
                success = true;
                break;
            }
        };

        if instruction.opcode == Opcode::JUMP {
            cir = (cir as i16 + instruction.operand).try_into().unwrap();
            continue;
        }

        cir += 1;

        match instruction.opcode {
            Opcode::JUMP => unreachable!(),
            Opcode::ACCUMULATE => accumulator += instruction.operand,
            Opcode::NOOP => (),
        }
    }

    return (accumulator, success);
}

fn main() {
    let program: Vec<Instruction> = include_str!("../../data.txt")
        .split_terminator("\n")
        .map(|s| s.split_whitespace().collect())
        .map(|d: Vec<&str>| {
            debug_assert_eq!(d.len(), 2);
            let opcode = d[0];
            let operand = d[1];
            Instruction {
                opcode: Opcode::from(opcode),
                operand: operand.parse::<i16>().expect("Failed to parse operand"),
            }
        })
        .collect();

    println!("1 {}", run_program(&program).0);

    for (i, instruction) in program.iter().enumerate() {
        let mut new_program = program.to_owned();

        match instruction.opcode {
            Opcode::ACCUMULATE => continue,
            Opcode::JUMP => {
                new_program[i] = Instruction {
                    opcode: Opcode::NOOP,
                    operand: instruction.operand,
                }
            }
            Opcode::NOOP => {
                new_program[i] = Instruction {
                    opcode: Opcode::JUMP,
                    operand: instruction.operand,
                }
            }
        }

        let (acc, success) = run_program(&new_program);
        if success {
            println!("2 {}", acc);
            break;
        }
    }
}
