import random

def get_input(prompt, is_number=False):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(" Input cannot be empty.")
            continue
        if is_number and not user_input.isdigit():
            print(" Please enter a valid number.")
            continue
        return user_input

print("Welcome to Mad Libs!")
print("Choose a template:")
print("1 - Hospital Story")
print("2 - Camping Trip")
print("3 - Enchanted Castle")

choice = input("Enter 1, 2, or 3: ")
while choice not in ("1", "2", "3"):
    print("❌ Invalid choice.")
    choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    number = get_input("Type a number: ", True)
    measure_of_time = get_input("Type a measure of time: ")
    transportation = get_input("Type a mode of transportation: ")
    adjective1 = get_input("Type an adjective: ")
    adjective2 = get_input("Type another adjective: ")
    noun1 = get_input("Type a noun (plural): ")
    color = get_input("Type a color: ")
    body_part1 = get_input("Type a part of the body (plural): ")
    verb1 = get_input("Type a verb: ")
    number2 = get_input("Type another number: ", True)
    noun2 = get_input("Type another noun (plural): ")
    noun3 = get_input("Type a noun: ")
    body_part2 = get_input("Type another part of the body: ")
    verb2 = get_input("Type another verb: ")
    noun4 = get_input("Type a noun (food): ")
    adjective3 = get_input("Type one more adjective: ")
    silly_word = get_input("Type a silly word: ")

    story = (
        f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transportation}. "
        f"The hospital is a {adjective1} place, there are a lot of {adjective2} {noun1} here. "
        f"There are nurses here who have {color} {body_part1}. "
        f"If someone wants to come into my room I told them that they have to {verb1} first. "
        f"I've decorated my room with {number2} {noun2}. Today I talked to a doctor and they were "
        f"wearing a {noun3} on their {body_part2}. I heard that all doctors {verb2} {noun4} every day. "
        f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun1}!"
    )

elif choice == "2":
    person = get_input("Type a person's name: ")
    noun1 = get_input("Type a noun: ")
    feeling1 = get_input("Type an adjective (feeling): ")
    verb1 = get_input("Type a verb: ")
    feeling2 = get_input("Type another adjective (feeling): ")
    animal1 = get_input("Type an animal: ")
    verb2 = get_input("Type another verb: ")
    color1 = get_input("Type a color: ")
    verb_ing = get_input("Type a verb ending in -ing: ")
    adverb = get_input("Type an adverb ending in -ly: ")
    number = get_input("Type a number: ", True)
    measure_of_time = get_input("Type a measure of time: ")
    color2 = get_input("Type another color: ")
    animal2 = get_input("Type another animal: ")
    number2 = get_input("Type another number: ", True)
    silly_word = get_input("Type a silly word: ")
    noun2 = get_input("Type another noun: ")

    story = (
        f"This weekend I am going camping with {person}. I packed my lantern, sleeping bag, and {noun1}. "
        f"I am so {feeling1} to {verb1} in a tent. I am {feeling2} we might see a {animal1}. "
        f"While we're camping, we are going to hike, fish, and {verb2}. The {color1} lake is great for {verb_ing}. "
        f"Then we will {adverb} hike for {number} {measure_of_time}. If I see a {color2} {animal2}, "
        f"I'll bring it home! At night we tell {number2} {silly_word} stories and roast {noun2}!"
    )

elif choice == "3":
    person = get_input("Type a person's name: ")
    adjective1 = get_input("Type an adjective: ")
    color = get_input("Type a color: ")
    animal = get_input("Type an animal: ")
    place = get_input("Type a place: ")
    creature1 = get_input("Type a magical creature (plural): ")
    room = get_input("Type a room in a house: ")
    noun1 = get_input("Type a noun: ")
    noun3 = get_input("Type a noun (plural): ")
    number = get_input("Type a number: ", True)
    measure_of_time = get_input("Type a measure of time: ")
    verb_ing = get_input("Type a verb ending in -ing: ")
    adjective5 = get_input("Type a final adjective: ")
    noun5 = get_input("Type a final noun: ")

    story = (
        f"Dear {person}, I am writing from a {adjective1} castle. I got here after riding a {color} {animal} in {place}. "
        f"There are {creature1} everywhere! In the {room} there is a pool of {noun1}. "
        f"I dream of {noun3} every night. It feels like I've been here for {number} {measure_of_time}. "
        f"The only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"
    )

fun_endings = ["What a story!", "Incredible adventure!", "10/10 would read again."]

print("\n--- Your Story ---")
print(story)
print(random.choice(fun_endings))
