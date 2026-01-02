import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)

# Define a Blog Writer agent
blog_agent = Agent(
    name="Blog Writer",
    instructions=(
        "You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post "
        "that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text."
    ),
    model="gpt-4.1"
)

async def main():
    # Run the Recipe Chef agent
    result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # Run the Blog Writer agent with the Recipe Chef agent's results
    result = await Runner.run(
        starting_agent=blog_agent,
        input=result.to_input_list() + [{"role": "user", "content": "Write a blog post about the recipe."}]
    )

    # Process the result...

if __name__ == "__main__":
    asyncio.run(main())


print(result.final_output)

'''
### Energize Your Morning with the Ultimate Green Breakfast Smoothie

There’s something empowering about starting the day off on a healthy note. For me, nothing sets the tone quite like a vibrant, nutrient-packed smoothie that fuels my morning with energy, flavor, and a little bit of zen. That’s why I’m excited to share my go-to recipe: the Green Energy Breakfast Smoothie! This wholesome blend of greens, fruits, and superfoods is perfect for busy mornings or as a quick pick-me-up any time of day.

#### Why You’ll Love This Smoothie

This recipe is more than just a pretty green drink—it’s a powerhouse of vitamins, fiber, and healthy fats to keep you full and focused. Fresh spinach loads you up on antioxidants and iron, while frozen mango and banana give natural sweetness and a creamy, dreamy texture. Chia seeds add a boost of omega-3s and protein, almond butter offers a touch of richness, and warming cinnamon and ginger give it a spicy kick. The best part? It’s incredibly easy to make and delicious enough for the whole family to enjoy.

#### Recipe: Green Energy Breakfast Smoothie

**Ingredients:**
- 1 cup unsweetened almond milk
...'''

print(result.last_agent)

'''
Agent(name='Blog Writer', instructions='You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=False, truncation=None, max_tokens=None), tools=[], mcp_servers=[], input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True)
'''

''' Exercise 1'''

import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # TODO: Print the original user input (use result.input)
    print(result.input)

    # TODO: Print the agent's final response (use result.final_output)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())


''' Exercise 1 - Output
Give me a recipe for a healthy smoothie.
**Green Power Glow Smoothie**

**Ingredients:**
- 1 cup fresh spinach leaves, packed
- 1/2 ripe avocado
- 1 frozen banana
- 1/2 cup frozen pineapple chunks
- 1 tablespoon chia seeds
- 1 cup unsweetened almond milk
- 1 tablespoon fresh lime juice
- 1 teaspoon honey (optional)

**Instructions:**
1. Place spinach, avocado, banana, pineapple, chia seeds, almond milk, lime juice, and honey (if using) into a blender.
2. Blend on high speed until smooth and creamy, about 45 seconds.
3. Taste and adjust sweetness by adding more honey if desired.
4. Pour into a glass and enjoy immediately.
'''

