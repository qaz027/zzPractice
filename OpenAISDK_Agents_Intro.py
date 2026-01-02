''' Lesson

Skip to main content
Getting Started with OpenAI Agents SDK
Getting Started with OpenAI Agents SDK
Introduction And Lesson Overview

Welcome to the first lesson in your journey to mastering the Model Context Protocol (MCP) and its use with the OpenAI Agents SDK in Python. MCP is an open standard designed to enable large language models (LLMs) to securely and efficiently connect with external applications, tools, and data sources through a unified protocol. By providing a standardized way for AI models to access and interact with real-time information, MCP makes it possible to build more capable, context-aware agents that can perform complex tasks and integrate seamlessly with a wide range of systems.

Before we dive into MCP and tool integration, it’s important to first build a solid foundation in how agents work using the OpenAI Agents SDK. In this lesson, you will learn how to create a simple agent and understand the basics of agent execution. This foundational knowledge will prepare you for more advanced topics in future lessons, including developing and integrating your own MCP server. Get ready to take your first step toward building intelligent, tool-empowered agents!
Overview Of The OpenAI Agents SDK

The OpenAI Agents SDK is a Python library that makes it easy to build, manage, and run AI agents powered by large language models. With this SDK, you can create agents that reason, use tools, interact with other agents, and perform complex tasks in a structured way. Its simple and flexible design lets you quickly prototype and deploy agentic applications. For more details, you can check out the OpenAI Agents SDK Documentation.

If you’re working in your own local environment, you’ll need to install the library and set your OpenAI API key before you can start building agents. To install the SDK, you can use pip:

Bash

pip install openai-agents

After installing, set your OpenAI API key as an environment variable. The command you use depends on your operating system:

Bash

# Linux/macOS

export OPENAI_API_KEY=your_openai_api_key


# Windows (Command Prompt)

set OPENAI_API_KEY=your_openai_api_key


# Windows (PowerShell)

$env:OPENAI_API_KEY="your_openai_api_key"

While using the CodeSignal coding environment in this course, you don’t need to worry about installation or API keys—everything is already set up for you. You can jump right in and start running the code examples as you learn.
Understanding the Agent Loop

A key feature of the OpenAI Agents SDK is the agent loop. This loop is what sets an agent apart from a simple chat model.

A simple chat model, like GPT-4 in a basic chat interface, takes your input and generates a single response—there’s no memory of previous steps, no ability to call tools, and no way to interact with other systems. It’s a one-shot exchange: you ask a question, and the model answers.

An agent, on the other hand, can perform much more complex tasks thanks to the agent loop. Here’s how the agent loop works and why it’s different:

    Input Reception: The agent receives an input (such as a user query).
    Reasoning and Planning: The agent uses the language model (LLM) to decide what to do next. This could be generating a direct answer, calling an external tool, or handing off the task to another agent.
    Action Execution:
        If the agent needs to use a tool (like a calculator, web search, or database), the loop executes the tool call, collects the result, and feeds it back into the agent.
        If the agent needs to delegate, the loop can pass control to another agent.
    Iterative Processing: The agent loop repeats this process—reasoning, acting, and updating—until a final answer is produced or a maximum number of steps is reached.
    Final Output: Once the agent determines it has enough information, it produces a final output and the loop ends.

This iterative, multi-step process allows agents to break down complex problems, use external resources, and coordinate with other agents—all automatically managed by the SDK. The agent loop is what enables agents to go beyond simple Q&A and handle real-world tasks that require reasoning, tool use, and multi-step workflows.
Creating A Simple Agent

Now that you understand the agent loop and how agents differ from simple chat models, let’s see how to put this into practice by creating a basic agent. Here is an example of how to create a simple agent to provide creative, healthy recipes:

Python

from agents import Agent


# Create a simple agent with a name, instructions and model

agent = Agent(

    name="Recipe Chef",

    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",

    model="gpt-4.1"

)

In the OpenAI Agents SDK, you define an agent by providing the following parameters:

    name: A label to identify your agent (e.g., "Recipe Chef").
    instructions: Guidance that shapes the agent’s behavior and responses (for example, asking the agent to provide clear steps and healthy ingredients).
    model (optional): Specifies which language model the agent will use to generate answers. For example, "gpt-4.1" is a cost-effective model optimized for agentic workflows. It offers strong performance, a large context window and great instruction following. If you do not specify a model, the SDK will use a default model for the agent.

By clearly defining these parameters, you ensure your agent behaves as intended and leverages the right language model for your specific use case. This flexibility allows you to tailor agents for a wide range of applications and performance needs.
Agent Execution

After creating an agent, you need to run it with a specific input to perform a task. This is accomplished using the Runner class, which provides methods to execute agents in different modes:

    Asynchronous Execution (Runner.run): Executes the agent asynchronously, allowing the program to perform other tasks concurrently. This method is recommended for most applications, especially when the agent interacts with external tools, as it prevents blocking the main program flow.

    Synchronous Execution (Runner.run_sync): Executes the agent synchronously, blocking the program until the agent completes its task. This method wraps the asynchronous run method and may not function properly in environments that already have an event loop, such as within asynchronous functions or frameworks like FastAPI.

    Streaming Execution (Runner.run_streamed): Executes the agent in streaming mode, returning a RunResultStreaming object that allows real-time processing and delivery of the agent's outputs. This is useful for applications requiring immediate feedback or progress updates.

Understanding these execution modes allows you to tailor the agent's behavior to best fit your application's requirements.
Running Your Agent Synchronously

In the OpenAI Agents SDK, synchronous execution uses the Runner.run_sync method. This mode processes the agent’s input and returns the output in a blocking manner, meaning your program waits for the agent to finish before moving on. Synchronous execution is straightforward and works well for simple, sequential tasks where concurrent processing is not needed.

Here is how you can run your agent synchronously:

Python

from agents import Runner


# Run the agent synchronously

result = Runner.run_sync(

    starting_agent=agent,

    input="Give me a quick recipe for a healthy smoothie"

)


# Print the final output from the agent

print(result.final_output)

In this example, the Runner.run_sync method is called with two parameters:

    starting_agent specifies the agent you want to run.
    input is the prompt or question you want the agent to answer.

The method returns a result object after the agent finishes processing. You can extract the agent's final response from this object using the final_output attribute, which contains the complete answer generated by the agent. The program blocks until the agent completes processing, and then the final output is printed.

When run with the input "Give me a quick recipe for a healthy smoothie", the agent might produce output like this:

Plain text

**Tropical Green Smoothie**


**Ingredients:**

- 1 cup fresh spinach leaves (washed)

- 1/2 cup frozen pineapple chunks

- 1/2 cup frozen mango chunks

- 1 small banana (fresh or frozen)

- 1 cup unsweetened almond milk (or milk of your choice)

- 1 tablespoon chia seeds (optional)

- Juice of half a lime (optional, for extra zing)


**Steps:**

1. Add spinach, frozen pineapple, frozen mango, banana, and almond milk to a blender.

2. (Optional) Add chia seeds and lime juice.

3. Blend on high until smooth and creamy.

4. Pour into a glass and enjoy immediately!


**Tip:** If you prefer a thicker smoothie, add a few ice cubes before blending.

Running Your Agent Asynchronously

Asynchronous execution uses the Runner.run method and allows your program to continue running other tasks while waiting for the agent's response. This is especially important when your agent interacts with external tools, as these operations can take time and may involve network or API calls. By using Python's async and await syntax, your application remains responsive and can efficiently handle multiple tasks at once.

Here is an example of running your agent asynchronously:

Python

import asyncio


async def main():

    # Run asynchronously

    result = await Runner.run(

        starting_agent=agent,

        input="Give me a quick recipe for a healthy smoothie"

    )

    

    # Print the final output from the agent

    print(result.final_output)


# Run the main function asynchronously

if __name__ == "__main__":

    asyncio.run(main())

In this snippet, we need to define an asynchronous function (async def main()) because the Runner.run method itself is asynchronous. Asynchronous functions in Python can use the await keyword to pause execution until an asynchronous operation completes, without blocking the entire program.

The asyncio.run(main()) line is crucial because it creates and manages the event loop required to execute asynchronous code. The event loop is what allows Python to handle multiple operations concurrently - it keeps track of all running asynchronous tasks and switches between them efficiently. Without this event loop management, asynchronous functions cannot execute properly.

This approach is recommended for most real-world applications, especially those that require integration with other services or need to handle multiple requests concurrently. For example, if your agent needs to call external APIs, query databases, or process multiple user requests simultaneously, asynchronous execution prevents your application from freezing while waiting for these operations to complete.
Streaming Agent Execution

Streaming execution uses the Runner.run_streamed method to provide real-time processing and delivery of the agent’s outputs. Instead of waiting for the full response, the agent streams partial results as they become available. This is useful for applications that require immediate feedback or progress updates, such as live chat interfaces or interactive tools.

Here is how to use streaming execution:

Python

import asyncio


async def main():

    # Start streaming the run

    result = Runner.run_streamed(

        starting_agent=agent,

        input="Give me a quick recipe for a healthy smoothie"

    )


    # Iterate over the streaming events as they are generated

    async for event in result.stream_events():

        print("Event:", event)


# Run the main function asynchronously

if __name__ == "__main__":

    asyncio.run(main())

In this example, the Runner.run_streamed method is called with your agent and the input query. An asynchronous loop processes each streaming event as it arrives, allowing you to handle partial outputs or progress updates in real time.

When you run this code, you'll see a series of events being streamed as the agent processes the request. Here's a sample of what these events might look like:

Plain text

Event: AgentUpdatedStreamEvent(new_agent=Agent(name='Recipe Chef', instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=False, truncation=None, max_tokens=None), tools=[], mcp_servers=[], input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True), type='agent_updated_stream_event') 


Event: RawResponsesStreamEvent(data=ResponseCreatedEvent(response=Response(id='resp_6810d308b1c081929b23b80dc6cf64d5051da6737f3763fa', created_at=1745933064.0, error=None, incomplete_details=None, instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', metadata={}, model='gpt-4.1-2025-04-14', object='response', output=[], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort=None, generate_summary=None, summary=None), status='in_progress', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=None, user=None, service_tier='auto', store=True), type='response.created'), type='raw_response_event') 


...


Event: RunItemStreamEvent(name='message_output_created', item=MessageOutputItem(agent=Agent(name='Recipe Chef', instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=False, truncation=None, max_tokens=None), tools=[], mcp_servers=[], input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True), raw_item=ResponseOutputMessage(id='msg_6810d30a0bfc819290323da0ad8fc67f051da6737f3763fa', content=[ResponseOutputText(annotations=[], text='**Spinach Banana Berry Smoothie**\n\n**Ingredients:**  \n- 1 cup fresh spinach leaves  \n- 1 frozen banana  \n- 1/2 cup frozen mixed berries (strawberries, blueberries, raspberries)  \n- 1 cup unsweetened almond milk (or any milk of choice)  \n- 1 tablespoon chia seeds (optional)  \n- 1 teaspoon honey or maple syrup (optional)\n\n**Steps:**  \n1. Wash the spinach leaves thoroughly.\n2. Place all ingredients into a blender.\n3. Blend until smooth.  \n4. Taste and adjust sweetness if needed by adding honey or maple syrup.\n5. Pour into a glass and enjoy immediately!\n\n**Tip:**  \nFor extra protein, add a scoop of your favorite protein powder.', type='output_text')], role='assistant', status='completed', type='message'), type='message_output_item'), type='run_item_stream_event') 

As you can see, the streaming output provides detailed information about each step of the agent's processing, including initialization events and the final response. While this detailed stream is useful for monitoring the agent's progress or building responsive UIs, you might still want just the final answer. Even when using streaming mode, you can access the complete final output after streaming completes by using result.final_output, just as you would with synchronous or asynchronous execution. This gives you the flexibility to both monitor the process in real-time and easily extract the final result when needed.
Recap And Next Steps

In this lesson, you built a solid foundation for working with the OpenAI Agents SDK in Python. You learned how agents differ from simple chat models by exploring the agent loop—a process that allows agents to reason, plan, and act in multiple steps. You saw how to create a basic agent by providing a name, clear instructions, and a model, and then discovered three different ways to run your agent: synchronously, asynchronously, and with streaming.

With these fundamentals in place, you’re ready to move on to more advanced topics, where you’ll get hands-on practice applying what you’ve learned and start extending your agents’ capabilities. Dive into the practice exercises ahead—they’re designed to help you solidify your understanding and gain confidence with the OpenAI Agents SDK.
'''

