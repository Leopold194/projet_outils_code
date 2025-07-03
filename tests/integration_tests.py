import requests
import uuid


def test00():
    data = {
        "email": "admin@test.com",
        "password": "password"
    }



    response = requests.post("http://localhost:3001/api/auth/login", json=data)
    assert response.status_code == 200
    
    data_0 = {
        "email": "admin@test.com",
        "password": "pass"
    }



    response = requests.post("http://localhost:3001/api/auth/login", json=data_0)
    assert response.status_code == 400
    
    


    
    

  
def test01():
    data = {
        "email": f"{uuid.uuid4()}@mail.com",
        "password": "pass1234",
        "name": "Test User"
    }

    response = requests.post("http://localhost:3001/api/auth/register", json=data)
    print(response.text)
    assert response.status_code == 201
    
    data = {
        "email": "admin@test.com",
        "password": "password",
        "name": "Test User"
    }

    response = requests.post("http://localhost:3001/api/auth/register", json=data)
    print(response.text)
    assert response.status_code == 400
    


def test02():
    data = {
        "email": "admin@test.com",
        "password": "password"
    }

    response = requests.post("http://localhost:3001/api/auth/login", json=data)
    token = response.json().get("token")
    
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get("http://localhost:3001/api/tasks", headers=headers)
    assert response.status_code == 200
    
    response = requests.get("http://localhost:3001/api/tasks/1", headers=headers)
    assert response.status_code == 200
    
    response = requests.get("http://localhost:3001/api/tasks/12794879", headers=headers)
    assert response.status_code == 404
    

def test03():
    data = {
        "email": "admin@test.com",
        "password": "password"
    }
    
    response = requests.post("http://localhost:3001/api/auth/login", json=data)
    token = response.json().get("token")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    task_data = {
        "title": "Nettoyer le code",
        "description": "À faire cette semaine",
        "priority": "medium"
    }
    
    res = requests.post("http://localhost:3001/api/tasks", headers=headers, json=task_data)
    
    assert res.status_code == 201
    
def test04():
    data = {
        "email": "admin@test.com",
        "password": "password"
    }
    
    response = requests.post("http://localhost:3001/api/auth/login", json=data)
    token = response.json().get("token")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    task_data = {
        "title": "Tâche modifiée",
        "description": "À faire cette Samedi",
    }
    
    res = requests.put("http://localhost:3001/api/tasks/1", headers=headers, json=task_data)

    assert res.status_code == 200
    
    res = requests.put("http://localhost:3001/api/tasks/1234567809876", headers=headers, json=task_data)

    assert res.status_code == 404
    
def test05():
    data = {
        "email": "admin@test.com",
        "password": "password"
    }
    
    response = requests.post("http://localhost:3001/api/auth/login", json=data)
    token = response.json().get("token")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.delete("http://localhost:3001/api/tasks/2", headers=headers)
    assert response.status_code == 204
    
    response = requests.delete("http://localhost:3001/api/tasks/1234567890", headers=headers)
    assert response.status_code == 404
    
    
    
def test06():
    res = requests.get("http://localhost:3001/api/users")
    print("Status /api/users sans token :", res.status_code)
    assert res.status_code == 401


def test07():
    res = requests.get("http://localhost:3001/health")
    print("Status /health :", res.status_code)
    print("Réponse :", res.json())

    assert res.status_code == 200
    assert res.json().get("status") == "OK"
    
def test08():
    res = requests.get("http://localhost:3001/route-qui-n-existe-pas")
    print("Status route inconnue :", res.status_code)
    print("Réponse :", res.text)

    assert res.status_code == 404
    assert "Route non trouvée" in res.text