''' Exercise 2'''
import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # TODO: Print the list of new items (events/messages) from the agent's run
    print(result.new_items)

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 2 - Output'''
'''
[MessageOutputItem(agent=Agent(name='Recipe Chef', instructions='You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, and step-by-step instructions. Do not include extra commentary. Output only the recipe text.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=None, truncation=None, max_tokens=None, reasoning=None, metadata=None, store=None, include_usage=None, extra_query=None, extra_body=None, extra_headers=None), tools=[], mcp_servers=[], mcp_config={}, input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True), raw_item=ResponseOutputMessage(id='msg_688c31973c748198a280058c17908a880cf2df2c0b3f1b2c', content=[ResponseOutputText(annotations=[], text='**Green Glow Power Smoothie**\n\n**Ingredients:**  \n- 1 cup fresh spinach leaves  \n- 1 cup unsweetened almond milk  \n- 1 medium banana (fresh or frozen)  \n- 1/2 cup frozen pineapple chunks  \n- 1/2 cup cucumber, chopped  \n- 1 tablespoon chia seeds  \n- 1 tablespoon fresh lemon juice  \n- 1 teaspoon honey (optional)  \n- 3–4 ice cubes\n\n**Instructions:**  \n1. Add the spinach and almond milk to a blender. Blend until smooth and no leafy bits remain.  \n2. Add banana, pineapple, cucumber, chia seeds, lemon juice, and honey (if using).  \n3. Add ice cubes.  \n4. Blend on high until the mixture is creamy and smooth.  \n5. Pour into a glass and enjoy immediately.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message'), type='message_output_item')]
'''

'''Exercise 3'''

import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # TODO: Print the full conversation history as a list of messages using to_input_list()
    print(result.to_input_list())

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 3 - Output '''
'''
[{'content': 'Give me a recipe for a healthy smoothie.', 'role': 'user'}, {'id': 'msg_688c32722728819890b32679760759a406a40b77d9a57a91', 'content': [{'annotations': [], 'text': '**Green Glow Healthy Smoothie**\n\n**Ingredients:**\n- 1 cup fresh spinach leaves, packed\n- 1 small ripe banana\n- 1/2 cup frozen mango chunks\n- 1/2 cup frozen pineapple chunks\n- 1/2 cup plain Greek yogurt\n- 1 tablespoon chia seeds\n- 1 cup unsweetened almond milk\n- 1/2 tablespoon fresh lemon juice\n- 1/2 teaspoon grated fresh ginger (optional)\n\n**Instructions:**\n1. Add spinach, banana, mango, pineapple, Greek yogurt, chia seeds, almond milk, lemon juice, and ginger to a blender.\n2. Blend on high until smooth and creamy, scraping down the sides as needed.\n3. Taste and adjust thickness by adding more almond milk if needed.\n4. Pour into a glass and serve immediately.', 'type': 'output_text', 'logprobs': []}], 'role': 'assistant', 'status': 'completed', 'type': 'message'}]
'''

''' Exercise 4 Instructions
You’ve just learned how to use the to_input_list() method to capture the full conversation context from an agent’s run. Now, let’s take things a step further by chaining two agents together and passing context between them.

Your task is to connect the Recipe Chef agent and the Blog Writer agent so that the second agent can use the recipe created by the first. Here’s what you need to do:

    Take the result from the Recipe Chef agent and use to_input_list() to get the conversation history.
    Add a new user message asking for a blog post about the recipe.
    Run the Blog Writer agent with this combined input.
    Print the final blog post output from the Blog Writer agent.

This exercise will help you practice passing context between agents and building more advanced workflows.
'''
import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)

# Define a Blog Writer agent
blog_agent = Agent(
    name="Blog Writer",
    instructions=(
        "You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post "
        "that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    recipe_result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # TODO: Get the conversation context from the Recipe Chef agent using to_input_list()
    

    # TODO: Add a new user message asking for a blog post about the recipe

    # TODO: Run the Blog Writer agent with the combined input

    # TODO: Print the final blog post output from the Blog Writer agent

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 4 
You’ve just learned how to use the to_input_list() method to capture the full conversation context from an agent’s run. Now, let’s take things a step further by chaining two agents together and passing context between them.

Your task is to connect the Recipe Chef agent and the Blog Writer agent so that the second agent can use the recipe created by the first. Here’s what you need to do:

    Take the result from the Recipe Chef agent and use to_input_list() to get the conversation history.
    Add a new user message asking for a blog post about the recipe.
    Run the Blog Writer agent with this combined input.
    Print the final blog post output from the Blog Writer agent.

This exercise will help you practice passing context between agents and building more advanced workflows.
'''
import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)

# Define a Blog Writer agent
blog_agent = Agent(
    name="Blog Writer",
    instructions=(
        "You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post "
        "that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    recipe_result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # TODO: Get the conversation context from the Recipe Chef agent using to_input_list()
    convo_context = recipe_result.to_input_list()

    # TODO: Add a new user message asking for a blog post about the recipe
    convo_context += [{"role": "user", "content": "Write a blog post about the recipe."}]
    
    #convo_context = recipe_result.to_input_list()
    
    # TODO: Run the Blog Writer agent with the combined input
    result = await Runner.run(
            starting_agent=blog_agent,
            input=convo_context 
        )
    # TODO: Print the final blog post output from the Blog Writer agent
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

'''
Exercise 4 - Output

**A Sip of Sunshine: My Favorite Tropical Green Power Smoothie**

With busy mornings and jam-packed days, nourishing our bodies sometimes slips to the bottom of the to-do list. That’s why I love finding simple, delicious, and nutrient-packed recipes to power me through—starting with breakfast! Today, I’m sharing my go-to morning boost: the Tropical Green Power Smoothie. This vibrant drink tastes like a mini vacation and gives you the energy and nutrients you need to tackle any day.

**Why I Love This Smoothie**

What makes this smoothie so special is its refreshing fusion of fruits with the added bonus of greens and superfoods. The frozen mango and pineapple deliver a juicy, naturally sweet flavor reminiscent of the tropics, while the banana adds just the right amount of creamy texture. Spinach sneaks in a serving of leafy greens without overpowering the taste, and chia seeds bring a welcome punch of fiber and healthy fats. A dollop of Greek yogurt gives it a protein boost, and a splash of lime juice ties all the flavors together with a zesty finish.

**The Recipe: Tropical Green Power Smoothie**

Here’s how you can make this energizing, feel-good smoothie in just minutes:

*Ingredients:*
- 1 cup fresh spinach leaves
- 1/2 cup frozen mango chunks
- 1/2 cup frozen pineapple chunks
- 1 small ripe banana
- 1 tablespoon chia seeds
- 1/2 cup unsweetened Greek yogurt
- 1 cup unsweetened almond milk
- 1 teaspoon fresh lime juice

*Instructions:*
1. Layer the spinach, frozen mango, frozen pineapple, and banana into your blender.
2. Sprinkle the chia seeds over the fruit.
3. Add the Greek yogurt for creaminess and protein.
4. Pour in the almond milk, and squeeze in the lime juice for a bright, tangy kick.
5. Blend on high until smooth and creamy, pausing to scrape down the sides if necessary.
6. Adjust to your preferred consistency by adding a little more almond milk, then pour into your favorite glass.
7. Sip, close your eyes, and savor that burst of tropical sunshine!

**The Nourishing Benefits**

Packed with vitamins, minerals, protein, and healthy fats, this smoothie truly delivers on health. Spinach provides a blast of iron and antioxidants, while chia seeds offer omega-3s and fiber to keep you feeling full. The fruit delivers immune-boosting vitamin C, and the Greek yogurt helps keep your energy levels steady. It’s the perfect way to start your day or recharge after a workout.

**Conclusion**

Whether you’re reaching for something quick and healthy in the morning or want a post-exercise pick-me-up, this Tropical Green Power Smoothie will leave you feeling refreshed, satisfied, and ready to face the day. The best part? It’s endlessly customizable—add a scoop of protein powder, swap in kale for spinach, or toss in your favorite seeds or nut butters. Give it a try and let a little sunshine into your routine!

Here’s to vibrant mornings and nourishing sips!
'''

''' Exercise 5

You’ve just practiced chaining two agents together and printing the final blog post output. Now, let’s take a closer look at how you can track which agent produced the final result in a multi-step workflow.

After running both the Recipe Chef and Blog Writer agents, your task is to print the last_agent property from the result of the Blog Writer agent. This will show you exactly which agent created the final output, which is helpful for understanding and debugging agent chains.

This step will help you see how to keep track of agent activity in more complex workflows.
'''

import asyncio
from agents import Agent, Runner

# Define a Recipe Chef agent
recipe_agent = Agent(
    name="Recipe Chef",
    instructions=(
        "You are a creative chef. Provide a detailed healthy smoothie recipe with a title, a list of ingredients, "
        "and step-by-step instructions. Do not include extra commentary. Output only the recipe text."
    ),
    model="gpt-4.1"
)

# Define a Blog Writer agent
blog_agent = Agent(
    name="Blog Writer",
    instructions=(
        "You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post "
        "that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text."
    ),
    model="gpt-4.1"
)


async def main():
    # Run the Recipe Chef agent
    recipe_result = await Runner.run(
        starting_agent=recipe_agent,
        input="Give me a recipe for a healthy smoothie."
    )

    # Get the conversation context from the Recipe Chef agent
    context = recipe_result.to_input_list()

    # Add a new user message asking for a blog post about the recipe
    combined_input = context + [{"role": "user", "content": "Write a blog post about the recipe."}]

    # Run the Blog Writer agent with the combined input
    blog_result = await Runner.run(
        starting_agent=blog_agent,
        input=combined_input
    )

    # Print the final blog post output from the Blog Writer agent
    print("Final Blog Post Output:")
    print(blog_result.final_output)

    # TODO: Print which agent produced the final output (use blog_result.last_agent)
    print(blog_result.last_agent)

if __name__ == "__main__":
    asyncio.run(main())

''' Exercise 5 Output

Final Blog Post Output:
**Glowing from the Inside Out: The Green Glow Power Smoothie**

There’s something magical about starting your day with a vibrant, nutrient-packed smoothie. Mornings can easily slip into a haze of coffee and rushed routines, but blending up a fresh smoothie not only fuels your body—it sets a positive intention for your whole day. If you’re looking to add more leafy greens and nourishing ingredients to your life, my Green Glow Power Smoothie is the perfect place to start!

**Why I Love This Smoothie**

This recipe brings together everything I love about breakfast: simplicity, flavor, and a serious health boost. It’s beautifully green, delightfully creamy, and naturally sweet, thanks to frozen mango, pineapple, and banana. Each ingredient was thoughtfully chosen—not just for taste, but for its unique superfood benefits.

Spinach is rich in iron, vitamin C, and fiber, making it a powerhouse for skin and energy. Mango and pineapple infuse your glass with antioxidants, tropical flavor, and just the right amount of sweetness. The banana provides creaminess and potassium, while chia seeds lend fiber and omega-3s to keep you full. Almond butter adds healthy fats and a subtle, nutty note. Finally, fresh lime juice brings brightness and boosts the immune system—everything you want in a single glass.

**How to Make the Green Glow Power Smoothie**

Let’s get blending! Here’s what you’ll need:

- 1 cup fresh spinach leaves, packed
- 1/2 cup frozen mango chunks
- 1/2 cup frozen pineapple chunks
- 1 small banana, peeled
- 1 tablespoon chia seeds
- 1 tablespoon almond butter
- 1 cup unsweetened almond milk
- 1/2 cup cold water
- Juice of 1/2 lime

To make your Green Glow Power Smoothie, simply add the spinach, frozen mango, frozen pineapple, and banana to your blender. Sprinkle in the chia seeds and almond butter, then pour over the almond milk, cold water, and the juice of half a lime. Blend on high for 1-2 minutes, or until silky smooth. Pour into your favorite glass, top with extra chia seeds if you’re feeling fancy, and enjoy immediately!

**A Daily Ritual for Wellness**

Whether you need a quick breakfast, a post-workout snack, or a midday energy lift, this smoothie delivers. It’s effortless, endlessly customizable, and it truly does make you feel radiant—inside and out. I invite you to try it for yourself and notice the difference in your day. Take a moment for you, savor each sip, and let your glow begin.

Cheers to health, happiness, and a little more green in every morning!
Agent(name='Blog Writer', instructions='You are an engaging blog writer. Given the recipe text for a healthy smoothie, write an inspiring blog post that includes an introduction, a detailed description of the recipe, and a conclusion. Output only the blog post text.', handoff_description=None, handoffs=[], model='gpt-4.1', model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=None, truncation=None, max_tokens=None, reasoning=None, metadata=None, store=None, include_usage=None, extra_query=None, extra_body=None, extra_headers=None), tools=[], mcp_servers=[], mcp_config={}, input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True)
'''