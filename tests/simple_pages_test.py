"""This test the Git Page"""

def test_request_Git_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/git")
    assert response.status_code == 200

    assert b'<li class="nav-item"><a href="/" class="nav-' \
    b'link" aria-current="page">Home</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-link ' \
     b'active" href="/git">Git</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/docker">Docker</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/python">Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/glos">Glossary</a></li>' in response.data



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
           b'width=1198&trim=1,1&bg-color=000&pad=1,1" class="d-block '\
            b'w-100" alt="...">' in response.data


#This test the Docker Page

def test_request_Docker_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-' \
    b'link" aria-current="page">Home</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/git">Git</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link active" href="/docker">Docker</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/python">Python/Flask</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/glos">Glossary</a></li>' in response.data

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


#This test the Python/Flask Page


def test_request_Python_Flask_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="/" class="nav-' \
    b'link" aria-current="page">Home</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/docker">Docker</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-' \
    b'link active" href="/python">Python/Flask</a></li>' in response.data

    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/aaa">AAA</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/oops">OOPS</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/solid">SOLID</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-' \
    b'link" href="/glos">Glossary</a></li>' in response.data

def test_request_Simple_Pages_Text(client):
    """This checks the content of Simple Pages"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<h3>Simple Pages</h3>' in response.data
    assert b'<strong>index.html</strong>' in response.data
    assert b'<strong>git.html</strong>' in response.data
    assert b'<strong>docker.html</strong>' in response.data
    assert b'<strong>python.html</strong>' in response.data
    assert b'<strong>cicd.html</strong>' in response.data

def test_request_Python_Img_Link(client):
    """This checks if the image is correct and the link is valid"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b'<a href="https://github.com/rahpat0211/Rahul_Project1">' in response.data
    assert b'<img src="https://www.python.org/static/community_logos/' \
           b'python-logo-master-v3-TM-flattened.png" class="d-' \
           b'block w-100" alt="...">' in response.data


#This test the CI/CD Page


def test_request_CICD_Heading(client):
    """This checks the headings of each content"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b'<h3>How to review code using <strong>Development Server</strong></h3>' in response.data
    assert b'<h3>How to deploy master to production server</h3>' in response.data
    assert b'<h3>How to deploy image of your project ' \
    b'to Docker Hub, when master is updated</h3>' in response.data

def test_request_CICD_Colors(client):
    """This checks the font color of 2 tags"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b'<font color="red">(Red is the original code)</font>' in response.data
    assert b'<font color="green">(Green is your edited code)</font>' in response.data
