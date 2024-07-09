import os
import outlines
from dotenv import load_dotenv
load_dotenv()
from enum import Enum
from pydantic import BaseModel, constr, conint
# Load model directly
from outlines import models
import llama_cpp

class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: conint(gt=18, lt=99)
    armor: Armor
    strength: conint(gt=1, lt=100)


model = models.llamacpp("TheBloke/Mistral-7B-Instruct-v0.2-GGUF", "mistral-7b-instruct-v0.2.Q5_K_M.gguf",
                        tokenizer=llama_cpp.llama_tokenizer.LlamaHFTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2"))
print('load generator')
generator = outlines.generate.choice(model, ["Blue", "Red", "Yellow"])

color = generator("What is the closest color to Indigo? ")
print(color)