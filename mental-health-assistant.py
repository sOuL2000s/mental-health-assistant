import random

# Sample affirmations and relaxation exercises
affirmations = [
    "You are strong and capable.",
    "Believe in yourself and your abilities.",
    "Today is a new opportunity to grow."
]
exercises = [
    "Take a deep breath and hold for 5 seconds, then exhale.",
    "Close your eyes and focus on positive thoughts for 1 minute.",
    "Try a quick 5-minute meditation session."
]

# Function to check mood and provide support
def mental_health_check(mood):
    if mood in ["stressed", "anxious"]:
        return random.choice(exercises)
    else:
        return random.choice(affirmations)

# User input
mood = "stressed"  # Example mood

# Provide support
support_message = mental_health_check(mood)
print("Suggested activity:", support_message)