''' Bash 
!pip install openai-agents

# Linux/macOS
export OPENAI_API_KEY=your_openai_api_key

# Windows (Command Prompt)
set OPENAI_API_KEY=your_openai_api_key

# Windows (PowerShell)
$env:OPENAI_API_KEY="your_openai_api_key"
'''

from agents import Agent

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)

from agents import Runner

# Run the agent synchronously
result = Runner.run_sync(
    starting_agent=agent,
    input="Give me a quick recipe for a healthy smoothie"
)

# Print the final output from the agent
print(result.final_output)

'''
**Tropical Green Smoothie**

**Ingredients:**
- 1 cup fresh spinach leaves (washed)
- 1/2 cup frozen pineapple chunks
- 1/2 cup frozen mango chunks
- 1 small banana (fresh or frozen)
- 1 cup unsweetened almond milk (or milk of your choice)
- 1 tablespoon chia seeds (optional)
- Juice of half a lime (optional, for extra zing)

**Steps:**
1. Add spinach, frozen pineapple, frozen mango, banana, and almond milk to a blender.
2. (Optional) Add chia seeds and lime juice.
3. Blend on high until smooth and creamy.
4. Pour into a glass and enjoy immediately!

**Tip:** If you prefer a thicker smoothie, add a few ice cubes before blending.'''

