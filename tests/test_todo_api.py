import base64


def test_register(client, request):
    response = client.post(
        "/auth/register",
        json={
            "username": request.config.cache.get("username", None),
            "password": request.config.cache.get("password", None),
        },
    )
    assert 201 == response.status_code

    cred = f"{request.config.cache.get('username', None)}:{request.config.cache.get('password', None)}"
    valid_credentials = base64.b64encode(bytes(cred, encoding="utf-8")).decode("utf-8")
    request.config.cache.set("cred", valid_credentials)


def test_create_task_list(client, request):
    response = client.post(
        "/task-lists/",
        json={"title": "test-task-list"},
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 201 == response.status_code
    request.config.cache.set("task_list_id", response.json["data"]["id"])


def test_get_task_list(client, request):
    response = client.get(
        "/task-lists/",
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert response.status_code == 200
    assert len(response.json["data"]) > 0


def test_update_task_list(client, request):
    updated_task_title = "test-task-list-2"
    response = client.put(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}",
        json={"title": updated_task_title},
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 200 == response.status_code
    assert updated_task_title == response.json["data"]["title"]


def test_create_task(client, request):
    response = client.post(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}/tasks",
        json={"description": "test-task"},
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 201 == response.status_code
    request.config.cache.set("task_id", response.json["data"]["id"])


def test_get_task(client, request):
    response = client.get(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}/tasks",
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert response.status_code == 200
    assert len(response.json["data"]) > 0


def test_update_task(client, request):
    updated_task_title = "test-task-2"
    response = client.put(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}/tasks/{request.config.cache.get('task_id', None)}",
        json={"description": updated_task_title, "is_finished": True},
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 200 == response.status_code
    assert updated_task_title == response.json["data"]["description"]
    assert response.json["data"]["finished_at"] is not None


def test_delete_task(client, request):
    response = client.delete(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}/tasks/{request.config.cache.get('task_id', None)}",
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 204 == response.status_code


def test_delete_task_list(client, request):
    response = client.delete(
        f"/task-lists/{request.config.cache.get('task_list_id', None)}",
        headers={"Authorization": "Basic " + request.config.cache.get("cred", None)},
    )

    assert 204 == response.status_code
