# import unittest
#
# class testInputs(word):
#     def test_spell(word):
#         if word in words:
#             return True
#         else:
#             print("Wrong spelling.")

blank ='''It was Thanksgiving, and the scent of succulent roast _______
wafted through my house. "_______, it's time to _______!"
my mother called. I couldn't wait to get my _______
on that _______ Thanksgiving meal.'''
print (blank)

noun = test_str(raw_input('Enter a noun: '))
person_in_room = test_str(raw_input('Enter the name of a person in the room: '))
verb = test_str(raw_input('Enter a verb: '))
part_of_body_plural = test_str(raw_input('Enter part of the body (plural): '))
adjective = test_str(raw_input('Enter an adjective: '))

list = [noun, person_in_room, verb, part_of_body_plural, adjective]

# def spellCheck(list_words):
#     for item in list_words:
#         testInputs(item)

def test_str(prompt):
    try:
        string = str(prompt)    
        return True
    except ValueError:
        print("Not a string!")
        return False

story = '''It was Thanksgiving, and the scent of succulent roast {}
wafted through my house. "{}, it's time to {}!"
my mother called. I couldn't wait to get my {}
on that {} Thanksgiving meal.'''.format(noun, person_in_room, verb, part_of_body_plural, adjective)

# spellCheck(list)
print(story)
