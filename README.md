# alx_travel_app_0x00

This project is a duplicate of `alx_travel_app` focusing on database modeling, API serialization, and data seeding for a travel application.

## Project Structure

- `listings/models.py`: Defines the `Listing`, `Booking`, and `Review` database models.
- `listings/serializers.py`: Contains Django REST Framework serializers for `Listing` and `Booking` models.
- `listings/management/commands/seed.py`: A custom Django management command to populate the database with sample data.

## Setup and Installation

1.  **Duplicate the Project:**
    If you haven't already, duplicate the `alx_travel_app` project:
    ```bash
    cp -r alx_travel_app alx_travel_app_0x00
    cd alx_travel_app_0x00
    ```

2.  **Navigate to the project root:**
    ```bash
    cd alx_travel_app
    ```

3.  **Create a Virtual Environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install Django djangorestframework Faker
    ```

5.  **Apply Migrations:**
    Make sure your database schema is up-to-date with the defined models.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Database Seeding

To populate the database with sample `Listing`, `Booking`, and `Review` data, run the custom management command:

```bash
python manage.py seed