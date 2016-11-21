import pandas as pd
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import grid_search
from sklearn.model_selection import cross_val_score

TEST_F = "../../data/testvec.csv"
TRAIN_F = "../../data/trainvec.csv"
PRED_F = "dtree.csv"
TREE_DUMP_F = "tree.p"

def visualize_tree(tree, feature_names):
    """
    Function from http://chrisstrelioff.ws/sandbox/2015/06/08/decision\
            _trees_in_python_with_scikit_learn_and_pandas.html
    Create tree png using graphviz.
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

def make_predictions(df, test_file_name, output_file):
    features = list(df.columns[2:])
    Y = df["Prediction"]
    X = df[features] 

    # In case you want to test only one sample
    #test = np.array(X.values.tolist()[0]).reshape(1,-1)
    
    df_test = pd.read_csv(test_file_name)
    test = df_test[list(df_test.columns[1:])]
    preds = dt.predict(test)
    df_preds = pd.DataFrame(preds, columns=["Prediction"])
    df_kaggle = pd.concat([df_test["Id"], df_preds["Prediction"]], axis=1, keys=["Id", "Prediction"])
    df_kaggle.to_csv(output_file, index=False)

df = pd.read_csv(TRAIN_F)
dt = train_tree(df)
# Persist tree
pickle.dump(dt, open(TREE_DUMP_F, "wb"))
# To restore the tree
#dt2 = pickle.load(open(TREE_DUMP_F, "rb"))

make_predictions(df, TEST_F, PRED_F)
visualize_tree(dt, features)

# Cross validation scores
#scores = cross_val_score(dt, X, Y, cv=5)
#print(scores)

# GridSearch for optimal parameters
#parameters = {'max_depth':range(1,20)}
#clf = grid_search.GridSearchCV(DecisionTreeClassifier(), parameters, n_jobs=4)
#clf.fit(X, Y)
#tree_model = clf.best_estimator_
#print (clf.best_score_, clf.best_params_) 
