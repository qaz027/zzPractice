''' Lesson

Managing Multi-Turn Agentic Conversations
Introduction & Lesson Overview

Welcome back! In the last lesson, you explored the details of the RunResult object and learned how to chain agents together using the OpenAI Agents SDK. You saw how to extract important information from an agent’s run and how to use the to_input_list() method to pass context between agents. This knowledge is essential for building more advanced workflows.

In this lesson, we will focus on a key feature of interactive agents: multi-turn conversations. Many real-world applications — such as chatbots, virtual assistants, and customer support agents — require the ability to remember and build upon previous exchanges. This is what makes interactions feel natural and coherent. By the end of this lesson, you will know how to manage and update conversation history using the to_input_list() method, enabling your agents to handle seamless, multi-turn interactions.
Recap of Agent Results and Conversation History

Let’s briefly review what you learned about the RunResult object. When you run an agent, the SDK returns a RunResult object that contains several useful properties: the original input, a list of new items (such as messages or tool calls), the final output, and the last agent executed. One of the most important features for multi-turn conversations is the to_input_list() method.

The to_input_list() method is designed to make managing conversation history easy. When you call this method on a RunResult object, it returns a list of message dictionaries. Each dictionary has a role (either "user" or "assistant") and a content field containing the text of the message. This format matches what the agent expects as input for the next turn. This method gives you the full conversation history in a format that the agent can understand for the next turn.

Preserving conversation history is crucial in multi-turn interactions. Without it, the agent would treat each message as a brand-new conversation, forgetting everything that happened before. By keeping track of both user and assistant messages, you ensure that the agent can respond in a way that makes sense, referencing earlier parts of the conversation as needed.

Let’s walk through a practical example that demonstrates how to manage a multi-turn conversation using the to_input_list() method.
Step 1: Set Up the Agent and Imports

To begin, import the necessary modules and create your agent. In this example, we’ll make a comedian agent that tells jokes on a given topic.

Python

import asyncio

import json

from agents import Agent, Runner


# Create an agent

agent = Agent(

    name="Comedian",

    instructions="You are a comedian that tells jokes on a given topic",

    model="gpt-4.1"

)


async def main():

    # The main conversation logic will go here


if __name__ == "__main__":

    asyncio.run(main())

Step 2: Initialize Conversation History and Add the First User Message

Start the conversation by initializing an empty conversation history. Then, add the first user message to this history.

Python

# Initialize conversation history as an empty list

conversation_history = []


# Define the first user message

first_message = "Tell me a joke about AI"


# Add the first message to the conversation history

conversation_history.append({"role": "user", "content": first_message})

Step 3: Run the Agent and Display the First Exchange

Pass the conversation history to the agent and print both the user’s message and the agent’s response.

Python

# Run the agent with the current conversation history

result = await Runner.run(

    starting_agent=agent,

    input=conversation_history

)


# Print the user's message and the agent's reply

print(f"User: {first_message}\n")

print(f"Assistant: {result.final_output}\n")

When you run this code, you'll see the user's message and the assistant's reply printed out:

Plain text

User: Tell me a joke about AI


Assistant: Why did the AI get kicked out of art class?


Because every time it tried to paint, it just kept drawing a blank!

Step 4: Update Conversation History Using to_input_list()

After the agent responds, update the conversation history using the to_input_list() method. This ensures the history now includes both the user’s message and the assistant’s reply.

Python

# Update the conversation history with the agent's output

conversation_history = result.to_input_list()

Step 5: Add a Second User Message and Continue the Conversation

Now, add a second user message to the conversation history and repeat the process to keep the conversation going.

Python

# Define a second user message

second_message = "Tell me another one on the same topic"


# Add the second message to the conversation history

conversation_history.append({"role": "user", "content": second_message})


# Run the agent again with the updated conversation history

result = await Runner.run(

    starting_agent=agent,

    input=conversation_history

)


# Print the user's message and the agent's reply

print(f"User: {second_message}\n")

print(f"Assistant: {result.final_output}\n")

If you try this next bit, you'll get the second user message and the assistant's new response—notice how the agent keeps up with the conversation and already knows the topic:

Plain text

User: Tell me another one on the same topic


Assistant: Why did the AI break up with its laptop?


Because it found it too *space*-y and not enough *person*-ality!

Step 6: Update and Review the Full Conversation History

Update the conversation history again with the latest result, then print the entire conversation to see how it has evolved.

Python

# Update the conversation history with the latest result

conversation_history = result.to_input_list()


# Print the full conversation history

print(f"Conversation history:\n{json.dumps(conversation_history, indent=2)}")

Once you update and print the conversation history, you'll see the full back-and-forth so far:

Plain text

Conversation history:

[

  {

    "role": "user",

    "content": "Tell me a joke about AI"

  },

  {

    "id": "msg_6810f0426c9081929bd4d71fb79ca68b0e49e9a42c739291",

    "content": [

      {

        "annotations": [],

        "text": "Why did the AI get kicked out of art class?\n\nBecause every time it tried to paint, it just kept drawing a blank!",

        "type": "output_text"

      }

    ],

    "role": "assistant",

    "status": "completed",

    "type": "message"

  },

  {

    "role": "user",

    "content": "Tell me another one on the same topic"

  },

  {

    "id": "msg_6810f043d02c8192a1b74358be0b91100e49e9a42c739291",

    "content": [

      {

        "annotations": [],

        "text": "Why did the AI break up with its laptop?\n\nBecause it found it too *space*-y and not enough *person*-ality!",

        "type": "output_text"

      }

    ],

    "role": "assistant",

    "status": "completed",

    "type": "message"

  }

]

By following these steps, you can build a natural, back-and-forth conversation with your agent, where each turn builds on the previous ones and the context is preserved throughout.
Summary & Preparation for Practice Exercises

In this lesson, you learned how to manage and update conversation history using the to_input_list() method, enabling your agents to handle seamless multi-turn interactions. You saw how to initialize a conversation, update it with each new message, and pass the evolving history back to the agent. This approach is essential for building interactive applications where context matters.

By following best practices — such as managing token limits and keeping your conversation history well-structured — you can create agents that feel natural and engaging. You are now ready to practice these skills in the upcoming exercises. Keep up the great work, and get ready to

'''

