# Flask Web Application

This repository contains a simple Flask web application with two routes: `/home` and `/about`.

## Project Structure

├── app.py  
├── templates/  
  │   ├── index.html  
  │   └── about.html  
└── README.md


-   `app.py`: Contains the Flask application logic and route definitions.
-   `templates/`: Directory containing the HTML templates for the web pages.
    -   `index.html`: The home page template.
    -   `about.html`: The about page template.
-   `README.md`: This file, providing information about the application.

## Prerequisites

Before running the application, ensure you have the following installed:

-   **Python:** (3.6 or higher recommended)
-   **Flask:** (Install using pip)

## Installation

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/MrTG-CodeBot/python-web
    cd python-web
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    -   **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install Flask:**

    ```bash
    pip install flask
    ```

## How to Run the Application

1.  **Navigate to the project directory:**

    ```bash
    cd python-web
    ```

2.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    This will start the Flask development server. You should see output similar to this:

    ```
    * Serving Flask app "app" (lazy loading)
    * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
    * Debug mode: on
    * Running on [http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/) (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 123-456-789
    ```

3.  **Open your web browser and access the application:**

    -   **Home page:** `http://127.0.0.1:5000/home`
    -   **About page:** `http://127.0.0.1:5000/about`

4.  **To stop the server, press `Ctrl+C` in the terminal.**

## How to Use the Application

-   **Home Page:**
    -      Displays a welcome message.
    -      Provides a link to the "About" page.
-   **About Page:**
    -      Displays information about the application, including the user name and server.
    -   Provides a link back to the "Home" page.

## Key Concepts

-   **Flask:** A lightweight and flexible Python web framework.
-   **Routes:** Define the URLs that the application responds to.
-   **Templates:** HTML files used to render the web pages.
-   **`render_template()`:** Flask function used to render HTML templates.
-   **Template variables:** using the `{{ variable_name }}` syntax to pass data from python to html.
-   **Debug Mode:** Enables automatic reloading of the server and debugging information.

## Notes

-   The `debug=True` option in `app.run()` enables debug mode. This should be disabled in a production environment.
-   For production deployments, use a production-ready WSGI server like Gunicorn or uWSGI.
-   Ensure that the `templates` folder is in the same directory as `app.py`.
-   If you modify the python code, or the html files, the server will reload automatically due to debug mode being on.
