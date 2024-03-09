# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        # Convert word to lowercase and sort its characters
        sorted_word = sorted(self.word)

        # Initialize a list to store matches
        matches = []

        # Iterate over each possible anagram
        for anagram in possible_anagrams:
            # Convert anagram to lowercase and sort its characters
            sorted_anagram = sorted(anagram.lower())

            # Check if the sorted characters of both words match
            if sorted_anagram == sorted_word:
                # If they match, add the anagram to matches list
                matches.append(anagram)

        return matches

# Example usage:
anagram = Anagram("listen")
possible_anagrams = ["enlists", "google", "inlets", "banana", "silent"]
print(anagram.match(possible_anagrams))  # Output: ['inlets', 'silent']