''' Python - Lesson '''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)

# Initialize conversation history as an empty list
conversation_history = []

# Define the first user message
first_message = "Tell me a joke about AI"

# Add the first message to the conversation history
conversation_history.append({"role": "user", "content": first_message})

async def main():
    # The main conversation logic will go here

if __name__ == "__main__":
    asyncio.run(main())

# Run the agent with the current conversation history
result = await Runner.run(
    starting_agent=agent,
    input=conversation_history
)

# Print the user's message and the agent's reply
print(f"User: {first_message}\n")
print(f"Assistant: {result.final_output}\n")

'''
User: Tell me a joke about AI

Assistant: Why did the AI get kicked out of art class?

Because every time it tried to paint, it just kept drawing a blank!
'''

# Define a second user message
second_message = "Tell me another one on the same topic"

# Add the second message to the conversation history
conversation_history.append({"role": "user", "content": second_message})

# Run the agent again with the updated conversation history
result = await Runner.run(
    starting_agent=agent,
    input=conversation_history
)

# Print the user's message and the agent's reply
print(f"User: {second_message}\n")
print(f"Assistant: {result.final_output}\n")

'''
User: Tell me another one on the same topic

Assistant: Why did the AI break up with its laptop?

Because it found it too *space*-y and not enough *person*-ality!
'''

# Update the conversation history with the latest result
conversation_history = result.to_input_list()

# Print the full conversation history
print(f"Conversation history:\n{json.dumps(conversation_history, indent=2)}")

'''
Conversation history:
[
  {
    "role": "user",
    "content": "Tell me a joke about AI"
  },
  {
    "id": "msg_6810f0426c9081929bd4d71fb79ca68b0e49e9a42c739291",
    "content": [
      {
        "annotations": [],
        "text": "Why did the AI get kicked out of art class?\n\nBecause every time it tried to paint, it just kept drawing a blank!",
        "type": "output_text"
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  },
  {
    "role": "user",
    "content": "Tell me another one on the same topic"
  },
  {
    "id": "msg_6810f043d02c8192a1b74358be0b91100e49e9a42c739291",
    "content": [
      {
        "annotations": [],
        "text": "Why did the AI break up with its laptop?\n\nBecause it found it too *space*-y and not enough *person*-ality!",
        "type": "output_text"
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  }
]
'''

''' Exercise 1 '''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)


async def main():
    # TODO: Initialize conversation history as an empty list
    conversation_history = []

    # TODO: Define the first user message
    first_message = "Tell me a joke about AI Agents"

    # TODO: Append the first message to the conversation history
    conversation_history.append({"role": "user", "content": first_message})


    # Run the agent with the current conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the user's message and the agent's reply
    print(f"User: {first_message}\n")
    print(f"Assistant: {result.final_output}\n")

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 2

