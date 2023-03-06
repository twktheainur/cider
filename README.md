Consensus-based Image Description Evaluation (CIDEr Code)
===================

Evaluation code for CIDEr metric. Provides CIDEr as well as
CIDEr-D (CIDEr Defended) which is more robust to gaming effects.

## Important Note ##
CIDEr by default (with idf parameter set to "corpus" mode) computes IDF values using the reference sentences provided. Thus, CIDEr score for a reference dataset with only 1 image will be zero. When evaluating using one (or few) images, set idf to "coco-val-df" instead, which uses IDF from the MSCOCO Vaildation Dataset for reliable results.

## Requirements ##
- java 1.8.0
- python 2.7

## Convert CSV format to json ##
Running `python convert_csv_to_cider_format.py some_YYY.csv` will generate `some_YYYY_pred.json` and `some_YYY_refs.json`

## Running the scorer ##

To compute the results, please run: 

`python cidereval.py some_YYY_refs.json some_YYYY_pred.json some_YYYY_results.json`

The mean results will be printed and additionally saved to `some_YYYY_results.json`.
