
    # Exponential Backoff Utilities
    import asyncio
    import time
    
    async def backoff_request(url, method='GET', headers=None, payload=None):
        delay = 2
        for attempt in range(5):
            try:
                async with httpx.AsyncClient() as c:
                    if method == 'GET':
                        resp = await c.get(url, headers=headers)
                    elif method == 'POST':
                        resp = await c.post(url, headers=headers, json=payload)
                    return resp
            except Exception as e:
                if attempt < 4:
                    await asyncio.sleep(delay)
                    delay *= 2
                else:
                    raise
        return None
    