You’ve just practiced starting a conversation and getting a response from your agent. Now, let’s take the next step and make sure your agent can remember what was said by updating the conversation history after the first exchange.

Your task is to:

    Use the agent’s to_input_list() method on the result after the first run to update the conversation_history variable.
    Print the updated conversation history using json.dumps() so you can see that it now includes both the user’s message and the agent’s reply.

This step is important for building agents that can keep track of the conversation as it grows.
'''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)


async def main():
    # Initialize conversation history as an empty list
    conversation_history = []

    # Define the first user message
    first_message = "Tell me a joke about AI Agents"

    # Append the first message to the conversation history
    conversation_history.append({"role": "user", "content": first_message})

    # Run the agent with the current conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the user's message and the agent's reply
    print(f"User: {first_message}\n")
    print(f"Assistant: {result.final_output}\n")

    # TODO: Update the conversation history with the agent's output
    conversation_history = result.to_input_list()

    # TODO: Print the updated conversation history
    print(f"Conversation history:\n{json.dumps(conversation_history, indent=2)}")

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 2 Output

User: Tell me a joke about AI Agents

Assistant: Why did the AI agent get kicked out of the bar?

Because it couldn’t stop trying to optimize everyone’s conversations!

Conversation history:
[
  {
    "role": "user",
    "content": "Tell me a joke about AI Agents"
  },
  {
    "id": "msg_688edaeb46d4819882e7312e7349baa80f47448c8e3c7a5f",
    "content": [
      {
        "annotations": [],
        "text": "Why did the AI agent get kicked out of the bar?\n\nBecause it couldn\u2019t stop trying to optimize everyone\u2019s conversations!",
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  }
]
'''

'''Exercise 3

You’ve just learned how to update the conversation history after your agent’s first response. Now, let’s see how your agent handles a real back-and-forth by adding another turn to the conversation.

Your task is to extend the conversation by having the user ask for another joke on the same topic. Here’s what you need to do:

    Define a second user message, such as "Tell me another one on the same topic".
    Add this new message to the existing conversation_history.

Once you complete these two steps, the code will automatically run the agent again and print out the new exchange. This will let you see how the agent responds when the conversation continues.

'''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)


async def main():
    # Initialize conversation history as an empty list
    conversation_history = []

    # Define the first user message
    first_message = "Tell me a joke about AI Agents"

    # Append the first message to the conversation history
    conversation_history.append({"role": "user", "content": first_message})

    # Run the agent with the current conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the user's message and the agent's reply
    print(f"User: {first_message}\n")
    print(f"Assistant: {result.final_output}\n")

    # Update the conversation history with the agent's output
    conversation_history = result.to_input_list()

    # TODO: Define the second user message (e.g., "Tell me another one on the same topic")
    second_message = "Tell me another one on the same topic"

    # TODO: Append the second message to the conversation history
    conversation_history.append({"role":"user","content":second_message})

    # Run the agent again with the updated conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the new user's message and the agent's reply
    print(f"User: {second_message}\n")
    print(f"Assistant: {result.final_output}\n")

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 3 Output

User: Tell me a joke about AI Agents

Assistant: Why did the AI agent apply for a job?

Because it wanted to earn some *cache*!

User: Tell me another one on the same topic

Assistant: Why did the AI agent get kicked out of the party?

Because it couldn’t stop trying to optimize everyone’s behavior!
'''

''' Exercise 4 

You’ve just seen how to keep a conversation going with your agent by adding new user messages and running the agent again. Now, let’s make sure your agent’s memory is up to date by saving the full conversation history after the second turn.

Your task is to:

    Update the conversation_history variable by using the agent’s to_input_list() method after the second run.
    Print the complete conversation history in a nicely formatted way using json.dumps().

This will help you see all the messages from both the user and the agent in the correct order. Keeping the full history is important for building agents that can follow along in longer chats.

