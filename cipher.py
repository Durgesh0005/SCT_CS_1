def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift_amount) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("❌ Invalid choice.")
        return
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g. 3): "))
    except ValueError:
        print("❌ Shift value must be an integer.")
        return

    output = caesar_cipher(message, shift, mode=choice)
    print(f"\n✅ The {choice}ed message is:\n{output}")

if __name__ == "__main__":
    main()
