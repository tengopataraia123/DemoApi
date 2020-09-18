from nltk.tokenize import sent_tokenize, word_tokenize

example_text="Musk has stated that he does not believe the U.S. government should provide subsidies to companies but should instead use a carbon tax to price in the negative externality of climate change and discourage poor behavior. Musk says that the free market would achieve the best solution, and that producing environmentally unfriendly vehicles should come with its own consequences."


for i in sent_tokenize(example_text):
    print(i)





