"""
Text Cleanup - Cleaning and Normalizing Text

This example demonstrates:
- Removing extra whitespace
- Converting to consistent case
- Removing punctuation
- Normalizing text for comparison
"""

import string


def clean_whitespace(text):
    """Remove extra whitespace from text."""
    # strip() removes leading/trailing whitespace
    cleaned = text.strip()
    
    # replace multiple spaces with single space
    cleaned = " ".join(cleaned.split())
    
    return cleaned


def to_lowercase(text):
    """Convert text to lowercase."""
    return text.lower()


def remove_punctuation(text):
    """Remove punctuation from text."""
    # Create translation table: map punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def normalize_text(text):
    """Clean and normalize text for comparison."""
    # Strip whitespace, convert to lowercase, remove punctuation
    cleaned = clean_whitespace(text)
    cleaned = to_lowercase(cleaned)
    cleaned = remove_punctuation(cleaned)
    return cleaned


def clean_user_input():
    """Demonstrate cleaning user input."""
    print("=== Cleaning User Input ===")
    
    # Simulated user input with extra spaces and mixed case
    user_input = "   Hello, WORLD!   "
    print(f"Original: '{user_input}'")
    
    # Clean it
    cleaned = clean_whitespace(user_input)
    print(f"Cleaned (whitespace): '{cleaned}'")
    
    # Normalize it
    normalized = normalize_text(user_input)
    print(f"Normalized: '{normalized}'")
    print()


def compare_texts():
    """Compare texts ignoring case and punctuation."""
    print("=== Text Comparison ===")
    
    text1 = "Hello, World!"
    text2 = "hello world"
    text3 = "Hello, world!!!"
    
    print(f"Text 1: '{text1}'")
    print(f"Text 2: '{text2}'")
    print(f"Text 3: '{text3}'")
    print()
    
    # Direct comparison (case-sensitive, punctuation matters)
    print(f"text1 == text2: {text1 == text2}")  # False
    print(f"text1 == text3: {text1 == text3}")  # False
    print()
    
    # Normalized comparison
    norm1 = normalize_text(text1)
    norm2 = normalize_text(text2)
    norm3 = normalize_text(text3)
    
    print(f"Normalized 1: '{norm1}'")
    print(f"Normalized 2: '{norm2}'")
    print(f"Normalized 3: '{norm3}'")
    print()
    
    print(f"norm1 == norm2: {norm1 == norm2}")  # True
    print(f"norm1 == norm3: {norm1 == norm3}")  # True
    print()


def extract_words(text):
    """Extract words from text."""
    # Clean and split into words
    cleaned = clean_whitespace(text)
    words = cleaned.split()
    return words


def count_words(text):
    """Count words in text."""
    words = extract_words(text)
    return len(words)


def clean_text_examples():
    """Run various text cleaning examples."""
    print("=== Text Cleaning Examples ===")
    
    examples = [
        "   Hello,   World!   ",
        "Python   is   FUN!!!",
        "  multiple   spaces   here  ",
        "Punctuation, is! annoying?",
    ]
    
    for example in examples:
        cleaned = clean_whitespace(example)
        normalized = normalize_text(example)
        word_count = count_words(example)
        
        print(f"Original: '{example}'")
        print(f"  Cleaned: '{cleaned}'")
        print(f"  Normalized: '{normalized}'")
        print(f"  Word count: {word_count}")
        print()


def is_similar(text1, text2, threshold=0.8):
    """
    Check if two texts are similar (simple version).
    Uses normalized comparison.
    """
    norm1 = normalize_text(text1)
    norm2 = normalize_text(text2)
    return norm1 == norm2


def similarity_examples():
    """Demonstrate text similarity checking."""
    print("=== Text Similarity ===")
    
    pairs = [
        ("Hello, World!", "hello world"),
        ("Python is fun", "python is FUN!"),
        ("Different text", "Not similar at all"),
    ]
    
    for text1, text2 in pairs:
        similar = is_similar(text1, text2)
        print(f"'{text1}'")
        print(f"  vs '{text2}': {similar}")
        print()


if __name__ == "__main__":
    clean_user_input()
    compare_texts()
    clean_text_examples()
    similarity_examples()
