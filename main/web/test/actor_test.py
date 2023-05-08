def test_find(client):
    # First, create a test actor to search for
    # actor = Actor(name="Test Actor", age=30, gender="Male")
    # db.session.add(actor)
    # db.session.commit()

    # Test searching by ID
    response = client.get(f"/actor/1")
    assert response.status_code == 200
    # assert response.json == {"id": actor.id, "name": "Test Actor", "age": 30, "gender": "Male"}
    #
    # # Test searching by name
    # response = client.get("/actor_api/Test Actor/name")
    # assert response.status_code == 200
    # assert response.json == {"id": actor.id, "name": "Test Actor", "age": 30, "gender": "Male"}
    #
    # # Test searching by age
    # response = client.get("/actor_api/30/age")
    # assert response.status_code == 200
    # assert response.json == [{"id": actor.id, "name": "Test Actor", "age": 30, "gender": "Male"}]
    #
    # # Test searching by gender
    # response = client.get("/actor_api/Male/gender")
    # assert response.status_code == 200
    # assert response.json == [{"id": actor.id, "name": "Test Actor", "age": 30, "gender": "Male"}]
