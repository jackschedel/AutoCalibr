
from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

paths = [str(x) for x in Path("../trainingSet/ply").glob("**/*.ply")]

tokenizer.train(paths, trainer)

tokenizer.save("../tokenizer/ply-tokenizer.json")