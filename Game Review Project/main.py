# initial data structure
games = {
    "Halo": {
        "genre": "FPS",
        "platform": "Xbox",
        "rating": 9,
        "review": "Great multiplayer!"
    },
    "Stardew Valley": {
        "genre": "RPG",
        "platform": "PC",
        "rating": 8,
        "review": "Relaxing farming sim."
    }
}

# This is the menu function. Pretty Simple.
def main_menu():
    print("1. Add a new game review")
    print("2. Look at reviewed games")
    print("3. Get Video Game suggestions")
    print("4. Quit")

# When people want to add a review, this function asks for data
def add_review():
    print("\n=== Add a New Game Review ===")

    #Loop for Game title
    while True:
        title = input("Game Title: ").strip()
        if not title:
            print("Title can't be empty. Please try again.")
        elif title in games:
            print("Sorry. A review for this game already exists. Try editing or pick another title.")
        else:
            break
            
    
    #Loop for Game Genre
    while True:
        genre = input("Genre (e.g, RPG, FPS, Adventure): ").strip()
        if genre and not genre.isdigit():
            break
        else:
            print("Please enter a valid genre (cannot be empty or just numbers).")

    #Loop for Game Platform
    while True:
        platform = input("Platform (e.g., PC, Xbox, PlayStation): ").strip()
        if platform and not platform.isdigit():
            break
        else:
            print("Please enter a valid platform (cannot be empty or just numbers).")

    #Loop for Rating
    while True:
        rating = input("Rating (1-10): ").strip()
        if rating and rating.isdigit(): 
            if (int(rating) <= 10 and int(rating) >= 1):
                break
        else:
            print("Please enter a valid rating (cannot be empty, greater than 10, less than 1, or words).")
    
    
    while True:
        review = input("Short Review: ")
        if review:
            break
        else:
            print("Review can't be empty.")
        


    # store this data in a dictionary
    games[title] = {
        "genre": genre,
        "platform": platform,
        "rating": rating,
        "review": review

    }
    
    print(f"Review for {title} is complete!\n")

# THis function is used for displaying current reviews.
def view_review():
    print("\n=== View Game Reviews ===")
    if not games:
        print("No reviews found.\n")
        return
    
    #The code below will ask the user if they want to filter.
    filter_choice = input("You can filter by genre (g), platform (p), or view all (a)").strip().lower()
    
    filter_val = None
    filter_key = None

    if filter_choice == "g":
        filter_val = input("Enter genre to filter by: ").strip().lower()
        filter_key = "genre"
    elif filter_choice == "p":
        filter_val = input("Enter platform to filter by: ").strip().lower()
        filter_key = "platform"

    found = None #used to track if any displayed revies match the filter
    for title, info in games.items():
        show_review = True
        if filter_key:
            # Compare lower-case for more robust matching
            if info[filter_key].lower() != filter_val:
                show_review = False
        if show_review:
            found = True
            print("-" * 40)
            print(f"Title:     {title}")
            print(f"Genre:     {info['genre']}")
            print(f"Platform:  {info['platform']}")
            print(f"Rating:    {info['rating']}/10")
            print(f"Review:    {info['review']}")
    if not found:
        print("No reviews found for your filter.\n")
    else:
        print("-"*40 + "\n")

# the main loop of code
def main_loop():
    while True:
        main_menu()
        choice = input("Hey, what do you want to do?: \n")

        if choice == "1":
            add_review()
        elif choice == "2":
            view_review()
        elif choice == "3":
            pass
        elif choice == "4":
            break
        else:
            print("\nDude, you're pretty dumb. Enter a number.\n")
            
main_loop()