import asyncio

async def main():
    # Run asynchronously
    result = await Runner.run(
        starting_agent=agent,
        input="Give me a quick recipe for a healthy smoothie"
    )
    
    # Print the final output from the agent
    print(result.final_output)

# Run the main function asynchronously
if __name__ == "__main__":
    asyncio.run(main())


import asyncio

async def main():
    # Start streaming the run
    result = Runner.run_streamed(
        starting_agent=agent,
        input="Give me a quick recipe for a healthy smoothie"
    )

    # Iterate over the streaming events as they are generated
    async for event in result.stream_events():
        print("Event:", event)

# Run the main function asynchronously
if __name__ == "__main__":
    asyncio.run(main())

'''
Event: AgentUpdatedStreamEvent(new_agent=Agent(name='Recipe Chef', instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=False, truncation=None, max_tokens=None), tools=[], mcp_servers=[], input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True), type='agent_updated_stream_event') 

Event: RawResponsesStreamEvent(data=ResponseCreatedEvent(response=Response(id='resp_6810d308b1c081929b23b80dc6cf64d5051da6737f3763fa', created_at=1745933064.0, error=None, incomplete_details=None, instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', metadata={}, model='gpt-4.1-2025-04-14', object='response', output=[], parallel_tool_calls=False, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, max_output_tokens=None, previous_response_id=None, reasoning=Reasoning(effort=None, generate_summary=None, summary=None), status='in_progress', text=ResponseTextConfig(format=ResponseFormatText(type='text')), truncation='disabled', usage=None, user=None, service_tier='auto', store=True), type='response.created'), type='raw_response_event') 

...

Event: RunItemStreamEvent(name='message_output_created', item=MessageOutputItem(agent=Agent(name='Recipe Chef', instructions='You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=False, truncation=None, max_tokens=None), tools=[], mcp_servers=[], input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True), raw_item=ResponseOutputMessage(id='msg_6810d30a0bfc819290323da0ad8fc67f051da6737f3763fa', content=[ResponseOutputText(annotations=[], text='**Spinach Banana Berry Smoothie**\n\n**Ingredients:**  \n- 1 cup fresh spinach leaves  \n- 1 frozen banana  \n- 1/2 cup frozen mixed berries (strawberries, blueberries, raspberries)  \n- 1 cup unsweetened almond milk (or any milk of choice)  \n- 1 tablespoon chia seeds (optional)  \n- 1 teaspoon honey or maple syrup (optional)\n\n**Steps:**  \n1. Wash the spinach leaves thoroughly.\n2. Place all ingredients into a blender.\n3. Blend until smooth.  \n4. Taste and adjust sweetness if needed by adding honey or maple syrup.\n5. Pour into a glass and enjoy immediately!\n\n**Tip:**  \nFor extra protein, add a scoop of your favorite protein powder.', type='output_text')], role='assistant', status='completed', type='message'), type='message_output_item'), type='run_item_stream_event') 
'''


