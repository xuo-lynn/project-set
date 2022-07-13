import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Set&#39;s Portfolio</title>" in html

        #TODO Add more tests relating to the home page
        assert '<nav class = "navbar">' in html
        assert '<a href="#about" class="nav-link">' in html
        assert '<a href="#experience" class="nav-link">' in html
        assert '<a href="#education" class="nav-link">' in html
        assert '<a href="#hobbies" class="nav-link">' in html
        assert '<a href="/timeline" class="nav-link">' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        # print( json['timeline_posts'] )
        assert len(json["timeline_posts"]) == 0

        #TODO Add more tests relating to the /api/timeline_post GET and POST apis
        response = self.client.post("/api/timeline_post", data={"name": "Bob", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 200

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        json = response.get_json()
        assert len(json["timeline_posts"]) == 1

        #TODO Add more tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h1>Message Board</h1>" in html
        assert '<form id= "form">' in html
        assert '<input name="name" placeholder="Enter your name">' in html
        assert '<input name="email" placeholder="Enter your email">' in html
        assert '<input name="content" placeholder="Enter your message">' in html
        assert '<button type="Submit">Submit</button>' in html
        assert '</form>' in html

    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe","email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html

if __name__ == '__main__':
    unittest.main()
