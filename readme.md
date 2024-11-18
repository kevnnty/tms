# Transport Management System (TMS)

The **Transport Management System (TMS)** is a web-based application for managing routes, vehicles, and drivers for a transportation company. The application provides an interface for administrators to assign vehicles to routes, manage driver assignments, and view detailed records of the company’s transport operations.


## Features

- **Route Management:** Create, update, and delete routes with details including start and end locations, estimated travel time, and assigned vehicles.
- **Vehicle Management:** Register vehicles, view assigned routes, and track the availability of vehicles for each route.
- **Driver Management:** Manage drivers, assign vehicles to drivers, and view driver details.
- **Pagination and Filtering:** Efficient pagination and filtering to manage a large number of records seamlessly.
- **User Authentication:** Secure login and registration to manage data.
- **Analytics:** Analytics about Vehicle informance and Driver performance (Coming soon)

## Technologies

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, TailwindCSS for styling
- **Database:** PostgreSQL
- **Tools:** Django ORM, Django Templates

---

## Installation
To set up and run the project locally, follow these steps:

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kevnnty/tms.git
2. **Set Up Virtual Environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
3. **Set Up PostgreSQL Database:**
    - Create a PostgreSQL database for the project.
    - Update the DATABASES configuration in the Django project’s settings file with your database information.
4. **Run Migrations:**
    ```
    python manage.py makemigrations
    python manage.py migrate
5. **Start Development Server**
    ```
    python manage.py runserver
    ```

6. **Access the Application:**
    - Open a browser and go to http://127.0.0.1:8000.



# Usage

## Key Apps

- **Routes List**: View, add, and manage routes and their assigned vehicles.
- **Drivers List**: View, add, and assign vehicles to drivers.
- **Vehicles Management**: Register vehicles and assign them to routes and drivers.
