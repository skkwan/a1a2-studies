import pandas as pd
import matplotlib as plt
df = pd.read_table("/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/fromTheorists/BP1.tsv",index_col=0)

# for col in df.columns:
#     print(col)

# To access all the rows with a specific condition/cut

## Asymmetric case
print("Asymmetric case...")
array_mH1_mH2 = [(15, 100)]

for massPointPair in array_mH1_mH2:
    (value_mH1, value_mH2) = massPointPair
    print("mH1: {}, mH2: {}".format(value_mH1, value_mH2))

    myMassPoint = df.loc[(df["mH2"] == value_mH2) & (df["mH1"] == value_mH1)]

    # Get the xs and branching ratios we want
    x_H3_gg   = myMassPoint["x_H3_gg"].item()
    print("Read the values: x_H3_gg: {}".format(x_H3_gg))
    b_H3_H1H1 = myMassPoint["b_H3_H1H1"].item()
    print("Read the values: b_H3_H1H1: {}".format(b_H3_H1H1))
    b_H3_H1H2 = myMassPoint["b_H3_H1H2"].item()
    print("Read the values: b_H3_H1H2: {}".format(b_H3_H1H2))
    b_H3_H2H2 = myMassPoint["b_H3_H2H2"].item()
    print("Read the values: b_H3_H2H2: {}".format(b_H3_H2H2))
    b_H2_H1H1 = myMassPoint["b_H2_H1H1"].item()
    print("Read the values: b_H2_H1H1: {}".format(b_H2_H1H1))


    b_H1_bb = myMassPoint["b_H1_bb"].item()
    print("Read the values: b_H1_bb: {}".format(b_H1_bb))

    b_H1_tautau = myMassPoint["b_H1_tautau"].item()
    print("Read the values: b_H1_tautau: {}".format(b_H1_tautau))


    b_H3_H1H2_cascade_4b2tau = b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_bb * b_H1_bb) * b_H1_tautau
    b_H3_H1H2_cascade_2b4tau = b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_tautau * b_H1_tautau) * b_H1_bb

    print("\t BR(h3->h1h2->cascade->4b2tau), calculated as B(h3 -> h1 h2) * B(h2 -> h1h1) * 3*(h1->bb * h1->bb) * (h1->tautau): {}".format(b_H3_H1H2_cascade_4b2tau))
    print("\t BR(h3->h1h2->cascade->2b4tau), calculated as B(h3 -> h1 h2) * B(h2 -> h1h1) * 3*(h1->tautau * h1->tautau) * (h1->bb): {}".format(b_H3_H1H2_cascade_2b4tau))

    print("xs of ggH H3 -> H1H2 -> cascade -> 4b2tau: {}".format(x_H3_gg * b_H3_H1H2_cascade_4b2tau))

    print("xs of ggH H3 -> H1H2 -> cascade -> 2b4tau: {}".format(x_H3_gg * b_H3_H1H2_cascade_2b4tau))

