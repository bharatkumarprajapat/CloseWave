Closewave
# CloseWave
This web application is a comprehensive solution developed using Django, a high-level Python web framework. The application integrates several key functionalities: a To-Do app, an Employee Management System (EMS), and a Job Board. Below is a detailed explanation of each component and the technologies used in this project.

## Features

### 1. To-Do App
The To-Do app helps users manage their tasks effectively. It allows users to:

- **Create, Read, Update, and Delete Tasks**: Users can add new tasks, view existing tasks, modify task details, and delete tasks.
- **Set Deadlines and Priorities**: Tasks can have deadlines and priority levels assigned to them.
- **Mark Tasks as Completed**: Users can mark tasks as completed.
- **Categorize Tasks**: Tasks can be categorized for better organization.

### 2. Employee Management System (EMS)
The Employee Management System streamlines HR processes and manages employee data efficiently. It includes features such as:

- **Employee Records Management**: Add and maintain employee records including name, contact details, job title, etc.
- **Department and Role Management**: Organize employees by departments and roles.
- **Performance and Attendance Tracking**: Track employee performance and attendance.

### 3. Job Board
The Job Board facilitates job postings and applications. It includes:

- **Job Postings**: Employers can post job openings.
- **Job Browsing and Application**: Job seekers can browse and apply for jobs.
- **Application Tracking**: Employers can manage job applications.
- **Notifications and Updates**: Both employers and job seekers receive notifications and updates about job applications.

## Technologies Used

### Django
Django is the primary framework used for this project. It provides a robust and scalable foundation for building web applications with built-in features such as ORM, authentication, and an admin interface.

### Python
Python is the programming language used to develop the backend of the application. It is known for its readability and efficiency, making it ideal for web development with Django.

### HTML & CSS
HTML and CSS are used for the frontend of the application. HTML structures the content, while CSS is used to style the application, ensuring a responsive and visually appealing user interface.

### PostgreSQL
PostgreSQL is the database management system used to store and manage the application's data. It is a powerful, open-source object-relational database system known for its reliability and performance.

## Detailed Code Explanation

### User Registration and Login

#### register View
- **POST Request Handling**: Collects user data from the registration form.
- **Validation**:
  - Checks if the provided registration code matches the predefined code ("EMS24").
  - Ensures the username and email are unique.
  - Confirms that the passwords match.
- **User Creation**: Creates a new user with a hashed password and saves it to the database.
- **Email Notification**: Sends a welcome email to the newly registered user.
- **Redirection**: Redirects the user to the login page upon successful registration.

#### login View
- **Authentication**: Authenticates the user using the provided username and password.
- **Redirection**: Redirects the user to the EMS page upon successful login, or back to the login page if authentication fails.

#### logout_view View
- **Logout**: Logs out the user and redirects to the product page.

### Employee Management System (EMS)

#### user_list View
- **User List Display**: Retrieves and displays a list of all users.

#### manage View
- **Employee Form Handling**: Handles both displaying and submitting the employee form.
- **Form Validation and Submission**: Validates and saves the form data to the database.

#### show View
- **Employee List Display**: Retrieves and displays a list of all employees.

#### edit View
- **Employee Edit Form Display**: Displays the form for editing an employee's details.

#### update View
- **Employee Update Handling**: Handles form submission for updating an employee's details.

#### destroy View
- **Employee Deletion**: Deletes an employee from the database.

### To-Do App

#### todo View
- **Task Form Handling**: Handles both displaying and submitting the task form.
- **Task List Display**: Retrieves and displays a list of all tasks.

#### editTodo and updateTodo Views
- **Task Edit Form Display**: Displays the form for editing a task.
- **Task Update Handling**: Handles form submission for updating a task.

#### destroyTodo View
- **Task Deletion**: Deletes a task from the database.

#### checkpoint View
- **Task Completion**: Marks a task as completed.

### EMS Page and Profile Management

#### EMS_page View
- **EMS Page Display**: Renders the EMS main page.

#### profile View
- **Profile Form Handling**: Handles both displaying and submitting the profile form.
- **Profile List Display**: Retrieves and displays a list of all profiles.

### Leave Management

#### leave View
- **Leave Form Handling**: Collects leave request data and sends an email notification.

### Task Assignment and Performance Management

#### Taskassign View
- **Task Assignment**: Allows authorized users to assign tasks.
- **Task List Display**: Displays tasks assigned to the user.

#### delete_task View
- **Task Deletion**: Deletes a task and sends an email notification.

#### performance_page View
- **Performance Rating**: Allows authorized users to rate the performance of employees.

#### account_page View
- **User Performance Display**: Displays the performance ratings for the logged-in user.

### Communication and Training Management

#### chatterbox View
- **Chat Box Display**: Renders the chat box page.

#### send_message View
- **Message Sending**: Handles sending messages between users.

#### schedule_training and manage_training Views
- **Training Session Management**: Allows authorized users to schedule and manage training sessions.

#### view_schedule View
- **Training Schedule Display**: Displays the training schedule for users.

### Recipe Sharing

#### recipe and recipe_list Views
- **Recipe List Display**: Retrieves and displays a list of all recipes.

#### recipe_detail View
- **Recipe Detail Display**: Displays detailed information about a specific recipe.

#### add_recipe View
- **Recipe Form Handling**: Handles both displaying and submitting the recipe form.

### Job Board

#### Careerregister and Careerlogin Views
- **User Registration and Login**: Handles registration and login for job seekers.

#### post_job View
- **Job Posting Form Handling**: Handles both displaying and submitting the job posting form.

#### job_details View
- **Job Detail Display**: Displays detailed information about a specific job.

#### apply_job View
- **Job Application Form Handling**: Handles both displaying and submitting the job application form.

#### application_success View
- **Application Success Display**: Renders a success page upon successful job application.

#### job_list View
- **Job List Display**: Retrieves and displays a list of all job postings.
