from flask import request, jsonify
from models import books, members
from utils import generate_id, authenticate, paginate

def setup_routes(app):
    # Routes for books
    @app.route("/books", methods=["GET"])
    def get_books():
        search = request.args.get("search", "")
        filtered_books = [book for book in books if search.lower() in book["title"].lower() or search.lower() in book["author"].lower()]
        return jsonify(paginate(filtered_books, request)), 200

    @app.route("/books", methods=["POST"])
    @authenticate
    def create_book():
        data = request.json
        data["id"] = generate_id(books)
        books.append(data)
        return jsonify({"message": "Book added successfully", "book": data}), 201

    @app.route("/books/<int:book_id>", methods=["PUT"])
    @authenticate
    def update_book(book_id):
        data = request.json
        for book in books:
            if book["id"] == book_id:
                book.update(data)
                return jsonify({"message": "Book updated successfully", "book": book}), 200
        return jsonify({"error": "Book not found"}), 404

    @app.route("/books/<int:book_id>", methods=["DELETE"])
    @authenticate
    def delete_book(book_id):
        global books
        books = [book for book in books if book["id"] != book_id]
        return jsonify({"message": "Book deleted successfully"}), 200

    # Routes for members
    @app.route("/members", methods=["GET"])
    def get_members():
        return jsonify(paginate(members, request)), 200

    @app.route("/members", methods=["POST"])
    @authenticate
    def create_member():
        data = request.json
        data["id"] = generate_id(members)
        members.append(data)
        return jsonify({"message": "Member added successfully", "member": data}), 201

    @app.route("/members/<int:member_id>", methods=["PUT"])
    @authenticate
    def update_member(member_id):
        data = request.json
        for member in members:
            if member["id"] == member_id:
                member.update(data)
                return jsonify({"message": "Member updated successfully", "member": member}), 200
        return jsonify({"error": "Member not found"}), 404

    @app.route("/members/<int:member_id>", methods=["DELETE"])
    @authenticate
    def delete_member(member_id):
        global members
        members = [member for member in members if member["id"] != member_id]
        return jsonify({"message": "Member deleted successfully"}), 200
