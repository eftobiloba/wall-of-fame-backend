def each_user_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "bio": user["bio"],
        "username": user["username"],
        "email": user["email"],
        "name": user["name"],
        "password": user["password"] 
    }

def list_users_serial(users) -> list:
    return [each_user_serial(user) for user in users]


def each_image_serial(image) -> dict:
    return {
        "id": str(image["_id"]),
        "user_id": image["user_id"],
        "tags": image["tags"],
        "url": image["url"],
        "order": image["order"],
    }

def list_images_serial(images) -> list:
    return [each_image_serial(image) for image in images]