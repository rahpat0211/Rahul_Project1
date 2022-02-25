"""This test the homepage"""

def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/about">About</a></li>' in response.data


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


