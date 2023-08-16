from http import client
from app.main import app

def test_login_and_access_protected_route():
    login_data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get("/protected-route", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "This is a protected route"}

    response = client.get("/protected-route")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

