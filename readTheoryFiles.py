import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_table("/Users/stephaniekwan/Dropbox/Princeton_G6/hToA1A2/fromTheorists/BP1.tsv",index_col=0)

# plt.rcParams.update({
#     "text.usetex": True
# })

# for col in df.columns:
#     print(col)

# To access all the rows with a specific condition/cut

## Asymmetric case
print("Asymmetric case...")
# 9 points with m_1 = 15 GeV, 7 points with m_1 = 20 GeV, 4 points with m_1 = 30 GeV
array_mH1_mH2 = [  
    (15, 40),
    (15, 50),
    (15, 60),
    (15, 70),
    (15, 80),
    (15, 90),
    (15, 100),
    (15, 110),
    (20, 40), 
    (20, 50),
    (20, 60),
    (20, 70),
    (20, 80),
    (20, 90),
    (20, 100),
    (30, 60),
    (30, 70),
    (30, 80),
    (30, 90),
]

br_values = []
xs_ggh_values = []

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

    br_values.append(b_H3_H1H2_cascade_4b2tau)
    xs_ggh_values.append(x_H3_gg * b_H3_H1H2_cascade_4b2tau)

print(br_values)

## Branching fraction 
# First 9 values are m_1 = 15 GeV
fig, ax = plt.subplots()

# Add grid
plt.grid(axis='both', color='0.95')
ax.plot([item[1] for item in array_mH1_mH2[0:8]], br_values[0:8], 'o-', label='$m_{1} = 15$ GeV')
ax.plot([item[1] for item in array_mH1_mH2[9:15]], br_values[9:15], 'o-', label='$m_{1} = 20$ GeV')
ax.plot([item[1] for item in array_mH1_mH2[16:19]], br_values[16:19], 'o-', label='$m_{1} = 20$ GeV')

ax.set_xlabel("Mass of $m_{2}$ (GeV)")
ax.set_ylabel("Branching fraction B(h $\\rightarrow a_1 a_2 \\rightarrow 3a_1 \\rightarrow 4b2\\tau$)")

plt.title("Branching fraction of $h_{125}$ cascade decay to $4b2\\tau$")

plt.legend()
plt.tight_layout()
plt.savefig("example_br.pdf")

## Branching fraction 
# First 9 values are m_1 = 15 GeV
fig, ax = plt.subplots()

# Add grid
plt.grid(axis='both', color='0.95')
ax.plot([item[1] for item in array_mH1_mH2[0:8]], xs_ggh_values[0:8], 'o-', label='$m_{1} = 15$ GeV')
ax.plot([item[1] for item in array_mH1_mH2[9:15]], xs_ggh_values[9:15], 'o-', label='$m_{1} = 20$ GeV')
ax.plot([item[1] for item in array_mH1_mH2[16:19]], xs_ggh_values[16:19], 'o-', label='$m_{1} = 30$ GeV')

ax.set_xlabel("Mass of $m_{2}$ (GeV)")
ax.set_ylabel("$\sigma$ of ggH $h_{125}$ cascade decay to $4b2\\tau$ (pb)")

plt.title("$\sigma$ of $h_{125}$ cascade decay to $4b2\\tau$, assuming SM ggH production")

plt.legend()
plt.tight_layout()
plt.savefig("example_ggh_xsec.pdf")