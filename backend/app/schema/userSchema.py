User_Schema = {
    '$jsonSchema': {
        "bsonType": "object",
        "required": ["first_name", "last_name", "email", "country", "phone_number", "password"],
        "properties": {
            "first_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "email": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "country": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "phone_number": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "password": {
                "bsonType": "string",
                "description": "must be a string and is required"
            }
        }
    }
}