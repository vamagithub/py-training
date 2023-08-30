from app import app

def test_home():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b'Welcome' in response.data

def test_home_post_405():
    with app.test_client() as client:
        response = client.post("/")
        assert response.status_code == 405

def test_insert_post():
    with app.test_client() as client:
        response = client.post("/insert", data={
            "name": "Test Name",
            "age": 200,
            "physics": 80,
            "maths": 50,
            "english": 100,
        })
        assert response.status_code == 200
        assert b"Test Name" in response.data
