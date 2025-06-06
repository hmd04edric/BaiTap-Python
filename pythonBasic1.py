"""
String Manipulation Exercises
"""

def capitalize_sentence():
    """Capitalize first letter of each word in a sentence"""
    s = input("Enter a string: ").strip()
    words = s.split()
    result = " ".join(word[0].upper() + word[1:].lower() for word in words)
    print("Result:", result)

def reverse_words():
    """Reverse the order of words in a string"""
    s = input("Enter a string: ").strip()
    words = s.split()
    result = " ".join(reversed(words))
    print("Reversed:", result)

def find_most_common_char():
    """Find the most frequently occurring character"""
    s = input("Enter a string: ").replace(" ", "")
    if not s:
        print("No characters found")
        return
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    max_char = max(char_count, key=char_count.get)
    print(f"Most common character: '{max_char}' ({char_count[max_char]} occurrences)")

def count_char_occurrences():
    """Count occurrences of each character in a string"""
    s = input("Enter a string: ")
    char_count = {}
    
    for char in s:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    
    print("Character occurrences:")
    for char, count in char_count.items():
        print(f"'{char}': {count}")

def extract_numbers():
    """Extract all numbers from a string"""
    s = input("Enter a string: ")
    numbers = []
    current_num = ""
    
    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num:
            numbers.append(int(current_num))
            current_num = ""
    
    if current_num:
        numbers.append(int(current_num))
    
    print("Numbers found:", numbers if numbers else "No numbers found")

def split_fullname():
    """Split full name into first name and last name"""
    full_name = input("Enter full name: ").strip().split()
    if len(full_name) < 2:
        print("Please enter at least first and last name")
        return
    
    first_name = full_name[0]
    last_name = full_name[-1]
    middle_name = " ".join(full_name[1:-1]) if len(full_name) > 2 else ""
    
    print(f"First name: {first_name}")
    if middle_name:
        print(f"Middle name: {middle_name}")
    print(f"Last name: {last_name}")

def title_case():
    """Convert first letter of each word to uppercase"""
    s = input("Enter a string: ").strip()
    result = " ".join(word.capitalize() for word in s.split())
    print("Title case:", result)

def alternate_case():
    """Alternate between uppercase and lowercase letters"""
    s = input("Enter a string: ")
    result = ""
    for i, char in enumerate(s):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    print("Alternating case:", result)

def is_palindrome():
    """Check if a string is a palindrome"""
    s = input("Enter a string: ").lower().replace(" ", "")
    if s == s[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

def number_to_words():
    """Convert a 3-digit number to words"""
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
           "eighty", "ninety"]
    
    while True:
        try:
            num = int(input("Enter a 3-digit number (100-999): "))
            if 100 <= num <= 999:
                break
            print("Please enter a number between 100 and 999")
        except ValueError:
            print("Please enter a valid number")
    
    h = num // 100
    t = (num % 100) // 10
    u = num % 10
    
    words = []
    if h > 0:
        words.append(f"{units[h]} hundred")
    
    if t == 1:
        words.append(teens[u])
    else:
        if t > 1:
            words.append(tens[t])
        if u > 0:
            words.append(units[u])
    
    print(" ".join(words) if words else "zero")

def show_menu():
    """Display the menu of available functions"""
    print("\n=== STRING MANIPULATION EXERCISES ===")
    print("1. Capitalize sentence")
    print("2. Reverse words")
    print("3. Find most common character")
    print("4. Count character occurrences")
    print("5. Extract numbers from string")
    print("6. Split full name")
    print("7. Convert to title case")
    print("8. Alternate letter cases")
    print("9. Check palindrome")
    print("10. Number to words")
    print("0. Exit")

def main():
    """Main program loop"""
    functions = [
        capitalize_sentence,
        reverse_words,
        find_most_common_char,
        count_char_occurrences,
        extract_numbers,
        split_fullname,
        title_case,
        alternate_case,
        is_palindrome,
        number_to_words
    ]
    
    while True:
        show_menu()
        try:
            choice = int(input("\nChoose an exercise (0-10): "))
            if choice == 0:
                print("Goodbye!")
                break
            elif 1 <= choice <= 10:
                functions[choice - 1]()
                input("\nPress Enter to continue...")
            else:
                print("Please enter a number between 0 and 10")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()
