import pandas as pd

df = pd.read_table("/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/fromTheorists/BP1.tsv",index_col=0)

# for col in df.columns:
#     print(col)

# To access all the rows with a specific condition/cut

## Asymmetric case
print("Asymmetric case...")
myMassPoint = df.loc[(df["mH2"] == 80) & (df["mH1"] == 30)]

# Get the cross sections we want
x_H3_gg   = myMassPoint["b_H3_gg"].item()
b_H3_H1H2 = myMassPoint["b_H3_H1H2"].item()
b_H2_H1H1 = myMassPoint["b_H2_H1H1"].item()

b_H1_bb = myMassPoint["b_H1_bb"].item()
b_H1_tautau = myMassPoint["b_H1_tautau"].item()

print("Read the values: b_H3_H1H2: {} \n b_H2_H1H1: {} \n b_H1_bb: {} \n b_H1_tautau: {}".format(b_H3_H1H2, b_H2_H1H1, b_H1_bb, b_H1_tautau))

xs_4b2tau = x_H3_gg * b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_bb * b_H1_bb) * b_H1_tautau
xs_2b4tau = x_H3_gg * b_H3_H1H2 * b_H2_H1H1 * 3*(b_H1_tautau * b_H1_tautau) * b_H1_bb

print("xs of 4b2tau: {} \n xs of 2b4tau: {}".format(xs_4b2tau, xs_2b4tau))

print("xs of H3 -> H1H2 -> 3H1 {}".format(x_H3_gg * b_H3_H1H2 * b_H2_H1H1))

## Symmetric case for comparison
print("Symmetric case...")
myMassPoint = df.loc[(df["mH2"] == 45) & (df["mH1"] ==45)]
x_H3_gg   = myMassPoint["b_H3_gg"].item()
b_H3_H1H2 = myMassPoint["b_H3_H1H2"].item()
b_H1_bb = myMassPoint["b_H1_bb"].item()
b_H1_tautau = myMassPoint["b_H1_tautau"].item()

