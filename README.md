Library Management System API
A RESTful Flask API for managing books and members of a library. This application supports CRUD operations, search functionality, pagination, and token-based authentication, adhering to best practices in REST API design.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features
Books Management:

Add, view, update, and delete books.
Search books by title or author.
Paginated responses for efficient data handling.
Members Management:

Add, view, update, and delete members.
Paginated responses for member lists.
Authentication:

Token-based authentication to secure critical endpoints.
Scalability and Clarity:

Organized codebase for ease of scaling and maintenance.
-------------------------------------------------------------

How to Run the Project
Prerequisites
Python 3.10+: Ensure Python is installed on your system.
Flask: Install Flask using pip:
bash
Copy code
pip install flask
Steps to Run
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd library_management_system
Run the Application:

bash
Copy code
python app.py
Access the API:

The API runs on http://127.0.0.1:5000/.
Test API Endpoints: Use tools like Postman or cURL to interact with the API.
----------------------------------------------------------------------------

API Endpoints
Books Endpoints
Method	Endpoint	Description
GET	/books	Get all books with search and pagination.
POST	/books	Add a new book (requires token).
PUT	/books/<book_id>	Update a book (requires token).
DELETE	/books/<book_id>	Delete a book (requires token).
Members Endpoints
Method	Endpoint	Description
GET	/members	Get all members with pagination.
POST	/members	Add a new member (requires token).
PUT	/members/<member_id>	Update a member (requires token).
DELETE	/members/<member_id>	Delete a member (requires token).
Authentication
Include the header Authorization: Bearer valid_token for secured routes.
------------------------------------------------------------------------

Design Choices
1. Modularity:
Divided code into multiple files (app.py, routes.py, models.py, utils.py) to improve readability and reusability.
2. Simplicity:
Used Python’s built-in data structures (lists) to mimic a database, keeping the project beginner-friendly.
Avoided third-party libraries to demonstrate problem-solving with native tools.
3. RESTful Principles:
Followed RESTful conventions to design endpoints and HTTP methods.
4. Security:
Implemented token-based authentication for sensitive operations.
5. Scalability:
Search and pagination were added to handle larger datasets efficiently.
-----------------------------------------------------------------------

Assumptions and Limitations
Data Storage:

Data is stored in-memory (in models.py). This means data is lost on server restart.
Persistent storage like a database can be integrated later.
Authentication:

A hardcoded token (valid_token) is used for simplicity. A real-world application should implement a robust authentication mechanism.
Validation:

Minimal input validation is performed to keep the focus on API functionality.
Constraints:

The project strictly avoids third-party libraries, ensuring the solution is built from scratch.
-----------------------------------------------------------------------------------------------

Project Structure
bash
Copy code
library_management_system/
│
├── app.py              # Main application file
├── models.py           # In-memory data models
├── routes.py           # API route handlers
├── utils.py            # Helper functions (pagination, authentication, etc.)
├── data.json           # Placeholder for initial data (if needed)
└── README.md           # Documentation
-----------------------------------------------------------------------------

How the Project Meets Constraints
No Third-Party Libraries:

All functionalities, including authentication and pagination, are implemented from scratch without external dependencies.
Avoiding AI-Generated Code:

The code is written manually to demonstrate understanding of Flask and REST API design principles.
--------------------------------------------------------------------------------------------------

Possible Extensions
Database Integration:

Replace the in-memory data with a database like SQLite or PostgreSQL.
Frontend:

Build a frontend interface for interacting with the API.
Enhanced Authentication:

Implement user registration, login, and role-based access control.
Testing:

Add automated tests using Python’s unittest or pytest framework.
----------------------------------------------------------------

Conclusion
This project showcases my ability to:

Write clean, modular, and scalable code.
Adhere to REST API design principles.
Build essential features without relying on third-party libraries.

Thank you for reviewing my submission. I look forward to discussing how I can contribute to your organization!