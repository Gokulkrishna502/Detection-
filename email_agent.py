print("📧 Welcome to Smart Email Reply Agent!")
print("Type 'exit' to quit the program.\n")

# Predefined keywords and suggested replies (Expanded Version)
responses = {
    "meeting": "Sure, what time works for you?",
    "thanks": "You’re welcome! 😊",
    "thank you": "No problem! Happy to help.",
    "hello": "Hi there! How can I help you?",
    "urgent": "I will get back to you ASAP.",
    "project": "I will update you on the project soon.",
    "question": "I will answer your question shortly.",
    "invoice": "I will send you the invoice shortly.",
    "deadline": "I understand. Let's discuss the deadline.",
    "feedback": "Thank you for your feedback! I’ll review it.",
    "issue": "I am looking into the issue and will reply soon.",
    "support": "Our support team will contact you shortly.",
    "help": "Sure! I am here to help you.",
    "schedule": "Please let me know your available time.",
    "call": "I am available for a call. What time works for you?",
    "meeting link": "I will share the meeting link shortly.",
    "update": "I will send you an update soon."
}

# Email loop
while True:
    email = input("Enter email content: ").lower()
    
    # Exit condition
    if email == "exit":
        print("Agent: Goodbye! Have a great day 😊")
        break
    
    # Check for keywords
    found = False
    for key in responses:
        if key in email:
            print("Suggested Reply:", responses[key])
            found = True
            break
    
    # Default reply if no keyword matches
    if not found:
        print("Suggested Reply: I will check and get back to you.")
    
    print()  # Blank line for readability