use itertools::Itertools;

fn main() {
    let data: Vec<i32> = include_str!("../../data.txt")
        .split("\n")
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    for (first, second) in data.iter().tuple_combinations() {
        if first + second == 2020 {
            println!("2 {}", first * second);
        }
    }

    for (first, second, third) in data.iter().tuple_combinations() {
        if first + second + third == 2020 {
            println!("3 {}", first * second * third);
        }
    }
}
