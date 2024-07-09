from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
#model_id = "databricks/dolly-v2-3b"
model_id = "google/gemma-2b-it"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id,
                                             device_map="cpu",
                                            torch_dtype=torch.bfloat16)
