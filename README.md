# Inventory Management System

A Flask REST API with a CLI frontend and OpenFoodFacts integration.

## Project Structure

inventory_project2/

├── app.py              # Flask API and routes

├── inventory.py        # Mock database

├── external_api.py     # OpenFoodFacts integration

├── cli.py              # Command line interface

├── tests/

│   ├── init.py

│   └── test_app.py     # Unit tests

└── README.md

## Setup

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd inventory_project2
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the App

### Start the API
```bash
python app.py
```

### Start the CLI (second terminal)
```bash
python cli.py
```

### Run tests
```bash
pytest tests/ -v
```

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | /inventory | Get all items |
| GET | /inventory/\<id\> | Get one item |
| POST | /inventory | Add new item |
| PATCH | /inventory/\<id\> | Update item |
| DELETE | /inventory/\<id\> | Delete item |
| GET | /inventory/fetch/\<barcode\> | Fetch from OpenFoodFacts |

## Example Requests

### Add a new item
```json
POST /inventory
{
  "product_name": "Oat Milk",
  "brands": "Oatly",
  "price": 94.00,
  "stock": 20
}
```

### Update an item
```json
PATCH /inventory/1
{
  "price": 3.49,
  "stock": 100
}
```

### Fetch from OpenFoodFacts
GET /inventory/fetch/3017620422003
Fetches Nutella by barcode and saves it to inventory.

## CLI Menu Options

View all inventory
View single item
Add new item
Update item
Delete item
Fetch item from OpenFoodFacts by barcode
Exit



