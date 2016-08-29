# Fine Food Reviews
### Predecir el puntaje de los reviews en función de sus datos

El objetivo de esta competencia es predecir la cantidad de estrellas de un review en base a los datos del mismo. En general debería ser suficiente usar los campos de texto para poder predecir la valoración de cada review. La valoración es una cantidad de estrellas entre 1 y 5, 1 es el mínimo y 5 el máximo y se aceptan valores no-enteros, por ejemplo 3.14

### File descriptions

* **train.csv** - the training set
* **test.csv** - the test set
* **sampleSubmission.csv** - a sample submission file in the correct format

### Data fields

* **Id** - El id que identifica a cada review
* **ProductId** - El Id del producto
* **UserId** - El Id del usuario
* **ProfileName** - El nombre del usuario 
* **HelpfulnessNumerator** - El numerador indicando la cantidad de usuarios que juzgaron al review como util
* **HelpfulnessDenominator** - El denominador indicando la cantidad de usuarios que evaluaron si el review fue útil o no
* **Prediction** - La cantidad de estrellas del review
* **Time** - Un timestamp para el review
* **Summary** - Un resumen del review
* **Text** - Texto del review

### Setup

* Python 3
* `pip install requirements.txt`
* Download the data from the contest [site](https://inclass.kaggle.com/c/fine-food-reviews)

### Team

* [Agustina Barbetta](https://github.com/abrden)
* [Chano](http://bit.ly/2buPwCG)
* [Manuel Porto](https://github.com/manuporto)
* [Santiago Lazzari](https://github.com/SantiagoLazzari)