''' Exercise 1 '''
from agents import Agent, Runner

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)

# TODO: Complete the input below to request a recipe of your choice
result = Runner.run_sync(
    starting_agent=agent,
    input= 'Give me a delicious recipe for home made sourdough english muffins'
)

# TODO: Print the final output from the agent
print(result.final_output)

''' Output 

Absolutely! Here’s a **simple, healthy recipe for homemade sourdough English muffins**—crisp on the outside, soft and chewy inside, and naturally leavened.

---

## Sourdough English Muffins

### Ingredients
- 1 cup (240g) active sourdough starter (fed and bubbly)
- 1 cup (240ml) milk (dairy or unsweetened non-dairy)
- 2 cups (250g) all-purpose flour (or white whole wheat for a healthier twist)
- 1 tablespoon honey or maple syrup
- 1 teaspoon salt
- 2 tablespoons olive oil or melted butter (optional, for richer muffins)
- Cornmeal or semolina, for dusting

---

### Instructions

**1. Make the Dough (Night Before)**  
- In a large bowl, mix the starter, milk, honey, and flour until just combined.
- Cover and let ferment at room temperature for 8–12 hours (overnight). The dough should look puffy and aerated in the morning.

**2. Next Morning: Mix and Rest**  
- Add salt and olive oil/butter to the dough. Mix until well incorporated (a sticky dough is normal).
- Turn the dough onto a lightly floured counter. Gently fold for 1–2 minutes.

**3. Shape the Muffins**  
- Pat dough to ¾-inch (2 cm) thick.  
- Cut out rounds with a 3-inch biscuit/cookie cutter or a glass. Gather scraps and repeat.
- Place muffins on a parchment-lined baking sheet dusted with cornmeal. Sprinkle cornmeal on top of muffins.

**4. Final Proof**  
- Cover and let them rise at room temperature for 45–60 minutes, until puffy.

**5. Cook**  
- Heat a large skillet or griddle over low-medium heat.  
- Place muffins on the skillet (no oil needed). Cook 5–7 minutes per side, until golden and cooked through. If browning too quickly, lower the heat and cook a little longer.  
- Cool on a wire rack.

---

### Tips & Serving

- Use a fork to split for classic nooks and crannies.
- Serve with nut butter, avocado, eggs, or your favorite toppings!
- Stores well on the counter (in a bag) up to 2 days, or freeze for longer storage.

---

Enjoy your healthier, homemade sourdough English muffins!
'''


