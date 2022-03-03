"""This test the homepage"""


def test_request_index(client):
    """This checks the About option on navbar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_about(client):
    """This checks the Home option on navbar"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Home" in response.data


