from google.oauth2 import service_account
import firebase_admin 
from firebase_admin import auth

default_app = firebase_admin.initialize_app()


# client = auth.get_user_by_email('a77x86@gmail.com')
# print(client.display_name)

# get all users 
users = auth.list_users().users

# verify id token
def verify_id_token():
    try:

        decoded_token = auth.verify_id_token('eyJhbGciOiJSUzI1NiIsImtpZCI6ImE4YmZhNzU2NDk4ZmRjNTZlNmVmODQ4YWY5NTI5ZThiZWZkZDM3NDUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWJkdWxsYWggTW9oYW1tZWQiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FGZFp1Y29Ib0g4ODBFSGkwd1BXbnFXLWl0c3pZLXNrc2thc3lURGJ1MUhEPXM5Ni1jIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3ZlZW11LTMzZTgxIiwiYXVkIjoidmVlbXUtMzNlODEiLCJhdXRoX3RpbWUiOjE2NjExOTIzMjYsInVzZXJfaWQiOiI3Z3c5WGpDZHlsWE5lN2VYb3VsaXR6VmthUnEyIiwic3ViIjoiN2d3OVhqQ2R5bFhOZTdlWG91bGl0elZrYVJxMiIsImlhdCI6MTY2MTE5NjkyNCwiZXhwIjoxNjYxMjAwNTI0LCJlbWFpbCI6ImE3N3g4NkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwNDE4NzI3MjI1NzUwNTMzNzkwOCJdLCJlbWFpbCI6WyJhNzd4ODZAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.lR3FqgqfUr10xFkLLkA8GGXYxZuZ6Y8k4-DzVqAdu8Fa9KKIYSttv_WvxkbHyhtYgoXxJ3s3o9zBUkHdx_HWpQ7jzB1gEmWFyab-p8gnjJt8M5-AzuLbHTCr8tFpCJ7liOIM274GLfkjPnVYPPcGqHJDa3RbVLqxJ714USNFVyELTuex1p-EmhPXJm0H6Nywgby-JAgH-AEmRWfq8Tu75JTYbw0HwYxEpRP8XlB_Frx4a-ZvVegut9B-nQ8s_OabGMMTayAeNdvCDCavcisEWrzxlH0WTcRqQ8LZQDYOeLNK6Uye2E8s-kr2t7CeRPLfd-8D80cEYAJLuHKlpkct_A')
        return decoded_token
    except ValueError as e:
        print(e)
        return None


# get user id from decoded token
def get_user_id_from_decoded_token(decoded_token):
    return decoded_token['uid']


print(get_user_id_from_decoded_token(verify_id_token()))


# for user in users:
#     print(user.uid)
#     print(user.display_name)
#     print(user.email)
#     print(user.phone_number)
#     print(user.photo_url)
#     print(user.email_verified)
#     print(user.disabled)
#     print(user.custom_claims)
#     print(user.provider_data)
#     print(user.password_hash)
#     print(user.provider_id)
#     print(user.tenant_id)
#     print(user.uid)
    