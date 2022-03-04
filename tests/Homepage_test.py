"""This test the homepage"""


def test_request_main_menu_links(client):
    """This checks the navbar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li class="nav-item"><a href="#" class="nav-link active" aria-current="page">Home</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/git">Git</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/docker">Docker</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/python">Python/Flask</a></li>' in response.data
    assert b'<li class="nav-item"><a class="nav-link" href="/cicd">CI/CD</a></li>' in response.data

def test_request_carousel(client):
    """This checks the Carousel Images and Text"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" ' \
           b'class="active" aria-current="true" aria-label="Slide 1"></button>' in response.data
    assert b'<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" ' \
           b'aria-label="Slide 2"></button>' in response.data
    assert b'<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" ' \
           b'aria-label="Slide 3"></button>' in response.data
    assert b'<button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="3" ' \
           b'aria-label="Slide 3"></button>' in response.data


