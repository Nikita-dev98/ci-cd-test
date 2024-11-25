from fastapi import FastAPI, HTTPException
import httpx


app = FastAPI()
fact_api_url = "https://api.api-ninjas.com/v1/facts"
api_key = "4hKO5fyQgCirv0Wj7uGbzg==8SOaY0ZmJrLYXTmc"

@app.get("/")
async def get_random_fact():
    headers = {"X-Api-Key": api_key}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(fact_api_url, headers=headers)
            response.raise_for_status()
            fact = response.json()
            
            if fact and isinstance(fact, list):
                return {"fact": fact[0]["fact"]}
        
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code)
    except Exception as e:
        raise HTTPException(status_code=500)