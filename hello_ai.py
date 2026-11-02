# hello_ai.py
# Brett Whitney
# CSCI 130 - Week 1 Project
# Date: 11/1/26
 
import random
import datetime
 
def greeting_agent():
    """
    A simple AI agent that provides personalized greetings.
    This demonstrates a simple reflex agent from Chapter 2.
    """
 
    current_hour = datetime.datetime.now().hour
 
    if current_hour < 12:
        time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
    else:
        time_period = "evening"
 
    name = input("What's your name? ")
 
    greetings = [
        f"Good {time_period}, {name}! Welcome to AI class!",
        f"Hello {name}! Hope you're having a great {time_period}!",
        f"Hi {name}! Ready to learn AI this {time_period}?"
    ]
 
    print(random.choice(greetings))
 
    mood = input("\nHow are you feeling about learning AI? ")
 
    if "excited" in mood.lower() or "good" in mood.lower():
        print("That's wonderful! Your enthusiasm will help you learn!")
    elif "nervous" in mood.lower() or "worried" in mood.lower():
        print("Don't worry! We'll take it step by step.")
    elif "confused" in mood.lower() or "lost" in mood.lower():
        print("It's okay to feel that way! We'll clarify things as we go.")
    else:
        print("Thanks for sharing! Let's make this a great learning experience!")
    
 
    ai_facts = [
        "Did you know? The term 'Artificial Intelligence' was coined in 1956!",
        "Fun fact: Your smartphone uses AI for face recognition!",
        "AI insight: Netflix uses AI to recommend shows you might like!",
        "Did you know? AI helps doctors detect diseases earlier!"
        "Fun fact: In 1997, IBM's Deep Blue became the first AI to defeat a reigning world chess champion!",
        "Self-driving cars use computer vision AI to detect lane lines and read road signs in real time!"
    ]
 
    print(f"\n{random.choice(ai_facts)}")
    print("\nLet's start our AI journey together!")
 
 
if __name__ == "__main__":
    print("=" * 50)
    print("Welcome to CSCI 130: Introduction to AI")
    print("=" * 50)
    print()
    greeting_agent()