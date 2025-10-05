Email Spam Classifier
This 

project is a small program that learns to tell the difference between regular emails and spam.

It's a straightforward demonstration of how a computer can be taught to understand and categorize text. The program first studies a collection of example emails and then uses what it learns to make educated guesses about new text you provide. Everything happens right in your terminal.

How It Works

The program follows a few simple, logical steps to learn how to classify emails.

Learning from Examples

The program starts with a built-in list of emails that have already been labeled as either spam or not spam. This is the study material.

Teaching the Program to Read

A computer doesn't understand words, but it does understand numbers. This step turns the text from the emails into a numerical format. It does this by counting how many times each word appears in each message.

Finding the Patterns

Using a popular method for sorting text called Naive Bayes, the program analyzes the word counts. It learns which words tend to show up more often in spam (like "prize," "free," or "winner") and which are more common in regular emails.

Putting It to the Test

Once the training is complete, the program is ready. It will ask you to type in a sentence or a piece of an email. It will then use the patterns it learned to predict whether your text is spam or not.

The Tools Used

This program is built with a couple of key Python libraries that do the heavy lifting:

scikit-learn: This is the main toolkit that provides the machine learning intelligence for the classifier.

pandas: This is used to neatly organize the initial training data before the learning process begins.

Getting Started

You can get the classifier running on your own computer by following these steps.

Before You Begin

Please make sure you have Python 3 installed on your system.

1. Prepare Your Project Space

It's a good idea to create a dedicated folder for this project. Place the script file inside that folder.

2. List the Required Tools

In the same folder, create a file named requirements.txt. This file tells Python which libraries the program needs to function. Add these two lines to the file:

code

Txt

scikit-learn

pandas

3. Install the Tools

To keep things tidy, you can use a virtual environment. This creates a self-contained space for your project's libraries.

code

Bash

# Create and activate a virtual environment

python3 -m venv venv

source venv/bin/activate  # On macOS or Linux

# venv\Scripts\activate    # On Windows

# Now, install the libraries from your list

pip install -r requirements.txt

How to Run the Program

Once the setup is done, you can start the classifier from your terminal.

code

Bash

python classify.py

The program will tell you when its training is complete. Then, it will prompt you to enter some text.

Example Session

Here is what you can expect to see in your terminal:

code

Code

--- Email Spam Classifier ---

Training an improved model...

Model trained successfully.

You can now enter email text to classify it as 'spam' or 'not spam'.

Type 'exit' or 'quit' to close the program.

Enter email text > congratulations you have won a prize click now

   >>> Prediction: SPAM <<<

Enter email text > Hi, just following up on our meeting from yesterday.

   >>> Prediction: NOT SPAM <<<

Enter email text > quit
Exiting classifier. Goodbye.
