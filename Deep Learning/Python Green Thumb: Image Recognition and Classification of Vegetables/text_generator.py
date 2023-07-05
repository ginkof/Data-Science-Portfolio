import openai
import re

# getting story/facts from chatgpt
openai.api_key = st.secrets['my_key']

def get_fact(ingredient,mode):
    response_fact = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"In about 250 characters, tell me a specific {mode} fact about the vegetable {ingredient}. Make sure you end the fact with the last character.",
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #extraction
    facts = response_fact['choices'][0]['text']
    split_facts = facts.split("\n")
    return [re.sub("\d. ", "", fact)for fact in split_facts][2:][0]

# 4 facts for kids

def get_4fact_kids(ingredient):
    four_facts = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Tell me 4 facts, distinct from each other, in a form of a bulletted list about the vegetable {ingredient} as if I were a kid. Every fact needs to be about 250 characters and sould start with the character '-'. Make sure you end the fact with the last character.",
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    facts = four_facts['choices'][0]['text']
    split_facts = facts.split("\n")
    return [re.sub("-", "", fact)for fact in split_facts][2:]


# 1 fact for kids

def get_fact_kids(ingredient):
    response_fact = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Suppose I'm a kid, max 10 years old. In about 250 characters, tell me a specific fact about the vegetable {ingredient}. Make sure you end the fact with the last character.",
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #extraction
    facts = response_fact['choices'][0]['text']
    split_facts = facts.split("\n")
    return [re.sub("\d. ", "", fact)for fact in split_facts][2:][0]



# Recipe

def get_recipe(ingredient):
    response_recipe = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"In about 600 characters, write a recipe with {ingredient} as main ingredient. Write in the form of a text without lists. The first line has to be the title and should be separated by the body of the recipe by '\n\n'",
        temperature=1,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response_recipe['choices'][0]['text']
    text_split = text.split('\n\n')[1:]
    return text_split


# Story

def get_story(ingredient):
    response_fact = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"In about 600 characters tell a fayritale for kids with {ingredient} as main character.",
        temperature=1,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #extraction
    facts = response_fact['choices'][0]['text']
    split_facts = facts.split("\n")
    return [re.sub("\d. ", "", fact)for fact in split_facts][2:][0]
