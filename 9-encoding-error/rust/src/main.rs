use itertools::Itertools;

fn main() {
    let data: Vec<u64> = include_str!("../../data.txt")
        .split("\n")
        .filter_map(|s| s.parse::<u64>().ok())
        .collect();

    let invalid_code = data
        .windows(26)
        .map(|win| win.split_last().unwrap())
        .filter(|(code, previous_values)| {
            previous_values
                .iter()
                .tuple_combinations()
                .find(|(first, second)| *first + *second == **code)
                .is_none()
        })
        .next()
        .expect("Failed to find invalid code")
        .0
        .clone();

    println!("1 {}", invalid_code);

    for window_size in 2..data.len() {
        match data
            .windows(window_size)
            .find(|win| win.into_iter().sum::<u64>() == invalid_code)
        {
            None => continue,
            Some(w) => {
                println!("2 {}", w.iter().min().unwrap() + w.iter().max().unwrap());
                break;
            }
        }
    }
}
