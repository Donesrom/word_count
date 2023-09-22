import os
import socketserver
import http.server

def count_words(text, case_sensitive=True):
    # Split the text into words and count them
    if not case_sensitive:
        text = text.lower()  # Convert text to lowercase if case insensitive
    words = text.split()
    return len(words)

def main():
    print("Word Counter")
    print("-------------")

    # Input from the user
    user_input = input("Enter text or 'file:<filename>' to count words from a file: ")

    if user_input.startswith("file:"):
        # If the user specifies a file, read the file and count words
        filename = user_input[5:]
        try:
            with open(filename, "r") as file:
                text = file.read()
                word_count = count_words(text)
                print(f"Word count in '{filename}': {word_count}")
        except FileNotFoundError:
            print("File not found.")
    else:
        # Count words in the provided text
        word_count = count_words(user_input)
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
