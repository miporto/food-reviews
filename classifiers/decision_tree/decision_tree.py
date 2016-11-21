import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import grid_search
from sklearn.model_selection import cross_val_score

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


def train_tree(df):
    features = list(df.columns[2:])
    Y = df["Prediction"]
    X = df[features]
    dt = DecisionTreeClassifier()
    dt.fit(X, Y)
    return dt

df = pd.read_csv("../../data/trainvec.csv", nrows=10000)
dt = train_tree(df)
# Persist tree
pickle.dump(dt, open('tree.p', 'wb'))
features = list(df.columns[2:])
Y = df["Prediction"]
X = df[features] 
scores = cross_val_score(dt, X, Y, cv=5)
print(scores)
#dt2 = pickle.load(open('tree.p', 'rb'))

#test = np.array(X.values.tolist()[0]).reshape(1,-1)
df_test = pd.read_csv("../../data/testvec.csv", nrows=10)
test = df_test[list(df_test.columns[1:])]
print(dt.predict(test))
#visualize_tree(dt, features)


#parameters = {'max_depth':range(1,20)}
#clf = grid_search.GridSearchCV(DecisionTreeClassifier(), parameters, n_jobs=4)
#clf.fit(X, Y)
#tree_model = clf.best_estimator_
#print (clf.best_score_, clf.best_params_) 
