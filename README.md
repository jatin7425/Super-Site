# Super-Site

```markdown
# Learning Management System (LMS)

A Django-based web application for managing and sharing learning entries with user collaboration features.

## Features

- **User Authentication**
  - Registration with email
  - Login/Logout functionality
  - Protected routes for authenticated users

- **Learning Entries Management**
  - Create/edit learning entries
  - Mark entries as completed
  - Soft delete functionality
  - Rich text content support

- **Collaboration Features**
  - Share entries with multiple users
  - Searchable user dropdown (Select2)
  - View shared entries from others
  - Visual indicators for shared entries

- **UI/UX**
  - Responsive design
  - Dark/Light theme toggle
  - Tailwind CSS styling
  - Interactive hover effects
  - Progress indicators
  - Confirmation modals

- **Additional Features**
  - SQLite database
  - Django admin interface
  - Form validation
  - CSRF protection
  - Error handling

## Technologies Used

- **Backend**
  - Python 3.x
  - Django 4.x
  - Django Select2

- **Frontend**
  - Tailwind CSS
  - HTML5
  - JavaScript (ES6)
  - Select2

- **Database**
  - SQLite (Development)
  - PythonAnywhere MySQL (Production)

- **Deployment**
  - PythonAnywhere
  - Git Version Control

## Installation

1. **Clone Repository**
   ```bash
   git clone [your-repository-url]
   cd learning-management-system
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Configuration

1. **Environment Variables**
   - Create `.env` file in project root:
     ```
     DEBUG=True
     SECRET_KEY=your-secret-key
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

2. **Tailwind CSS Setup**
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

3. **Select2 Configuration**
   - Ensure proper CDN links in base template
   - Configure caching in settings.py

## Deployment (PythonAnywhere)

1. **Create PythonAnywhere Account**
2. **Set Up New Web App**
3. **Configure:**
   - Virtual environment
   - WSGI configuration file
   - Static files mapping
4. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

## Screenshots

![Dashboard](screenshots/dashboard.png)
![Create Entry](screenshots/create-entry.png)
![Shared Entries](screenshots/shared-entries.png)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
   
---

**Note:** This project uses SQLite for development simplicity. For production environments, consider using PostgreSQL or MySQL.
```

This README includes:
- Project overview
- Key features list
- Technology stack
- Installation instructions
- Configuration guidelines
- Deployment steps
- Contributing guidelines
- License information

You should:
1. Create a `screenshots` directory and add actual screenshots
2. Update the repository URL in installation section
3. Add any additional environment variables you're using
4. Customize the license if needed
5. Add proper documentation for any custom configurations

Would you like me to explain any specific section in more detail?