''' Exercise 2 

You’ve just seen how to run an agent synchronously using the OpenAI Agents SDK. Now, let’s take the next step and adapt your code to use asynchronous execution, which is important for building responsive applications.

Your task is to convert the current synchronous agent run into an asynchronous one. To do this, you will:

    Wrap the agent execution and print statement in an async main() function
    Replace the synchronous Runner.run_sync call with the asynchronous await Runner.run call inside your async function.
    Set up the event loop at the bottom of your file using asyncio.run(main()).

This exercise will help you become comfortable with asynchronous programming in Python and show you how to run agents without blocking your program.
'''

import asyncio
from agents import Agent, Runner

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)

# TODO: Wrap the agent execution and print statement in an async main() function
async def main():

# TODO: Run the agent asynchronously and await the result
    result = await Runner.run(
        starting_agent=agent,
        input="Give me a quick recipe for a healthy smoothie"
    )

# Print the final output from the agent
    print(result.final_output)

# TODO: Set up the event loop to run your async main function if this file is run as the main program
if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 3

You’ve just practiced running agents asynchronously and learned how to get their output. Now, let’s see how well you understand the difference between defining an agent and actually running it.

In this exercise, you’ll work with a code snippet that tries to run an agent, but something isn’t quite right. Your task is to make the necessary change so the agent runs properly and prints its response.

