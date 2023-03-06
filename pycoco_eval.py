# coding: utf-8

# In[1]:

# demo script for running CIDEr
import json
from pathlib import Path
import sys

from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap

param_path = sys.argv[1]

# load the configuration file
config = json.loads(open(param_path, 'r').read())
print(sys.argv)
refName = sys.argv[1] 
candName = sys.argv[2]
#resultFile = sys.argv[3]

# Print the parameters
print("Running Pycoco eval with the following settings")
print("*****************************")
print("Reference File:%s" % (refName))
print("Candidate File:%s" % (candName))
#print("Result File:%s" % (resultFile))
#print("IDF:%s" % (df_mode))
print("*****************************")

coco = COCO(refName)
coco_result = coco.loadRes(candName)

coco_eval = COCOEvalCap(coco, coco_result)

coco_eval.evaluate()

# print output evaluation scores
for metric, score in coco_eval.eval.items():
    print(f'{metric}: {score:.3f}')


# # scores['CIDEr'] contains CIDEr scores in a list for each candidate
# # scores['CIDErD'] contains CIDEr-D scores in a list for each candidate
# resultFile = Path(resultFile)
# with open(resultFile, 'w') as outfile:
#     json.dump(scores, outfile)
