print("=" * 60)
print("        PHISHING AWARENESS TRAINING")
print("=" * 60)

print("\nWhat is Phishing?")
print("Phishing is a cyber attack where attackers impersonate trusted")
print("people or organizations to steal sensitive information.")

print("\nCommon Phishing Signs:")
signs = [
    "Suspicious or unknown sender address",
    "Urgent or threatening messages",
    "Unexpected attachments",
    "Suspicious links or unusual URLs",
    "Requests for passwords, OTPs or financial information",
    "Spelling and grammatical mistakes",
    "Offers that appear too good to be true"
]

for i, sign in enumerate(signs, 1):
    print(f"{i}. {sign}")

print("\nBest Practices:")
tips = [
    "Verify the sender before responding.",
    "Do not click suspicious links.",
    "Check website URLs carefully.",
    "Never share passwords or OTPs.",
    "Enable multi-factor authentication.",
    "Keep software and security tools updated.",
    "Report suspicious emails or messages."
]

for i, tip in enumerate(tips, 1):
    print(f"{i}. {tip}")

print("\nQuick Phishing Quiz")
print("-" * 60)

questions = [
    ("An email asks you to urgently verify your bank account using a link.", "no"),
    ("You receive an unexpected attachment from an unknown sender.", "no"),
    ("You independently open the official website instead of clicking an email link.", "yes")
]

score = 0

for question, correct in questions:
    print("\nScenario:", question)
    answer = input("Is it safe? (yes/no): ").lower().strip()

    if answer == correct:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Be cautious with unexpected requests.")

print("\n" + "=" * 60)
print(f"Quiz Score: {score}/{len(questions)}")
print("=" * 60)

if score == len(questions):
    print("Excellent! You understand the basics of phishing awareness.")
elif score >= 2:
    print("Good job! Continue practicing safe browsing habits.")
else:
    print("Keep learning and always verify suspicious messages.")
