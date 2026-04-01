import random

print("Welcome to Mad Libs!")
print("Choose a template:")
print("1 - Hospital Story")
print("2 - Camping Trip")
print("3 - Enchanted Castle")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    number = input("Type a number: ")
    measure_of_time = input("Type a measure of time (e.g. days, weeks): ")
    transportation = input("Type a mode of transportation: ")
    adjective1 = input("Type an adjective: ")
    adjective2 = input("Type another adjective: ")
    noun1 = input("Type a noun (plural): ")
    color = input("Type a color: ")
    body_part1 = input("Type a part of the body (plural): ")
    verb1 = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun (plural): ")
    noun3 = input("Type a noun (like an object): ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type a noun (food-like): ")
    adjective3 = input("Type one more adjective: ")
    silly_word = input("Type a silly word: ")

    story = (
        f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}. "
        f"The hospital is a {adjective1} place, there are a lot of {adjective2} {noun1} here. "
        f"There are nurses here who have {color} {body_part1}. "
        f"If someone wants to come into my room I told them that they have to {verb1} first. "
        f"I've decorated my room with {number2} {noun2}. "
        f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
        f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun1}!"
    )

elif choice == "2":
    person = input("Type a person's name: ")
    noun1 = input("Type a noun: ")
    feeling1 = input("Type an adjective (feeling): ")
    verb1 = input("Type a verb: ")
    feeling2 = input("Type another adjective (feeling): ")
    animal1 = input("Type an animal: ")
    verb2 = input("Type another verb: ")
    color1 = input("Type a color: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adverb = input("Type an adverb ending in -ly: ")
    number = input("Type a number: ")
    measure_of_time = input("Type a measure of time: ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    number2 = input("Type another number: ")
    silly_word = input("Type a silly word: ")
    noun2 = input("Type another noun: ")

    story = (
        f"This weekend I am going camping with {person}. "
        f"I packed my lantern, sleeping bag, and {noun1}. "
        f"I am so {feeling1} to {verb1} in a tent. "
        f"I am {feeling2} we might see a {animal1}, I hear they're kind of dangerous. "
        f"While we're camping, we are going to hike, fish, and {verb2}. "
        f"I have heard that the {color1} lake is great for {verb_ing}. "
        f"Then we will {adverb} hike through the forest for {number} {measure_of_time}. "
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
        f"At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!"
    )

elif choice == "3":
    person = input("Type a person's name: ")
    adjective1 = input("Type an adjective: ")
    color = input("Type a color: ")
    animal = input("Type an animal: ")
    place = input("Type a place: ")
    adjective2 = input("Type another adjective: ")
    creature1 = input("Type a magical creature (plural): ")
    adjective3 = input("Type one more adjective: ")
    creature2 = input("Type another magical creature (plural): ")
    room = input("Type a room in a house: ")
    noun1 = input("Type a noun: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type a noun (plural): ")
    adjective4 = input("Type yet another adjective: ")
    noun4 = input("Type a noun (plural): ")
    number = input("Type a number: ")
    measure_of_time = input("Type a measure of time: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adjective5 = input("Type a final adjective: ")
    noun5 = input("Type a final noun: ")

    story = (
        f"Dear {person}, I am writing to you from a {adjective1} castle in an enchanted forest. "
        f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
        f"There are {adjective2} {creature1} and {adjective3} {creature2} here! "
        f"In the {room} there is a pool full of {noun1}. "
        f"I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}. "
        f"It feels as though I have lived here for {number} {measure_of_time}. "
        f"I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"
    )

else:
    story = "Invalid choice. Please run the program again and enter 1, 2, or 3."

# random fun fact at the end
fun_endings = [
    "What a story!",
    "Incredible adventure!",
    "You can't make this stuff up!",
    "10/10 would read again."
]

print("\n--- Your Story ---")
print(story)
print(random.choice(fun_endings))
