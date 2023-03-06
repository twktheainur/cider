# demo script for running CIDEr

import json
from pathlib import Path

import pickle
import sys


input = Path(sys.argv[1])
with open(input,"r") as f:
    lines = f.readlines()
ref_list_dict = []
pred_list_dict = []

for id,line in enumerate(lines):
    rp = line.replace("\n","").split(',')
    refs  = rp[1:]
    pred = rp[0]
    pred_list_dict.append({"image_id": id, "caption": pred})
    for i in range(len(refs)):
     ref_list_dict.append({"image_id": id, "caption": refs[i]})


with open(Path("results", input.stem+"_refs.json"),"w") as f:
    json.dump(ref_list_dict,fp=f)

with open(Path("results", input.stem+"_pred.json"),"w") as f:
    json.dump(pred_list_dict,fp=f)

# from pydataformat.loadData import LoadData
# import pdb
# import json
# from pyciderevalcap.eval import CIDErEvalCap as ciderEval
# from pyciderevalcap.tokenizer.ptbtokenizer import PTBTokenizer
# tokenizer = PTBTokenizer()
# pathToData = 'data/'

# refName = 'results/refs.json'
# candName = 'results/pred.json'

# result_file = 'results.json'
# df_mode = 'kit-test-df'

# # load reference and candidate sentences
# loadDat = LoadData(pathToData)
# gts, res = loadDat.readJson(refName, candName)

# # calculate cider scores
# scorer = ciderEval(gts, res, df_mode)
# # scores: dict of list with key = metric and value = score given to each candidate
# scores = scorer.evaluate()

