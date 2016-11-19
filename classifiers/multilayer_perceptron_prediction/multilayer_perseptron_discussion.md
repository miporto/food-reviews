## Multilayer perceptron discussion

#### MLPClassifier

[Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier)

```python
from sklearn.neural_network import MLPClassifier

X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X, y)
```

#### Persitence

[Documentation](http://scikit-learn.org/stable/modules/model_persistence.html)

```python
from sklearn.externals import joblib

joblib.dump(clf, 'filename.pkl')
clf = joblib.load('filename.pkl')
```
