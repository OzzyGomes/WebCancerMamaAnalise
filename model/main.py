import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def get_clean_data():
    data = pd.read_csv('../data/data.csv')
    
    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({ 'M': 1, 'B': 0})
    return data

def creat_model(data):
    #train and test data
    X = data.loc[:, data.columns != 'diagnosis']
    Y = data['diagnosis']

    #scale the data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    #split the data
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    #traning data
    model = LogisticRegression()
    model.fit(x_train, y_train)

    return model, scaler
     
def main():
    data = get_clean_data()
    
    model, scaler = creat_model(data)

    

if __name__ == '__main__':
    main()
