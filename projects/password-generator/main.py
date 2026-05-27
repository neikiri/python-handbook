"""Password Generator - Generate secure random passwords."""

import argparse
import secrets
import string
import sys


def generate_password(length=12, include_symbols=True):
    """Generate a random password.
    
    Args:
        length: Length of the password (minimum 4)
        include_symbols: Whether to include special characters
        
    Returns:
        A randomly generated password string
    """
    if length < 4:
        length = 4
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Build character pool
    pool = lowercase + uppercase + digits
    if include_symbols:
        pool += symbols
    
    # Ensure at least one character from each required set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits)
    ]
    
    if include_symbols:
        password.append(secrets.choice(symbols))
    
    # Fill the rest with random characters
    while len(password) < length:
        password.append(secrets.choice(pool))
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)


def main():
    """Main function to run the password generator."""
    parser = argparse.ArgumentParser(
        description="Generate a secure random password."
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length of the password (minimum 4, default: 12)"
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclude special characters from the password"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)"
    )
    
    args = parser.parse_args()
    
    # Validate length
    if args.length < 4:
        print("Error: Password length must be at least 4.")
        sys.exit(1)
    
    # Generate and display passwords
    print("\n" + "=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)
    
    for i in range(args.number):
        password = generate_password(args.length, not args.no_symbols)
        print(f"\nPassword {i + 1}: {password}")
    
    print("\n" + "=" * 40)
    print("Generated using Python's secrets module for security.")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    main()