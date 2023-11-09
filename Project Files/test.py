import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv(
    'E:\College stuff\Break work\AI ML\Project\FlaskProject\car_data.csv')
df['Gender'].replace(['Male', 'Female'],
                     [0, 1], inplace=True)
x_train, x_test, y_train, y_test = train_test_split(df.drop(
    ['Purchased', 'User ID'], axis=1), df['Purchased'], test_size=0.3, random_state=909)
DT_model = DecisionTreeClassifier(random_state=192)
DT_model.fit(x_train, y_train)
pickle.dump(DT_model, open(
    "E:\College stuff\Break work\AI ML\Project\FlaskProject\model.pkl", "wb"))
