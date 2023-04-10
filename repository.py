DATABASE = {
    "animals": [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 1,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        }
    ],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        }
    ]
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(resources, id):
    """For GET requests to a single resource"""
    requested_resource = None

    for resource in DATABASE[resources]:
        if resource["id"] == id:
            requested_resource = resource

    return requested_resource


def create(resource, new_resource):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]

    new_id = max_id + 1

    new_resource["id"] = new_id

    DATABASE[resource].append(new_resource)

    return new_resource


def update(resources, id, new_resource):
    """For PUT requests to a single resource"""
    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            DATABASE[resources][index] = new_resource
            break


def delete(resources, id):
    """For DELETE requests to a single resource"""
    resource_index = -1

    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            resource_index = index

    if resource_index >= 0:
        DATABASE[resources].pop(resource_index)
