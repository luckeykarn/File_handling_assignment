import csv
from fpdf import FPDF 
import os

filename = "recipe_book.csv" 
recipes = []

# Load recipe from csv file
def load_recipe():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) == 4:
                    recipe = {
                        "title": row[0],
                        "ingredients": row[1].split(', '),
                        "steps": row[2],
                        "tags": row[3].split(', ')
                    }
                    recipes.append(recipe)

# Save recipe to csv file
def save_recipe():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Ingredients", "Steps", "Tags"])  # Header
        for recipe in recipes:
            ingredients = ', '.join(recipe["ingredients"])
            tags = ', '.join(recipe["tags"])
            writer.writerow([recipe["title"], ingredients, recipe["steps"], tags])

# Load existing recipes
load_recipe()

# Add a new recipe
def add_recipe():
    title = input("Enter recipe title: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    steps = input("Enter steps: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    
    recipe = {
        "title": title,
        "ingredients": [i.strip().lower() for i in ingredients],
        "steps": steps.strip(),
        "tags": [t.strip().lower() for t in tags]
    }
    recipes.append(recipe)
    save_recipe()
    print("Recipe added successfully!")

# Search recipes
def search_recipe():
    search_type = input("Search by (tag / ingredient): ").lower()
    search_value = input("Enter value to search: ").lower().split(',')
    found = False 
    
    for recipe in recipes:
        if search_type == "tag":
            for val in search_value:
                if val.strip() in recipe["tags"]:
                    print(f"- {recipe['title']} (Tags: {', '.join(recipe['tags'])})")
                    found = True

        elif search_type == "ingredient":
            for val in search_value:
                if val.strip() in recipe["ingredients"]:
                    print(f"{recipe['title']} (Ingredients: {', '.join(recipe['ingredients'])} Steps: {recipe['steps']})")
                    found = True
                    break

    if found:
        print(f"Recipes found by {search_type}.")
    else:
        print("No recipes found.")

# CLI interface
while True:
    print("\nCLI Recipe Book")
    print("add | search or search_recipe | exit |")
    command = input("Enter command: ").lower()

    if command == "add":
        add_recipe()
    elif command == "search" or command == "search_recipe":  
        search_recipe()
    elif command == "exit":
        print("Thanks for using CLI Recipe!")
        save_recipe()
        break
    else:
        print("Invalid command.")

# Export recipes to PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Recipe Book", ln=1, align='C')
pdf.ln(5)

for recipe in recipes:
    pdf.cell(200, 10, txt=f"Title: {recipe['title']}", ln=1)
    pdf.cell(200, 10, txt=f"Ingredients: {', '.join(recipe['ingredients'])}", ln=1)
    pdf.cell(200, 10, txt=f"Steps: {recipe['steps']}", ln=1)
    pdf.cell(200, 10, txt=f"Tags: {', '.join(recipe['tags'])}", ln=1)
    pdf.ln(5)

pdf.output("recipe_book.pdf")
