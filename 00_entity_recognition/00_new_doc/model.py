<<<<<<< HEAD
import os
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

class Model:
    def __init__(self, model_name:str="bert-base-uncased", model_dir:str=None, model=None, tokenizer=None):
        self.model_name=model_name
        self.model_dir=model_dir
        self.model=model 
        self.tokenizer=tokenizer

    def create_model_dir(self):
        """create directory for our model

        Args:
            model_name (_type_): _description_
        """
        self.model_dir = "models/" + self.model_name
        os.makedirs(self.model_dir, exist_ok=True)
        return self.model_dir

    def charge_model(self):
        """charge our model and tokenizer in the appropriate dir, do it only one per model 

        Args:
            model_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.create_model_dir()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(self.model_name)
        self.tokenizer.save_pretrained(self.model_dir)
        self.model.save_pretrained(self.model_dir)

        return f'model dir : {self.model_dir}, tokenizer: {self.tokenizer}, model: {self.model}'
    





# class config:
#     MAX_LEN = 128
#     TRAIN_BATCH_SIZE = 32
#     VALID_BATCH_SIZE = 8
#     EPOCHS = 3
#     BASE_MODEL_PATH = "../input/bert-base-uncased/"
#     MODEL_PATH = "model.bin"
#     TRAINING_FILE = "../input/entity-annotated-corpus/ner_dataset.csv"
#     TOKENIZER = transformers.BertTokenizer.from_pretrained(
#         BASE_MODEL_PATH,
#         do_lower_case=True
=======
import os
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

class Model:
    def __init__(self, model_name:str="bert-base-uncased", model_dir:str=None, model=None, tokenizer=None):
        self.model_name=model_name
        self.model_dir=model_dir
        self.model=model 
        self.tokenizer=tokenizer

    def create_model_dir(self):
        """create directory for our model

        Args:
            model_name (_type_): _description_
        """
        self.model_dir = "models/" + self.model_name
        os.makedirs(self.model_dir, exist_ok=True)
        return self.model_dir

    def charge_model(self):
        """charge our model and tokenizer in the appropriate dir, do it only one per model 

        Args:
            model_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.create_model_dir()
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForMaskedLM.from_pretrained(self.model_name)
        self.tokenizer.save_pretrained(self.model_dir)
        self.model.save_pretrained(self.model_dir)

        return f'model dir : {self.model_dir}, tokenizer: {self.tokenizer}, model: {self.model}'
    





# class config:
#     MAX_LEN = 128
#     TRAIN_BATCH_SIZE = 32
#     VALID_BATCH_SIZE = 8
#     EPOCHS = 3
#     BASE_MODEL_PATH = "../input/bert-base-uncased/"
#     MODEL_PATH = "model.bin"
#     TRAINING_FILE = "../input/entity-annotated-corpus/ner_dataset.csv"
#     TOKENIZER = transformers.BertTokenizer.from_pretrained(
#         BASE_MODEL_PATH,
#         do_lower_case=True
>>>>>>> 0f64690af03ca4633cc152e3237766b7451a88fc
#     )