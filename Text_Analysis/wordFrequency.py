import spacy  # Import the spaCy library for natural language processing
nlp = spacy.load("en_core_web_md")  # Load the medium-sized English language model

text = "Hello hello hello" + " "  # Define the text to be processed and add a space at the end
new_word = str()  # Initialize an empty string to build words
text_data = {}  # Initialize an empty dictionary to store word frequencies

# Loop through each character in the text
for i in text:
    if i != " ":  # If the character is not a space
        new_word += i.lower()  # Add the character to new_word in lowercase
    elif i == " ":  # If the character is a space
        if new_word in text_data:  # Check if the word is already in the dictionary
            text_data[new_word] += 1  # Increment the word's frequency by 1
        elif new_word not in text_data:  # If the word is not in the dictionary
            text_data[new_word] = 1  # Add the word to the dictionary with a frequency of 1
        new_word = ""  # Reset new_word to an empty string

print(text_data)  # Print the dictionary containing word frequencies

# Process the text using spaCy
doc = nlp(text)
print(doc)  # Print the processed text (a spaCy Doc object)

# Initialize an empty dictionary to store text classification data
text_classification = {}

# Loop through each token (word) in the processed text
for token in doc:
    # Add the token's text (in lowercase) to the dictionary with its part of speech and frequency
    text_classification[token.text.lower()] = {
        "Part of speech": token.pos_,  # Part of speech of the token
        "Frequency": text_data[token.text.lower()]  # Frequency of the token in the original text
    }

print(text_classification)  # Print the dictionary containing text classification data
