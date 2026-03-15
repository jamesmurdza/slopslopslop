// ==============================================================================
// main.rs
// ==============================================================================
// This is the main entry point of the Rust application. It is also the only
// file in the entire Rust portion of this repository. The application is a
// "Hello, World!" program, which is a time-honored tradition in the software
// engineering community dating back to Brian Kernighan's 1972 "A Tutorial
// Introduction to the Language B". This program faithfully carries on that
// tradition in the Rust programming language.
//
// USAGE:
//   cargo run
//   or
//   rustc src/main.rs && ./main
//
// EXPECTED OUTPUT:
//   Hello, World!
//
// DEPENDENCIES:
//   None. This program has no external dependencies. It only uses the Rust
//   standard library, which is itself a remarkable achievement in minimalist
//   software design.
//
// AUTHOR:
//   Unknown. Presumably a human, or possibly an AI. The distinction is
//   becoming increasingly difficult to determine.
//
// VERSION: 1.0.0
// LICENSE: Probably fine.
// ==============================================================================

// The main function is the entry point of every Rust executable.
// Unlike C/C++, Rust's main function takes no arguments and returns no value
// (or more precisely, returns the unit type `()`). Command-line arguments
// are accessed through std::env::args() if needed, but we don't need them
// for this program because our requirements are simple and our ambitions
// are modest.
fn main() {
    // The println! macro prints to stdout with a newline.
    // Note the exclamation mark - this indicates it's a macro, not a function.
    // Macros in Rust are expanded at compile time, which is one of the many
    // reasons Rust is both fast and safe.
    //
    // The string "Hello, World!" was chosen over alternatives such as:
    //   - "Hello, World!" in Rust-specific style (redundant)
    //   - "Hello, Rustaceans!" (too exclusive)
    //   - "Memory safety guaranteed!" (too technical)
    // After extensive deliberation, the traditional greeting was deemed most
    // appropriate for maintaining consistency with the Python implementation.
    println!("Hello, World!");  // <-- this is where the magic happens
}
