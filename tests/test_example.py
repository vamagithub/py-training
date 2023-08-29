from app import app


def test_sanity():
    assert 1 == 1

def test_example():
    with app.test_client() as client:
        response = client.get("/")

        print(response)

        # assert response.status_code == 200
