import jwt, os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, authenticate
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv("SECRET")
User = get_user_model()

@api_view(["POST"])
def register(request):
    data = request.data

    if User.objects.filter(username=data["username"]).exists():
        return Response({"error": "Username already exists"}, status=400)
    
    user = User.objects.create(
        username = data["username"],
        email = data["email"],
        password = make_password(data["password"])
    )

    return Response({"message": "User regostered", "user_id": user.id})

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Invalid username or password"}, status=401)

    # token payload
    payload = {
        "id": user.id,
        "username": user.username
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return Response({
        "message": "Login successful",
        "token": token
    })

@api_view(["GET"])
def profile(request):
    return Response({
        "id": request.headers.get("X-User-Id"),
        "username": request.headers.get("X-User-Name")
    })