from fastapi import FastAPI
from model import call_llm

app=FastAPI()

#NL2SQL
@app.post("/sql")

def convert_sql(qsn: str):

    prompt = f"""
Convert the following natural language query to SQL.
Return only SQL.

{qsn}
"""

    sql_query = call_llm(prompt)

    return {
        "sql_query": sql_query
    }
@app.post("/NL")

def NL_analysis(msg: str,time: int):
        word_count =  len(msg.split())
        wpm = 0 if time == 0 else (word_count/(time/60))
        
        prompt = f"""
Analyze the following user message in the input

Message:
{msg}
Time:
{time}


Return ONLY JSON in this format:

{{
  "sentiment": "",
  "confidence": 0-100,
  "WPM": {wpm},
  "empathy_score": 0-100,
  "reason": ""
}}


{msg}
"""
        res = call_llm(prompt)
        return {"response":res}
