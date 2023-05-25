import openai 

def create_table_definition_prompt(df, table_name):
    "Create a prompt for the OpenAI API to generate SQL queries"
    prompt = '''### sqlite table, with its properties:
    #
    # {}({})
    #
    '''.format(table_name, ",".join(str(x) for x in df.columns))
    return prompt

def user_query_input():
    "Ask the user what data they need to show"
    user_input = input("Tell OpenAI what data you need to show: ")
    return user_input

def combine_prompts(fixed_sql_prompt, user_query):
    "Combine the fixed SQL prompt with the user query"
    final_user_input = f"### A query to answer: {user_query}\nSELECT"
    return fixed_sql_prompt + final_user_input

def send_to_openai(prompt):
    "Send the prompt to OpenAI"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["#", ";"]
    )
    return response
    