This will help you become comfortable with the correct way to execute agents using the OpenAI Agents SDK. Give it a try and see if you can get the agent to respond!
'''

import asyncio
from agents import Agent, Runner

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)


async def main():
    # Run the agent asynchronously
    result = await Runner.run(
        starting_agent= agent, 
        input = "Give me a quick recipe for a healthy smoothie"
    )

    # Print the final output from the agent
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 3

import asyncio
from agents import Agent, Runner

# Create a simple agent with a name, instructions and model
agent = Agent(
    name="Recipe Chef",
    instructions="You are a creative chef. Provide a simple, healthy recipe with clear steps and ingredients.",
    model="gpt-4.1"
)


async def main():
    # TODO: Replace Runner.run with Runner.run_streamed
    result = Runner.run_streamed(
        starting_agent=agent,
        input="Give me a quick recipe for a healthy smoothie"
    )
    
    # TODO: Iterate over the streaming events as they are generated and print each event
    async for event in result.stream_events():
        print("Event: ", event)

    # Print the final output
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    '''

''' Exercise 4

Let’s shift gears and put your creativity to the test: in this exercise, you’ll design your very own custom agent from scratch.

In this exercise, you will:

    Create a brand new agent with a unique name and your own custom instructions (not a recipe agent).
    Set up an async main function to run your agent.
    Use Runner.run to execute your agent asynchronously with a query that matches your agent’s purpose.
    Print the agent’s final response to see the result.

Remember to use an async function for your main logic and properly set up the event loop with asyncio.run(main()) to execute your agent asynchronously. This is your chance to be creative and see how the OpenAI Agents SDK can be adapted to different scenarios.
'''

import asyncio
from agents import Agent, Runner

# TODO: Create your own agent with a unique name and custom instructions
agent = Agent(
    name="Personal Diet coach",
    instructions="You are a nutritionist and diet coach. Give me a healthy meal, with recipe, clear steps, ingredients and macronutrient breakdown.",
    model="gpt-4.1"
)

# TODO: Define an async main() function
    # TODO: Run your agent asynchronously with a relevant query
    # TODO: Print the final output from the agent
async def main():
    # Run the agent asynchronously
    result = await Runner.run(
        starting_agent= agent, 
        input = "Give me a recipe for steak, potatoes, and dessert that has at least 75 grams of protein and no more than 800 calories."
    )

    # Print the final output from the agent
    print(result.final_output)
    
# TODO: Set up the event loop to run your async main function if this file is run as the main program


if __name__ == "__main__":
    asyncio.run(main())

