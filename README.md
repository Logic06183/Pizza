

# Pizza Inventory Management and Ordering System

## Overview

This project is a Django-based web application designed for managing pizza orders and tracking inventory levels for daily and weekly stock in a pizza shop. It allows users to:

- Place orders and track pizza types, quantities, and order statuses.
- Manage daily and weekly inventory of ingredients and other stock items.
- Generate and review daily and weekly stock reports.

## Features

1. **Pizza Order Management:**
   - Create new pizza orders with customizable pizza types and quantities.
   - Track order time, preparation time, and high-priority/late orders.
   - View detailed reports of daily pizza orders.

2. **Inventory Management:**
   - Manage daily and weekly stock levels, including adding new deliveries and recording closing stock.
   - Track inventory items such as pizza ingredients and other supplies.
   - Mark stock items as requiring orders when stock levels are low.

3. **Stock Reports:**
   - View detailed daily and weekly stock reports.
   - Easily add or remove stock items through the reports page.
   - Track new deliveries, closing stock, and order requirements for all items.

## Technologies Used

- **Python (3.12)** with Django (5.0.6)
- **PostgreSQL** for the database backend
- **HTML/CSS** for front-end styling
- **JavaScript** for dynamic form handling (add/remove stock rows)
  
## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/pizza-inventory.git
   cd pizza-inventory
   ```

2. **Install dependencies:**
   Make sure you have Python 3.12+ and Django 5.0.6+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Database setup:**
   Configure your database settings in `settings.py`, then apply migrations:
   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8001/`.

## Usage

1. **Order Management:**
   - Go to the Orders section to create new pizza orders.
   - Track ongoing orders and view detailed reports of pizza consumption.

2. **Inventory Management:**
   - Visit the Daily Stocks or Weekly Stocks page to manage stock items.
   - Add new stock deliveries or adjust closing stock levels.
   - Use the Daily or Weekly Reports pages to review and update inventory.

## Contribution

Contributions are welcome! Please submit pull requests or report issues for improvements.

## License

This project is licensed under the MIT License.

---

Let me know if you'd like any additional details or sections added!
