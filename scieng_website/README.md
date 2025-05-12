# SciEng Website

`SciEng Website` is a Django web app for a science and engineering organization. It showcases projects, provides user authentication, and includes a contact form.

---

## Table of Contents

1. [Features](#features)
2. [How to Install](#how-to-install)
3. [Usage](#usage)
4. [License](#license)
5. [Contact](#contact)
6. [Images](#images)
7. [Screenshots of Project](#screenshots-of-project)

---

## Features!

- **Home Page**: Introduces the organization.
- **Projects**: Displays a list of projects with details and has images.
- **User Authentication**: Allows users to sign up, log in, and log out.
- **Responsive Design**: Works on both desktop and mobile devices.

---

## How to Install?

1. **Clone the Project**:
   ```bash
   git clone <repository-url>
   cd scieng_website
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For Unix-based systems
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   python manage.py migrate
   ```

5. **Run the App**:
   ```bash
   python manage.py runserver
   ```

6. **Open in Your Browser**:
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

1. Navigate to the home page to learn about the organization.
2. Explore the **Projects** section to view detailed project information.
3. Use the **Sign Up** or **Log In** options to create an account or access additional features.
4. Use the **Contact Form** to send inquiries or feedback.
5. In Web url with ending in 8000/admin/ to access admin but create superuser before then.
6. If you get an error page but it show web urls just add whatever is there to 8000/ in url to navigate to the desired urls.
7. Look to Screenshots section for better visuals on this.

---

## License

Has no licence.

---

## Contact

Questions or feedback? Email me at [barnesjulian368@gmail.com].

---

## Images

The images in this project are not mine and are for placeholder purposes only.

---

## Screenshots of Project

<p text-align="center">
   <img src="screenshots3/Screenshot 1.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 2.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 3.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 4.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 5.png" width="400px" height="400px" alt="image of project"/>
   <img src="screenshots3/Screenshot 6.png" width="400px" height="400px" alt="image of project"/>
</p>
