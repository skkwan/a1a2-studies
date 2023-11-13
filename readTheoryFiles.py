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
    b_H3_H1H1 = myMassPoint["b_H3_H1H1"].item()
    b_H3_H1H2 = myMassPoint["b_H3_H1H2"].item()
    b_H3_H2H2 = myMassPoint["b_H3_H2H2"].item()
    b_H2_H1H1 = myMassPoint["b_H2_H1H1"].item()

    b_H1_bb = myMassPoint["b_H1_bb"].item()
    b_H1_tautau = myMassPoint["b_H1_tautau"].item()

    print("Read the values: x_H3_gg: {}, b_H3_H1H2: {} \n b_H2_H1H1: {} \n b_H1_bb: {} \n b_H1_tautau: {}".format(x_H3_gg, b_H3_H1H2, b_H2_H1H1, b_H1_bb, b_H1_tautau))

    x_4b2tau = b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_bb * b_H1_bb) * b_H1_tautau
    x_2b4tau = b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_tautau * b_H1_tautau) * b_H1_bb

    print("xs of 4b2tau: {} \n xs of 2b4tau: {}".format(x_4b2tau, x_2b4tau))

    print("xs of H3 -> H1H2 -> 3H1 {}".format(x_H3_gg * b_H3_H1H2 * b_H2_H1H1))

    print("b_H3_H1H1: {}, b_H3_H1H2 {}, b_H3_H2H2 {}".format(b_H3_H1H1, b_H3_H1H2, b_H3_H2H2))

