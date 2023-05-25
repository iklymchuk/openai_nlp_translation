from sqlalchemy import create_engine
from sqlalchemy import text

def dataframe_to_database(df, table_name):
    "Convert a pandas dataframe to a database"
    engine = create_engine(f"sqlite:///:memory:", echo=False)
    df.to_sql(name=table_name, con=engine, index=False)
    return engine

def handle_response(response):
    "Handle the response from OpenAI"
    query = response["choices"][0]["text"]
    if query.startswith(" "):
        query = "Select" + query
    return query

def execute_query(engine, query):
    "Execute a query on a database"
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()