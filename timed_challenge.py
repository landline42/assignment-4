# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

"""
5. Unique Word Count
Count how many distinct words are in the collection.
Input: "one fish two fish red fish blue fish"
Output: 5
"""

class WordCounter:

    def __init__(self):
        self.punctuation_list = [",", ".", "?", "!", "(", ")", "'", "\""]
    
    def format_string(self, text):
        """ Formats the string to remove punctuation and capitalized words """
        
        #Remove punctuation
        for punctuation in self.punctuation_list:
            text = text.replace(punctuation, "")

        #Convert all text to lowercase to prevent the same words with different capitalizations from being counted as unique words
        text = text.lower()

        return text


    def count_words(self, text):
        """ Finds the word count of a string """
        
        #Check if the input is a string
        if type(text) != str:
            return "Error: input was not a string"
            
        #Check if the string is empty
        if len(text) == 0:
            return 0

        #Format the string
        formatted_text = self.format_string(text)

        #Convert the string into a set of words
        word_set = set(formatted_text.rsplit(" "))

        return len(word_set)


word_counter = WordCounter()

#Create sample strings and test the functions
sample = "one fish two fish red fish blue fish"
sample_with_capitals = "One Fish Two fish Red FISH Blue FiSh"
sample_with_punctuation = "one fish, \"two two fish! red 'fish blue fish."
empty_string = ""
not_a_string = 42

print("Input:", sample, "\nWord count:", word_counter.count_words(sample))
print("\nInput:", sample_with_capitals, "\nWord count:", word_counter.count_words(sample_with_capitals))
print("\nInput:", sample_with_punctuation, "\nWord count:", word_counter.count_words(sample_with_punctuation))
print("\nInput:", empty_string, "\nWord count:", word_counter.count_words(empty_string))
print("\nInput:", not_a_string, "\nWord count:", word_counter.count_words(not_a_string))