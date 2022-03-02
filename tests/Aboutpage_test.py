"""This test the About page"""

def test_request_about(client):
    """This checks the title of the web page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>Rahul's F-Layou Page</title>" in response.data

def test_request_to_do_list(client):
    """This checks for the to do list"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b'<strong class="mb-1">To-Do List 1</strong>' in response.data
    assert b'<strong class="mb-1">To-Do List 2</strong>' in response.data
    assert b'<strong class="mb-1">To-Do List 3</strong>' in response.data
    assert b'<strong class="mb-1">To-Do List 4</strong>' in response.data