# import json

recipe_file = "recipes.json"
def  load_recipes():
    try:
        with open(recipe_file,"r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {}
def save_recipes(recipes):
    with open(recipe_file,"w") as file:
        json.dump(recipes,file,indent=4)
def add_recipe(recipes):
    name = input("enter recipe name: ")
    ingredients = input("enter ingredients(comma_seperated): ")
    instructions = input("enter instructions: ")

    recipes[name] = {"ingredients":ingredients.split(","),"instructions":instructions} 
    print(f"recipe'{name}'added!")       
def view_recipes(recipes):
    if not recipes:
        print("No recipes found.")
    else:
        for name, details in recipes.items():
            print(f"\nrecipe:{name}")
            print("ingredients:")
            for ingredient in details["ingredients"]:
                print(f"- {ingredient}")
            print("instructions:",details["instructions"])

def search_recipe(recipes):
    name = input("enter recipe name to search for: ") 
    recipe = recipes.get(name)
    if recipe:
        print("\nrecipe:{name}")
        print("ingredients:") 
        for ingredient in recipe["ingredients"]:
            print(f"-{ingredient}")
        print("instructions:",recipe["instructions"])
    else:
        print(f"No recipe found with the name '{name}'.")
def main():
    recipes = load_recipes()

    while True:
        print("\nrecipe book")
        print("1. add recipes")
        print("2. view recipes")
        print("3. search recipe")
        print("4. Quit")

        choice = input("choose an option: ")

        if choice == "1":
            add_recipe(recipes)
            save_recipes(recipes)
        elif choice == "2":
            view_recipes(recipes)
        elif choice == "3":
            search_recipe(recipes)
        elif choice == "4":
            print("Good bye!")
            break
        else:
            print("Invalid choice.please try again")

if __name__  == "__main__":
    main()
