contact_info = {
    "name": "David Smith",
    "street": "123 Main Street",
    "city": "San Leandro",
    "state": "CA",
    "zip": "94577"
}


print(f"""{contact_info['name']}
{contact_info['street']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")


del contact_info["name"]


full_name = {
    "first name": "David",
    "last name": "Smith"
}

full_name.update({"honorific": "Mr."})


contact_info.update({"full_name": full_name})

print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['street']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")