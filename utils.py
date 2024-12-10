from flask import request, jsonify

# Generate unique IDs
def generate_id(data):
    return max([item["id"] for item in data], default=0) + 1

# Pagination utility
def paginate(data, request):
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))
    start = (page - 1) * per_page
    end = start + per_page
    return {"data": data[start:end], "total": len(data)}

# Dummy authentication decorator
def authenticate(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token == "Bearer valid_token":
            return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    return wrapper
