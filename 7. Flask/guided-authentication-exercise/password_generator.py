import hashlib

password = "javiersolisprieto"
hashed_password = hashlib.md5(password.encode()).hexdigest()

print(hashed_password)  # 9c87baa223f464954940f859bcf2e233, por ejemplo


# {
#     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidHlwZSI6ImFjY2VzcyIsImV4cCI6MTc5MjEwNTgwMn0.mE3fgq1Az7ebgu1-dLlffKBLd05km1Lg0Ax54V1Yb-A",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidHlwZSI6InJlZnJlc2giLCJleHAiOjE3OTI3MDk3MDJ9.LWjNWfB_HUSUkYcJldAP-dnzJuJED8LxVPQyYDeUQ2c"
# }