import jwt
import datetime

SECRET_KEY = "assemai"

def generate_token(user_id, business, role, exp_minutes=60):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes)
    token = jwt.encode({"user": user_id, "business": business,"role":role, "exp": expiration_time}, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return "Token has expired."
    except jwt.InvalidTokenError:
        return "Invalid token."

