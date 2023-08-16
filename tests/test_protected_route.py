import httpx

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/protected-route", headers={"Authorization": f"Bearer {token}"})

    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
