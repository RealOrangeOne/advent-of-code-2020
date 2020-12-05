use regex::Regex;

struct PasswordEntry {
    pub min_count: usize,
    pub max_count: usize,
    pub target_char: char,
    pub password_candidate: String,
}

fn main() {
    let matcher = Regex::new(r"^(\d+)\-(\d+) (\S+): (\S+?)$").expect("Invalid regex");

    let data: Vec<PasswordEntry> = include_str!("../../data.txt")
        .split("\n")
        .filter(|s| !s.is_empty())
        .map(|s| {
            let matches = matcher.captures(s).expect("Match failed");
            PasswordEntry {
                min_count: matches
                    .get(1)
                    .expect("Failed to get min_count")
                    .as_str()
                    .parse::<usize>()
                    .expect("min_count isn't usize"),
                max_count: matches
                    .get(2)
                    .expect("Failed to get max_count")
                    .as_str()
                    .parse::<usize>()
                    .expect("max_count isn't usize"),
                target_char: matches
                    .get(3)
                    .expect("Failed to get target_char")
                    .as_str()
                    .chars()
                    .next()
                    .expect("No char"),
                password_candidate: String::from(
                    matches
                        .get(4)
                        .expect("Failed to get password_candidate")
                        .as_str(),
                ),
            }
        })
        .collect();

    let valid_passwords_1 = data
        .iter()
        .filter(|entry| {
            let occurances = entry
                .password_candidate
                .chars()
                .filter(|c| c == &entry.target_char)
                .count() as usize;
            occurances >= entry.min_count && occurances <= entry.max_count
        })
        .count();

    println!("1 {}", valid_passwords_1);

    let valid_passwords_2 = data
        .iter()
        .filter(|entry| {
            let min_match = entry
                .password_candidate
                .chars()
                .nth(entry.min_count - 1)
                .expect("Overflow")
                == entry.target_char;
            let max_match = entry
                .password_candidate
                .chars()
                .nth(entry.max_count - 1)
                .expect("Overflow")
                == entry.target_char;
            min_match ^ max_match
        })
        .count();

    println!("2 {}", valid_passwords_2);
}