'''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)


async def main():
    # Initialize conversation history as an empty list
    conversation_history = []

    # Define the first user message
    first_message = "Tell me a joke about AI Agents"

    # Append the first message to the conversation history
    conversation_history.append({"role": "user", "content": first_message})

    # Run the agent with the current conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the user's message and the agent's reply
    print(f"User: {first_message}\n")
    print(f"Assistant: {result.final_output}\n")

    # Update the conversation history with the agent's output
    conversation_history = result.to_input_list()

    # Define the second user message
    second_message = "Tell me another one on the same topic"

    # Append the second message to the conversation history
    conversation_history.append({"role": "user", "content": second_message})

    # Run the agent again with the updated conversation history
    result = await Runner.run(
        starting_agent=agent,
        input=conversation_history
    )

    # Print the new user's message and the agent's reply
    print(f"User: {second_message}\n")
    print(f"Assistant: {result.final_output}\n")

    # TODO: Update the conversation history with the agent's output after the second run
    conversation_history = result.to_input_list()

    # TODO: Print the full conversation history as formatted JSON
    print(f"Conversation history:\n{json.dumps(conversation_history, indent=2)}")

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 4

You’ve just practiced how to keep the conversation history updated after each exchange with your agent. Now, let’s see how you can handle several user queries in a row while making sure your agent remembers the whole conversation.

Your task is to work with an array of queries. For each query, you should:

    Add the user’s message to the conversation history.
    Run the agent using the current conversation history.
    Print both the user’s message and the agent’s reply.
    Update the conversation history with the result's to_input_list().

After all queries have been processed, print the complete conversation history so you can see the full back-and-forth.

This exercise will help you see how to manage multi-turn conversations in a loop, just like a real chat application.

'''

import asyncio
import json
from agents import Agent, Runner

# Create an agent
agent = Agent(
    name="Comedian",
    instructions="You are a comedian that tells jokes on a given topic",
    model="gpt-4.1"
)


async def main():
    # Initialize conversation history as an empty list
    conversation_history = []

    # Define an array of queries
    queries = [
        "Tell me a joke about AI",
        "Tell me another one",
        "Tell me the first joke again"
    ]

    # TODO: Iterate over each query
    for query in queries:
        # TODO: Add the user query to the conversation history
        conversation_history.append({"role":"user", "content":query})
        # TODO: Run the agent with the current conversation history
        result = await Runner.run(
            starting_agent=agent,
            input=conversation_history
        )
        # TODO: Print the user's query and the agent's reply
        print(f"User: {query}\n")
        print(f"Assistant: {result.final_output}\n")

        # TODO: Update the conversation history with the result's to_input_list()
        conversation_history = result.to_input_list()

    # TODO: Print the full conversation history at the end
    print(f"Conversation history:\n{json.dumps(conversation_history, indent=2)}")

if __name__ == "__main__":
    asyncio.run(main())

''' output '''
'''
User: Tell me a joke about AI

Assistant: Why did the AI cross the road?

To optimize its chicken detection algorithm… but now it’s stuck questioning if it’s a chicken or just a very advanced rubber duck.

User: Tell me another one

Assistant: Why did the AI go to therapy?

Because it had too many neural issues and kept getting lost in thought loops!

User: Tell me the first joke again

Assistant: Sure! Here it is:

Why did the AI cross the road?

To optimize its chicken detection algorithm… but now it’s stuck questioning if it’s a chicken or just a very advanced rubber duck.

Conversation history:
[
  {
    "role": "user",
    "content": "Tell me a joke about AI"
  },
  {
    "id": "msg_688ede0ea884819aa764b6df32e04874083e8facd01cbd5a",
    "content": [
      {
        "annotations": [],
        "text": "Why did the AI cross the road?\n\nTo optimize its chicken detection algorithm\u2026 but now it\u2019s stuck questioning if it\u2019s a chicken or just a very advanced rubber duck.",
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  },
  {
    "role": "user",
    "content": "Tell me another one"
  },
  {
    "id": "msg_688ede0fe450819aa4421f0612a8cf90083e8facd01cbd5a",
    "content": [
      {
        "annotations": [],
        "text": "Why did the AI go to therapy?\n\nBecause it had too many neural issues and kept getting lost in thought loops!",
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  },
  {
    "role": "user",
    "content": "Tell me the first joke again"
  },
  {
    "id": "msg_688ede11e3e0819abaa97771ca355400083e8facd01cbd5a",
    "content": [
      {
        "annotations": [],
        "text": "Sure! Here it is:\n\nWhy did the AI cross the road?\n\nTo optimize its chicken detection algorithm\u2026 but now it\u2019s stuck questioning if it\u2019s a chicken or just a very advanced rubber duck.",
        "type": "output_text",
        "logprobs": []
      }
    ],
    "role": "assistant",
    "status": "completed",
    "type": "message"
  }
]
'''