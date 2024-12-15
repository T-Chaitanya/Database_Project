# Tax Payment Management System

---

## Description:
This project is a web-based Tax Payment Management System built using Flask, SQLAlchemy, and Bootstrap. It provides an interface for users to manage tax payment records, filter by due dates and tax rates, and perform CRUD (Create, Read, Update, Delete) operations.

---

## Features:
- **CRUD Operations**: 
  - Add new tax payment records.
  - View existing tax payment records.
  - Edit existing tax payment records.
  - Delete tax payment records.
  
- **Filtering Options**:
  - Filter payments by Due Date.
  - Filter payments by Tax Rate.
  
- **Bootstrap UI**:
  - Responsive table layout with sorting and pagination.
  - Modals for Edit and Delete operations.

---

## Technologies Used:
- **Backend**: Python, Flask, SQLAlchemy
- **Database**: MySQL
- **Frontend**: Bootstrap, HTML, CSS, JavaScript
- **Styling**: Bootstrap for UI design and responsiveness

---

## Prerequisites:
1. **Python** (>= 3.7)
2. **Flask**: `pip install Flask`
3. **SQLAlchemy**: `pip install flask-sqlalchemy`
4. **MySQL**: Ensure MySQL is installed and running.
5. **Bootstrap**: CSS and JS from CDN.

---

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd tax-payment-management
   ```

2. Set up virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate  # For Windows
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure `app.py`:
   - Update database configuration in `app.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/tax'
     ```

---

## Running the Application:
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/` to access the Tax Payment Management System.

---

## Usage:
1. **Add Payment**: Use the form to add new tax payment records.
2. **View Payments**: View all payments in a table.
3. **Filter Payments**: Use the dropdown to filter by due date and tax rate.
4. **Edit/Delete**: Use the buttons to manage payment records via modals.

---

## Contribution:
- Fork this repository and create a pull request.
- Feel free to suggest improvements or submit issues.

---

## License:
[MIT](LICENSE)

---
