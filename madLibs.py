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

noun = str(input('Enter a noun: '))
person_in_room = str(input('Enter the name of a person in the room: '))
verb = str(input('Enter a verb: '))
part_of_body_plural = str(input('Enter part of the body (plural): '))
adjective = str(input('Enter an adjective: '))

list = [noun, person_in_room, verb, part_of_body_plural, adjective]

# def spellCheck(list_words):
#     for item in list_words:
#         testInputs(item)

story = '''It was Thanksgiving, and the scent of succulent roast {}
wafted through my house. "{}, it's time to {}!"
my mother called. I couldn't wait to get my {}
on that {} Thanksgiving meal.'''.format(noun, person_in_room, verb, part_of_body_plural, adjective)

# spellCheck(list)
print(story)
