user = {
    "user_name": "my_user",
    "password": "test@123",
    "email":"my_user@example.com",
    "address":"ABC Road, 111111",
    "country": "Belgium"
}

sensitive_info= ["password", "address", "phone"]

for i in sensitive_info:
    if i in user:
        print(f"DELETED => Key:{i}, Value:{user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")

print(user)