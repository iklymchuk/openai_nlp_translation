## Example how to transform natural language to SQL queries with OpenAI.

Dataset: https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

Flow: `csv dataset -> sqlalchemy db -> sending NLP request to OpenAI -> receiving the SQL query -> processing such SQL query`

Env variable: `OPENAI_API_KEY`

Test:

<img width="1148" alt="Screenshot 2023-05-29 at 11 39 59" src="https://github.com/iklymchuk/openai_nlp_translation/assets/5702058/6154f0d0-9751-4f07-9003-caf5fcfa33c4">
