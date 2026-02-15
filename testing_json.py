

import json

# ... inside capture_audio_from_file ...

# Load the context
with open('test.json', 'r') as f:
    context = json.load(f)

user_info = context['speechSupportType']

print(f"User speech support type: {user_info}")
