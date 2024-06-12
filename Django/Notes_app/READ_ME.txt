Sticky Notes Application
A dynamic Django-powered web application for creating, editing, and managing sticky notes. 
Features a sleek, responsive UI with custom CSS styling, intuitive note creation and detail views, and robust backend functionality.
Perfect for personal organization and productivity, this project demonstrates the integration of Django's powerful MVC framework with modern web development practices.
Explore the code to see how static files, URL routing, and Django's form handling work together seamlessly.


Usage
Run the development server:

bash
Copy code
python manage.py runserver
Access the application in your web browser:
Open your browser and go to http://127.0.0.1:8000/.

Home Page:

The home page provides a form to fill in details and a large button to create a new note.
Creating a Note:

Click the "Create New Note" button on the home page or go to /note/new/ to access the note creation form. Fill in the details and click "Save".
Viewing Notes:

Navigate to /notes/list/ to see a list of all your sticky notes. Click on any note title to view its details.
Editing and Deleting Notes:

From the note detail view, you can edit or delete the note using the provided buttons.
Admin Panel:

If you created a superuser, you can access the Django admin panel at http://127.0.0.1:8000/admin/ to manage your notes and other data directly.
