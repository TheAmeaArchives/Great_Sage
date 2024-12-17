# 🌟 Great Sage

## ✨ Introduction

Welcome to **Great Sage**, a modern Socratic tool designed to uncover the essence of personality traits through text and handwriting analysis. Inspired by the probing questions of Socrates and grounded in modern psychological research, Great Sage uses innovative techniques to provide deep insights into individuals' personalities and preferences.

## 🛠️ Features

### 📝 1. Text Analysis for Personality Insights

Great Sage evaluates the use of functional words in texts to reveal aspects of an individual’s personality. This feature draws on principles from the book “The Secret Life of Pronouns” to uncover underlying traits and behavioral tendencies.

### ✍️ 2. Handwriting Analysis

Using advanced image processing and analysis, Great Sage can interpret handwriting to infer details about an individual’s personality. Handwriting speaks volumes about the writer, and this feature unlocks those insights.

### 🎵 3. Music Genre Inference

Based on text and conversational inputs, Great Sage can make educated guesses about your favorite genre of music. These inferences add another dimension to understanding your preferences and personality.

### 💬 4. Behavioral Concept Conversations

Engage with Great Sage in conversations about behavioral and psychological concepts. This feature provides an interactive way to explore your personality, akin to having a modern ChatGPT-like experience.

## 🧰 Technologies Used

Great Sage relies on the following technologies to deliver its features:

- **`re`** (Regular Expressions): For parsing and processing text data efficiently.
- **spaCy:** A robust library for natural language processing (NLP), enabling advanced text analysis.
- **Django:** The web framework used to create a seamless and interactive user experience.
- **Pillow:** For image processing, particularly in analyzing handwriting samples.

## 🛠️ Installation

To get started with Great Sage, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd great-sage
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/MacOS
   env\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## 💻 Usage

1. Access Great Sage in your browser at `http://127.0.0.1:8000` after starting the development server.
2. Upload text files or handwriting samples for analysis.
3. Interact with the conversational feature to explore behavioral concepts and personalized insights.

## 🤝 Contributing

We welcome contributions to Great Sage! If you have ideas for features or improvements:

1. Fork the repository and create a new branch for your feature or fix.
2. Make your changes and submit a pull request with a detailed explanation.
3. Ensure all tests pass before submitting your PR.

## 🙌 Acknowledgments

Great Sage is inspired by the works of James W. Pennebaker, particularly his book “The Secret Life of Pronouns.” We also thank the open-source community for the tools and frameworks that made this project possible.

---

Start your journey of self-discovery with **Great Sage** today!

