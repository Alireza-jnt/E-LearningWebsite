# E-Learning Website

## Introduction
This project is a Django-based application that includes role management and an authentication system. After setting up migrations, you can use the following management commands to initialize the system:

- `init_roles` – Creates the basic set of roles.
- `makesuperuser` – Creates an admin user.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.x)
- PostgreSQL or SQLite (for local development)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Alireza-jnt/E-LearningWebsite.git
   cd E-LearningWebsite
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Initialize roles:
   ```bash
   python manage.py init_roles
   ```

6. Create a superuser:
   ```bash
   python manage.py makesuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- The admin panel is available at `http://127.0.0.1:8000/admin/`.
- Authentication and user management are handled via Django’s built-in authentication system.

## Contributing
Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Future Enhancements
- Add API documentation.
- Implement CI/CD for automated testing and deployment.
- Improve role-based access control (RBAC).

