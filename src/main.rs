fn main() {
    println!("{}", get_greeting());
}

fn get_greeting() -> &'static str {
    "Hello, World!"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_greeting() {
        assert_eq!(get_greeting(), "Hello, World!");
    }

    #[test]
    fn test_greeting_not_empty() {
        assert!(!get_greeting().is_empty());
    }

    #[test]
    fn test_greeting_length() {
        assert_eq!(get_greeting().len(), 13);
    }
}
