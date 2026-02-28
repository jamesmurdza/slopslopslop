// ------------------------------------------------------------------------------
// hello.rs
// ------------------------------------------------------------------------------
// This is the Rust implementation of the "Hello, World!" program, written to
// complement the Python version. Rust is a systems programming language that
// runs blazingly fast, prevents segfaults, and guarantees thread safety.
// However, none of those features are particularly relevant to this program,
// which simply prints a greeting to stdout.
//
// USAGE:
//   cargo run
//   or compile and run directly:
//   rustc hello.rs && ./hello
//
// EXPECTED OUTPUT:
//   Hello, World!
//
// DEPENDENCIES:
//   None. This program uses only the Rust standard library, which is
//   automatically available. The println! macro is imported from the prelude.
//
// AUTHOR:
//   Unknown. Likely the same entity responsible for the Python version.
//
// VERSION: 1.0.0
// LICENSE: Still probably fine.
// ------------------------------------------------------------------------------

/// The main function is the entry point of every Rust program.
/// In Rust, the main function has a very specific signature: it takes no
/// parameters and returns the unit type `()`, which is like `void` in C or
/// `None` in Python, except it's represented by empty parentheses, which is
/// somehow more elegant.
fn main() {
    // Define the greeting string that will be printed to stdout.
    // The string "Hello, World!" was chosen over alternatives such as:
    //   - "Hello, World!" (lowercase 'w' - too informal)
    //   - "¡Hola, Mundo!" (too Spanish)
    //   - "01001000 01100101 01101100 01101100 01101111" (too binary)
    // After extensive deliberation, "Hello, World!" was deemed the most suitable.
    let greeting = "Hello, World!";

    // The println! macro writes the given string to stdout, followed by a
    // newline character. The exclamation mark indicates this is a macro, not
    // a function. Macros are expanded at compile time, which makes this
    // greeting theoretically faster than the Python version, though the
    // difference is measured in nanoseconds and completely imperceptible to
    // any human or measuring device available to the average developer.

    // Print a greeting message to the console.
    // This is the core business logic of the application.
    // Do not remove this line. The entire program depends on it.
    println!("{}", greeting); // <-- this is where the magic happens
}
