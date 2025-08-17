# Authentication Documentation

## Overview
This project uses Django's built-in authentication system, extended with custom forms and a Profile model for additional user information. Users can register, log in, log out, and update their profile.

---

## Authentication Process

### 1. **Registration**
- Users access the registration page via `/register/`.
- The `UserRegistrationForm` collects username, first name, last name, email, and password.
- On successful registration, a new user is created and redirected to the login page.

### 2. **Login**
- Users access the login page via `/login/`.
- The login form collects username and password.
- On successful authentication, users are redirected to the home or feeds page.

### 3. **Logout**
- Users can log out via the `/logout/` URL.
- After logout, users are redirected to the home page.

### 4. **Profile Update**
- Logged-in users can access `/profile/` to update their account and profile information.
- The `UserUpdateForm` allows updating username and email.
- The `ProfileUpdateForm` allows updating phone number, gender, age, address, bio, and images.

---

## User Interaction

- **Register:** Fill out the registration form and submit. On success, you will be prompted to log in.
- **Login:** Enter your credentials and submit. On success, you will be redirected to your dashboard or feeds.
- **Logout:** Click the logout button in the navigation bar.
- **Update Profile:** Access your profile page, update details, and save changes.

---

## Testing Authentication Features

1. **Registration**
   - Go to `/register/`.
   - Fill in all required fields and submit.
   - Check for success message and redirection to login.

2. **Login**
   - Go to `/login/`.
   - Enter valid credentials and submit.
   - Verify redirection and authenticated session.

3. **Logout**
   - Click the logout button.
   - Confirm you are redirected and session is ended.

4. **Profile Update**
   - Log in and go to `/profile/`.
   - Change details and submit.
   - Check for success message and updated information.

---

## Notes
- CSRF protection is enabled for all forms.
- Only authenticated users can access feeds and profile pages.
- Error messages are displayed for invalid form submissions.




#
I want this to be added to the readme

Feature Documentation:
Document the blog post features in a README file or directly in the code as comments. Include details on how to use each feature and any special notes about permissions and data handling.

#
System Documentation:
Document the comment system thoroughly, explaining how to add, edit, and delete comments. Include any rules related to comment visibility and user permissions.