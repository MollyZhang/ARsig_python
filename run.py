"""
AR signature in python
converted from Artem Sokolov and Vlado Uzunangelov's R code
"""
import pandas as pd




X = "filtered_mrna.tab"
y = "all_class_labels"

def main():
    X = pd.read_csv("data/AR_sig_celline.tab", delimiter="\t")
    Y = pd.read_csv("data/ar_cell_line_clin.txt", delimiter="\t")
    print(Y.shape)
    print(Y.columns)

    



if __name__ == "__main__":
    main()
