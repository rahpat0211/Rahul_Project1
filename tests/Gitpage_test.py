"""This test the Git Page"""


def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data

def test_request_h3(client):
    """This checks the page for the h3 values"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'<h3>Branches</h3>' in response.data
    assert b'<h3>Merge</h3>' in response.data
    assert b'<h3>Commit</h3>' in response.data
    assert b'<h3>Tag</h3>' in response.data
    assert b'<h3>Repository</h3>' in response.data

def test_request_img(client):
    """This checks the page for the github image"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b'<img src="https://www.cloudsavvyit.com/p/uploads/2019/10/e713ed70-1.png?' \
           b'width=1198&trim=1,1&bg-color=000&pad=1,1" class="d-block w-100" alt="...">' in response.data


