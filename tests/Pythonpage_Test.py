"""This test the Python/Flask Page"""


def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="#" class="nav-link" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/python">Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data

def test_request_Simple_Pages_Text(client):
    """This checks the content of Simple Pages"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<h3>Simple Pages</h3>' in response.data
    assert b'<strong>index.html</strong>' \
           b'<strong>git.html</strong>' \
           b'<strong>docker.html</strong>' \
           b'<strong>python.html</strong>' \
           b'<strong>cicd.html</strong>' in response.data

