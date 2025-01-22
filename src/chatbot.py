import pandas as pd

# Load the cleaned dataset
recipes = pd.read_parquet(r'D:\Projects\AI and ML project\Chatbot-recipes\data\cleaned_recipes.parquet')

# Function to search for recipes by ingredient
def search_by_ingredient(ingredient):
    matches = recipes[recipes['RecipeIngredientParts'].apply(
        lambda x: any(ingredient.lower() in item.lower() for item in x)
    )]
    return matches[['Name', 'RecipeInstructions']]

# Function to search for recipes by ingredients (list)
def search_by_ingredients(ingredients):
    matches = recipes[recipes['RecipeIngredientParts'].apply(
        lambda x: all(any(ing.lower() in item.lower() for item in x) for ing in ingredients)
    )]
    return matches[['Name', 'RecipeInstructions']]

# Function to search for recipes by name or keyword
def search_by_recipe_name(name):
    matches = recipes[recipes['Name'].str.contains(name, case=False, na=False)]
    return matches[['Name', 'RecipeInstructions']]

# Function to filter recipes by Category
def filter_by_category(category):
    matches = recipes[recipes['RecipeCategory'].str.contains(category, case=False, na=False)]
    return matches[['Name', 'RecipeInstructions']]

# Function to filter recipes by nutritional content
def filter_by_nutrition(max_calories=None, max_sodium=None):
    filtered = recipes
    if max_calories is not None:
        filtered = filtered[filtered['Calories'] <= max_calories]
    if max_sodium is not None:
        filtered = filtered[filtered['SodiumContent'] <= max_sodium]
    return filtered[['Name', 'RecipeInstructions', 'Calories', 'SodiumContent']]

# Function to recommend recipes based on user preferences
def recommend_recipes(cuisine=None, max_cook_time=None):
    filtered = recipes
    if cuisine:
        filtered = filtered[filtered['Keywords'].apply(lambda x: cuisine.lower() in [kw.lower() for kw in x])]
    if max_cook_time:
        filtered = filtered[filtered['TotalTime'] <= max_cook_time]
    return filtered[['Name', 'RecipeInstructions', 'TotalTime']]

# Combined function to search, filter and recommend recipes
def search_recipes(ingredient=None, category=None, max_calories=None):
    filtered = recipes
    if ingredient:
        filtered = filtered[filtered['RecipeIngredientParts'].apply(
            lambda x: any(ingredient.lower() in item.lower() for item in x)
        )]
    if category:
        filtered = filtered[filtered['RecipeCategory'].str.contains(category, case=False, na=False)]
    if max_calories:
        filtered = filtered[filtered['Calories'] <= max_calories]
    return filtered[['Name', 'RecipeInstructions', 'Calories']]

# Example call
result = search_recipes(ingredient="chicken", category="Healthy", max_calories=300)
print(result.head())
