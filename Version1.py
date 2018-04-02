# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message
# call send_message() in the IPython Shell with the following questions:
# "what's today's weather?"
# "what's your name?"
# "what's your favorite color?"

# Adding variety to the responses
# Import the random module
import random

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

  # Answering Questions:

	def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


	# Send messages ending in a question mark
	send_message("what's today's weather?")
	send_message("what's today's weather?")

	# Send messages which don't end with a question mark
	send_message("I love building chatbots")
	send_message("I love building chatbots")

# Creating a dictionary "rules"
	
	rules = {'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'], 'do you think (.*)': ['if {0}? Absolutely.', 'No chance'], 'do you remember (.*)': ['Did you think I would forget {0}', "Why haven't you been able to forget {0}", 'What about {0}', 'Yes .. and?'], 'I want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"]}

# Extracting key phrases using "re" package
	# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase

		# Test match_rule
		print(match_rule(rules, "do you remember your last birthday"))

## Adding pronouns to sound more grammatically coherent
# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub("me", "you", message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub("my", "your", message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub("your", "my", message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub("you", "me", message)

    return message

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))
