import pandas as pd
from NFETC2018 import config


def transform(types, mapping):
    res = [mapping[t] for t in types.split() if t in mapping]
    if len(res) == 0:
        print(types)
    return " ".join(res)

if __name__ == "__main__":
    mapping = {}
    infile = open(config.WIKI_MAPPING)
    for line in infile.readlines():
        a, b = line.strip().split()
        mapping[a] = b

    df_all = pd.read_csv(config.tWIKI_ALL, sep="\t", names=["p1", "p2", "text", "type", "f"])
    df_train = pd.read_csv(config.tWIKI_TRAIN, sep="\t", names=["p1", "p2", "text", "type", "f"])
    df_valid = pd.read_csv(config.tWIKI_VALID, sep="\t", names=["p1", "p2", "text", "type", "f"])
    df_test = pd.read_csv(config.tWIKI_TEST, sep="\t", names=["p1", "p2", "text", "type", "f"])

    df_all["type"] = df_all["type"].map(lambda x: transform(x, mapping))
    df_train["type"] = df_train["type"].map(lambda x: transform(x, mapping))
    df_valid["type"] = df_valid["type"].map(lambda x: transform(x, mapping))
    df_test["type"] = df_test["type"].map(lambda x: transform(x, mapping))

    df_all.to_csv(config.tWIKI_ALL, sep="\t", index=False, header=False)
    df_train.to_csv(config.tWIKI_TRAIN, sep="\t", index=False, header=False)
    df_valid.to_csv(config.tWIKI_VALID, sep="\t", index=False, header=False)
    df_test.to_csv(config.tWIKI_TEST, sep="\t", index=False, header=False)
