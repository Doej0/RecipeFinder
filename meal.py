import requests
import random


def recipe_search(ingredient, health=None):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = '43b6438f'
    app_key = '802138205f7c348afc9651ad0e032a1d'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

    if health:
        health_query = '&'.join([f'health={h}' for h in health])
        url += f'&{health_query}'

    result = requests.get(url)
    data = result.json()
    return data['hits']


# health param added to include its list of values
# if statement will return health values only if user request health filters using ampersand

def run():
    # Ask user if they want random meal plan
    mealplan = input('Would you like random meal plan with three chosen ingredients? (Y/N): ').upper()

    if mealplan == 'Y':

        # User chooses 3 ingredients to randomize their meal plan
        ingredients = input('Enter three ingredients for your meal plan separated by commas: ')
        ingredient_list = ingredients.split(',')

        # Split them to variables
        ingredient1 = ingredient_list[0].strip()
        ingredient2 = ingredient_list[1].strip()
        ingredient3 = ingredient_list[2].strip()

        print(f"Here is today's meal plan")

        print(f"For breakast")
        result1 = recipe_search(ingredient1)
        randomrecipe1 = random.choice(result1)
        recipe = randomrecipe1['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

        print(f"For dinner")
        result2 = recipe_search(ingredient2)
        randomrecipe2 = random.choice(result2)
        recipe = randomrecipe2['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

        print(f"Snack")
        result3 = recipe_search(ingredient3)
        randomrecipe3 = random.choice(result3)
        recipe = randomrecipe3['recipe']
        print(recipe['label'])
        print(recipe['uri'])
        print()

    else:

        # Request the user to input their first ingredient
        ingredient = input('Enter an ingredient: ')
        # Request the user if they would like to include an additional ingredient
        add_ingredient = input('Would you like an additional ingredient? (Y/N):').upper()
        # Check if the user wants an additional ingredient included or print only the recipe for the first ingredient
        # Ask user if there are any dietary restrictions before printing recipe with additional ingredients
        diet_restriction = input('do you have any dietary restrictions? (Y/N):').upper()

        # health options provided by api held within an array
        health_options = [
            "alcohol-free", "celery-free", "crustacean-free", "dairy-free", "egg-free",
            "fish-free", "gluten-free", "kidney-friendly", "kosher", "low-potassium",
            "lupine-free", "mustard-free", "low-fat-abs", "no-oil-added", "low-sugar",
            "paleo", "peanut-free", "pescatarian", "pork-free", "red-meat-free",
            "sesame-free", "shellfish-free", "soy-free", "sugar-conscious", "tree-nut-free",
            "vegan", "vegetarian", "wheat-free"
        ]

        # an empty array to hold the users selections

        selected_health_options = []

        # if the user says yes to diet restrictions they will then select from the list of options provided for further filtering
        # for loop uses enumerate function(to add counter to choices) and provides user with a list of options from health options
        # and the user can choose 1 or more by using commas

        if diet_restriction == 'Y':
            print("Choose from the list below, if more than one selection (enter the numbers separated by commas):")
            for i, option in enumerate(health_options, 1):
                print(f"{i}. {option}")
            selected_nums = input("Enter your selection(s) here: ")
            selected_nums = [int(idx.strip()) - 1 for idx in selected_nums.split(",")]
            # This line takes the string of comma separated numbs entered by user and converts it into a list of ints it also adjusts
            # each to start in the correct position by subtracting 1 from each ( count starts at  0)
            selected_health_options = [health_options[idx] for idx in selected_nums]

        if add_ingredient == 'Y':
            additional_ingredient = input('Enter the additional ingredient: ')

            # Search for the first ingredient recipes
            first_ingredient_results = recipe_search(ingredient, selected_health_options)
            print('The result from your first recipe request is listed below: ')
            for first_ingredient in first_ingredient_results:
                first_recipe = first_ingredient['recipe']
                print(first_recipe['label'])
                print(first_recipe['uri'])
                # Print the ingredients needed
                for ingredient in first_recipe['ingredientLines']:
                    print(ingredient)
                print()

            # Search for the additional ingredient recipes
            second_ingredient_results = recipe_search(additional_ingredient, selected_health_options)
            print('The result from your second recipe request is listed below: ')
            for second_ingredient in second_ingredient_results:
                second_recipe = second_ingredient['recipe']
                print(second_recipe['label'])
                print(second_recipe['uri'])
                # Print the ingredients needed
                for ingredient in second_recipe['ingredientLines']:
                    print(ingredient)
                print()
        else:
            # Search for the first ingredient recipes
            first_ingredient_results = recipe_search(ingredient, selected_health_options)
            print('The result from your first recipe request is listed below: ')
            for first_ingredient in first_ingredient_results:
                first_recipe = first_ingredient['recipe']
                print(first_recipe['label'])
                print(first_recipe['uri'])
                # Print the ingredients needed
                for ingredient in first_recipe['ingredientLines']:
                    print(ingredient)
                print()


run()
