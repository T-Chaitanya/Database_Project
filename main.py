from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def format_date(date_string):
    if date_string:
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.strftime('%m/%d/%Y')
        except ValueError:
            return 'NA'  # In case of an error with the format
    return 'NA'  # If date_string is None or empty

# Initialize the Flask application and configure the database URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)

# Models
class TaxPayment(db.Model):
    __tablename__ = 'TaxPayment'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.String(20))  # Optional
    status = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.String(20))  # Optional

    def __repr__(self):
        return f"<TaxPayment {self.id} {self.company} {self.amount}>"

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Routes
# @app.route("/")
# def home():
#     """Homepage."""
#     return render_template("index.html")


# @app.route("/")
# def index():
#     """View all tax payments."""
#     payments = TaxPayment.query.all()
#     total_amount = sum(payment.amount for payment in payments)
#
#     return render_template("payments.html", payments=payments,total_amount = total_amount)
@app.route('/')
def index():
    # Get current year
    current_year = datetime.now().year

    # Get selected due date from query parameters
    selected_due_date = request.args.get('due_date', '')
    selected_tax_rate = request.args.get('tax_rate', 0)
    if selected_tax_rate == '':
        selected_tax_rate = 0

    # Query all payments or filter by due date
    if selected_due_date:
        try:
            due_date_obj = datetime.strptime(selected_due_date, '%m/%d/%Y').date()
            print(due_date_obj,selected_due_date)
            payments = TaxPayment.query.filter_by(due_date=selected_due_date).all()
        except ValueError:
            payments = []
    else:
        payments = TaxPayment.query.all()

    # Calculate total amount
    total_amount = sum(float(payment.amount) for payment in payments)
    total_tax = total_amount * (float(selected_tax_rate))

    # Render the template with data
    return render_template(
        'payments.html',
        payments=payments,
        total_amount=total_amount,
        selected_due_date=selected_due_date,
        current_year=current_year,
        total_tax = total_tax,
        tax_rate = str(float(selected_tax_rate)*100)+"%"
    )

@app.route("/payments/add", methods=["GET", "POST"])
def add():
    """Add a new tax payment."""
    if request.method == "POST":
        company = request.form["company"]
        amount = request.form["amount"]
        payment_date = request.form["payment_date"] or "NA"
        status = request.form["status"]
        due_date = request.form["due_date"]

        # Create a new TaxPayment object and add it to the database
        new_payment = TaxPayment(
            company=company, amount=amount, payment_date=format_date(payment_date), status=status, due_date=due_date
        )
        print(payment_date,due_date)
        db.session.add(new_payment)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_payment.html", current_year = 2024)


@app.route("/payments/edit/<int:payment_id>", methods=["GET", "POST"])
def edit(payment_id):
    """Edit an existing tax payment."""
    payment = TaxPayment.query.get_or_404(payment_id)

    if request.method == "POST":
        payment.company = request.form["company"]
        payment.amount = request.form["amount"]
        payment.payment_date = format_date(request.form["payment_date"]) or "NA"
        payment.status = request.form["status"]
        payment.due_date = request.form["due_date"]
        print(format_date(request.form["payment_date"]))
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("edit_payment.html", payment=payment)


@app.route("/payments/delete/<int:payment_id>", methods=["POST"])
def delete(payment_id):
    """Delete a tax payment."""
    payment = TaxPayment.query.get_or_404(payment_id)
    db.session.delete(payment)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
