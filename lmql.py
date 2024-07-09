# argmax(verbose=True) 
# # review to be analyzed
# review = """We had a great stay. Hiking in the mountains 
#             was fabulous and the food is really good."""

# # use prompt statements to pass information to the model
# "Review: {review}"
# "Q: What is the underlying sentiment of this review and why?"
# # template variables like [ANALYSIS] are used to generate text
# "A:[ANALYSIS]" where not "\n" in ANALYSIS

# # use constrained variable to produce a classification
# "Based on this, the overall sentiment of the message\
#  can be considered to be[CLS]" where CLS in [" positive", " neutral", " negative"]

# CLS # positive

argmax(verbose=True)
"A list of things not to forget when going to the sea (not travelling): \n"
backpack = []
for i in range(5):
   "-[THING]" where STOPS_AT(THING, "\n") 
   backpack.append(THING.strip())

"The most essential of which is: [ESSENTIAL_THING].\n" \
    where ESSENTIAL_THING in backpack
from lmql.model("llama.cpp:/Users/dinhtungtp/github_projects/epam-llm/notebook/mistral-7b-instruct-v0.2.Q4_K_M.gguf", 
                tokenizer="mistralai/Mistral-7B-Instruct-v0.2")


# sample(temperature=0.8)
#    "A list of things not to forget when going to the sea (not travelling): \n"
#    "- Sunglasses \n"
#    for i in range(4):
#       "- [THING] \n"
# where
#    THING in set(["Volleyball", "Sunscreen", "Bathing Suite"])


         
         
# # generates an arithmetic expression
# "A simple math problem for addition (without solution, \
#     without words): [MATH]" where STOPS_BEFORE(MATH, "=")

# # evaluate the expression and feed it back into the prompt
# "= {eval(MATH.strip())}"

# argmax "What is the capital of France? [ANSWER]" from "gpt2"\
#     where len(TOKENS(ANSWER)) < 10