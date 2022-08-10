import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def getModel():
    train_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='train')
    test_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/binary_classification/%E1%84%83%E1%85%A1%E1%86%BC%E1%84%82%E1%85%AD_%E1%84%8E%E1%85%AC%E1%84%8C%E1%85%A9%E1%86%BC_jvyrMwR.xlsx?raw=true', sheet_name='test')
    
    x1 = train_df.iloc[:,1:-1].to_numpy()
    y1 = train_df["당뇨여부"].to_numpy()
    x2 = test_df.iloc[:,1:-1].to_numpy()
    y2 = test_df["당뇨여부"].to_numpy()
    
    dclf = DecisionTreeClassifier()
    dclf.fit(x1,y1)
    return dclf