import base64

def main():
    original_text = input("Podaj tekst do zaszyfrowania: ")

    encrypted_text = base64.b64encode(original_text.encode()).decode()
    decrypted_text = base64.b64decode(encrypted_text).decode()

    print("\nOriginal Text:", original_text)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()
