# Restaurant Menu Management API

## Overview
A Django REST Framework project for managing restaurant menus, allowing restaurant owners to create and manage their restaurant, menu categories, subcategories, dishes, and ingredients.

## Features
- User authentication for restaurant owners
- Create and manage restaurants
- Hierarchical menu structure (Restaurant → Main Categories → Subcategories → Dishes → Ingredients)
- Permissions to ensure only restaurant owners can modify their own data

## Authentication
### Super user
- `Username` : Giga
- `Password` : pass123!
### Test account
- `Username` : Giga1
- `Password` : pass123!

## Models
- **Restaurant**: Basic restaurant information
- **MenuMainCategory**: Top-level menu categories
- **MenuSubCategory**: Subcategories within main categories
- **Dish**: Individual menu items
- **Ingredient**: Components of each dish

## Key Endpoints
- `/restaurants/`: List and create restaurants
- `/main-categories/`: Manage menu main categories
- `/subcategories/`: Manage menu subcategories
- `/dishes/`: Manage dishes
- `/ingredient/`: Manage ingredients

## Requirements
- Django
- Django REST Framework

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/GigaDarchia/DjangoRestaurant.git
   cd DjangoRestaurant
   ```
2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations
   ```bash
   python manage.py migrate
   ```
4. Run the development server
   ```bash
   python manage.py runserver
   ```
   