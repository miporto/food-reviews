import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")

HTABLE_DIM = 127
features = ['Id', 'Prediction'] + list(range(HTABLE_DIM))
df = pd.read_csv("../../data/trainvec.csv", names=features, nrows=50)
features = list(df.columns[2:])
#print(features)
Y = df["Prediction"]
X = df[features]
#print(len(df.columns))
#print(Y[:3])
#print(X[0][0:10])
dt = DecisionTreeClassifier()
dt.fit(X, Y)
visualize_tree(dt, features)
