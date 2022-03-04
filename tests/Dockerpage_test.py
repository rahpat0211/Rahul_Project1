"""This test the Docker Page"""


def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link active" href="/docker">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data

def test_request_Steps(client):
    """This checks to see if the steps are correct"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<h10>Step 1:<p>Open terminal and type in this command:<br><strong>' \
           b'docker pull rup1141/patel-r-project1:master</strong></p></h10>' in response.data
    assert b'<h10>Step 2:<p>Change directory to where this file is located.<br><strong>' \
           b'cd Rahul_Project1</strong></p></h10>' in response.data
    assert b'<h10>Step 3:<p>Once on the right path, type in this command:<br><strong>' \
           b'docker compose up --build</strong></p></h10>' in response.data
    assert b'<h10>Step 4:<p>Finally, open up your browser and type in:<br><strong>' \
           b'localhost</strong></p></h10>' in response.data

def test_request_Table(client):
    """This checks to see if the Table consists of 2 Columns"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<th>Command</th>' in response.data
    assert b'<th>Explanation</th>' in response.data


