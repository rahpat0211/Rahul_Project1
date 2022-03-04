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


"""This test the Python/Flask Page"""


def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-link" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data

def test_request_Simple_Pages_Text(client):
    """This checks the content of Simple Pages"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<h3>Simple Pages</h3>' in response.data
    assert b'<strong>index.html</strong>' in response.data