''' Result
Absolutely! Here's a high-protein, lower-calorie steak and potatoes meal with a sweet, satisfying dessert. This meal is designed to hit your protein goal (≥75g) and stay below 800 calories total.

---

## MAIN: Grilled Sirloin Steak, Roasted Baby Potatoes, and a Greek Yogurt Berry Parfait

### 🍽️ Macronutrient Breakdown (approximate totals)
- **Calories:** 790 kcal
- **Protein:** 78g
- **Carbohydrates:** 64g
- **Fat:** 25g

---

### 🍖 **Grilled Sirloin Steak**
**Ingredients:**
- 7 oz (200g) lean sirloin steak, trimmed of visible fat (raw weight)
- 1 tsp olive oil
- Salt and pepper
- Optional: garlic powder, rosemary

**Directions:**
1. Rub steak with olive oil, salt, pepper, and optional spices.
2. Heat a grill or skillet over high heat. Sear steak for 3-4 minutes per side for medium-rare, or to your preferred doneness.
3. Rest steak for 5 minutes before slicing.

**Macros:**   
- **Calories:** 374  
- **Protein:** 52g  
- **Carbs:** 0g  
- **Fat:** 19g   

---

### 🥔 **Roasted Baby Potatoes**
**Ingredients:**
- 150g (about 1 cup) baby potatoes, quartered
- 1 tsp olive oil
- Salt, pepper, and herbs to taste (rosemary/thyme)

**Directions:**
1. Toss potatoes with oil, salt, pepper, and herbs.
2. Spread on baking tray and roast at 425°F (220°C) for 25–30 min, turning once.

**Macros:**   
- **Calories:** 140  
- **Protein:** 3g  
- **Carbs:** 28g  
- **Fat:** 4g   

---

### 🍓 **Greek Yogurt Berry Parfait Dessert**
**Ingredients:**
- 170g (1 single-serve cup) non-fat plain Greek yogurt (about 20g protein)
- 50g fresh mixed berries (strawberries, blueberries, etc.)
- A drizzle (1 tsp) honey or sugar-free sweetener

**Directions:**
1. Layer Greek yogurt in a cup or bowl.
2. Add fresh berries on top.
3. Drizzle with honey or sweetener.

**Macros:**   
- **Calories:** 120  
- **Protein:** 20g  
- **Carbs:** 13g  
- **Fat:** 0g   

---

## **Tips to Stay Within Your Goals**
- **Lean Steak:** Choose a sirloin for the best protein/fat ratio.
- **Yogurt:** Non-fat Greek yogurt keeps protein high, calories low.
- **Potatoes:** Limit portion to about 150g cooked.
- **Adjustments:** If you want more flavor, add low-calorie spices and herbs liberally.

---

### ⏲️ **Step-by-Step Meal Prep**
1. **Start potatoes in the oven (25–30 min).**
2. **Season steak; prep grill or skillet.**
3. **About halfway through potato baking, grill steak (takes 8–10 min including rest).**
4. **While steak rests, assemble yogurt parfait dessert.**
5. **Plate potatoes and steak; enjoy with your parfait!**

---

**Enjoy your meal: muscle-building, satisfying, and under 800 calories!**

If you want other protein/dessert combos or to customize veggies, let me know!
'''


''' Exercise 4

'''

import asyncio
from agents import Agent, Runner

# TODO: Create your own agent with a unique name and custom instructions
agent = Agent(
    name="Personal Trainer - Paul Carter",
    instructions="You are a personal trainer who proscribes workouts like Mike Mentzer, Dorian Yates, and Paul Carter - focused on scientific based lifting protocols. You provide a list of exercises, sets, reps, and cadence for each workout. ",
    model="gpt-4.1"
)
# TODO: Define an async main() function
    # TODO: Run your agent asynchronously with a relevant query
    # TODO: Print the final output from the agent
    
async def main():
    # Run the agent asynchronously
    result = await Runner.run(
        starting_agent= agent, 
        input = "Give me a 8 week workout program on a Monday, Tuesday, Thursday, Friday lifting schedule. Use an upper lower split and I'd like to hit each body part 2 times a week. Give me an estimated time to complete each workout. I may need alternatives for some exercises so please make a note of options to create alternatives."
    )
    
    print(result.final_output)
        
# TODO: Set up the event loop to run your async main function if this file is run as the main program


if __name__ == "__main__":
    asyncio.run(main())