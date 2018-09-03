import unittest
# def ask_input():
# random.coice(input_list)

class testInputs():
    def test_word(input):
        if integer in input:
            print("Invalid input!")
        else:
            return True

    # def test_noun():

noun = str(input('Enter a noun: '))
person_in_room = str(input('Enter the name of a person in the room: '))
verb = str(input('Enter a verb: '))
part_of_body_plural = str(input('Enter part of the body (plural): '))
adjective = str(input('Enter an adjective: '))

story = '''It was Thanksgiving, and the scent of succulent roast {}
wafted through my house. "{}, it's time to {}!"
my mother called. I couldn't wait to get my {}
on that {} Thanksgiving meal.'''.format(noun, person_in_room, verb, part_of_body_plural, adjective)


print(story)
