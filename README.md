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
pip install flask requests pytest python-dotenv
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



Step 8 — Push to GitHub
First create a .gitignore file so you don't push unnecessary files:
Create .gitignore in your root folder:
.venv/
__pycache__/
*.pyc
.env
Now run these git commands one at a time:
Initialize git:
bashgit init
Create your first branch:
bashgit checkout -b main
Stage all files:
bashgit add .
Make your first commit:
bashgit commit -m "Initial commit - inventory management system"
Now go to GitHub:

Go to github.com
Click the + button top right
Click New repository
Name it inventory_management
Leave it empty (no README, no .gitignore)
Click Create repository

Copy the commands GitHub shows you under "push an existing repository" — they will look like this:
bashgit remote add origin https://github.com/yourusername/inventory_management.git
git push -u origin main

Once that's done your whole project is done. Here's what you built:
FileWhat you learnedinventory.pyPython lists as databasesexternal_api.pyCalling external APIs with requestsapp.pyFlask routes, CRUD, HTTP methodscli.pyBuilding a menu that talks to an APItest_app.pyWriting tests with pytest and mocking
Tell me when it's on GitHub and I'll help you with anything else!