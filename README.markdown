# Password Generator

## Overview
This Python script generates a random password of a user-specified length and saves it to a file (`passwords.txt`) along with a description of its intended use and a timestamp. The password is created using ASCII characters (from 33 to 126) and includes basic input validation to ensure the password length is greater than 4 characters.

## Features
- Generates random passwords using ASCII characters.
- Ensures a minimum password length of 5 characters.
- Saves generated passwords to `passwords.txt` with:
  - Usage location (e.g., email, website).
  - Date and time of generation.
- Simple command-line interface for ease of use.

## Prerequisites
- Python 3.x installed on your system.
- No external libraries are required (uses standard `random` and `datetime` modules).

## Installation
1. Save the script as `password_generator.py`.
2. Ensure Python 3 is installed. You can verify this by running:
   ```bash
   python3 --version
   ```
3. No additional dependencies are needed.

## Usage
1. Run the script using Python:
   ```bash
   python3 password_generator.py
   ```
2. Follow the prompts:
   - Enter the desired password length (must be greater than 4).
   - Specify where the password will be used (e.g., "email", "website").
3. The generated password will be displayed and saved to `passwords.txt` in the same directory as the script.

### Example Interaction
```
Welcome to the password generator
Tell me how long you want your password to be: 3
Password length must be greater than 4. Please try again.
Tell me how long you want your password to be: 8
Generating password...
Kj#9mP$2
Where are you going to use this password? (e.g., email, website): email
Password saved with location: email
```

### Output File (`passwords.txt`)
The generated password and its details are appended to `passwords.txt`. Example content:
```
Used for: email
Password: Kj#9mP$2
Date/Time: 2025-04-16 12:34:56
```

## Limitations
- Passwords are stored in plain text in `passwords.txt`, which is not secure for sensitive applications.
- The `random` module is used, which is not cryptographically secure. For stronger passwords, consider using the `secrets` module.
- No error handling for file I/O issues or invalid input types (e.g., non-integer input for length).

## Future Improvements
- Use the `secrets` module for cryptographically secure password generation.
- Add encryption for storing passwords securely.
- Implement input validation for non-integer inputs.
- Allow users to customize character sets (e.g., exclude special characters).
- Add an option to view previously saved passwords securely.

## License
This project is unlicensed and provided as-is for educational purposes.