import os


def offline_ai_response(prompt):
    text = prompt.lower()
    if "summarize" in text:
        content = prompt.split(":", 1)[-1].strip()
        words = content.split()
        short_summary = " ".join(words[:15]) + ("..." if len(words) > 15 else "")
        return f"Summary: {short_summary}"
    elif "quiz" in text or "question" in text:
        return "Sample Quiz Question: What is the difference between supervised and unsupervised learning?"
    else:
        return f"AI Assistant Response: Processed your request -> '{prompt}'"


def ask_gemini(prompt):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return offline_ai_response(prompt)

    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception:
        return offline_ai_response(prompt)


def main():
    print("=== AI Study & Productivity Assistant ===")
    while True:
        print("\n1. Summarize Study Notes")
        print("2. Generate Practice Quiz Question")
        print("3. Ask Custom AI Query")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            notes = input("Paste your notes: ").strip()
            print("\n" + ask_gemini(f"Summarize this in 2 bullet points: {notes}"))
        elif choice == "2":
            topic = input("Enter AI/ML topic: ").strip()
            print("\n" + ask_gemini(f"Create one short interview quiz question on {topic}"))
        elif choice == "3":
            query = input("Enter your prompt: ").strip()
            print("\n" + ask_gemini(query))
        elif choice == "4":
            print("Exiting AI Assistant.")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
