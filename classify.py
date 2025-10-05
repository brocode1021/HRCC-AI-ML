import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def train_model():

    training_data = [
        {'text': 'Urgent: You have won a 1 million dollar prize, claim now!', 'label': 'spam'},
        {'text': 'Buy cheap viagra online and get free shipping', 'label': 'spam'},
        {'text': 'Your account has been compromised, please update your password immediately', 'label': 'spam'},
        {'text': 'Exclusive deal: 50% off on all products for a limited time', 'label': 'spam'},
        {'text': 'Congratulations! You are the lucky winner of our lottery.', 'label': 'spam'},
        {'text': 'Click here to get a risk-free trial of our new product', 'label': 'spam'},
        {'text': 'Earn extra cash from home, apply now', 'label': 'spam'},
        {'text': 'FREE entry to win a new car. Enter your details now', 'label': 'spam'},

        {'text': 'Hi team, please find the attached report for our quarterly meeting.', 'label': 'not spam'},
        {'text': 'Hello, just checking in to see how you are doing. Let me know if you need anything.',
         'label': 'not spam'},
        {'text': 'Your Amazon order for "The Art of Programming" has been shipped.', 'label': 'not spam'},
        {'text': 'Reminder: Parent-teacher meeting tomorrow at 4 PM in the school auditorium.', 'label': 'not spam'},
        {'text': 'Could you please review the latest document and provide feedback?', 'label': 'not spam'},
        {'text': 'Your appointment with Dr. Smith is confirmed for next Tuesday.', 'label': 'not spam'},
        {'text': 'Here is the invoice for your recent purchase.', 'label': 'not spam'},
        {'text': 'The project schedule has been updated. Please see the attachment.', 'label': 'not spam'},
    ]

    df = pd.DataFrame(training_data)
    X_train = df['text']
    y_train = df['label']

    vectorizer = CountVectorizer(stop_words='english')
    X_train_counts = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(X_train_counts, y_train)

    return model, vectorizer


def main():
    print("--- Email Spam Classifier ---")
    print("Training an improved model...")

    model, vectorizer = train_model()

    print("Model trained successfully.")
    print("You can now enter email text to classify it as 'spam' or 'not spam'.")
    print("Type 'exit' or 'quit' to close the program.\n")

    while True:
        email_input = input("Enter email text > ")

        if email_input.lower() in ['exit', 'quit']:
            print("Exiting classifier. Goodbye!")
            break

        if not email_input.strip():
            print("Warning: Please enter some text to classify.\n")
            continue

        email_input_counts = vectorizer.transform([email_input])
        prediction = model.predict(email_input_counts)[0]

        print(f"\n   >>> Prediction: {prediction.upper()} <<<\n")


if __name__ == "__main__":
    main()

