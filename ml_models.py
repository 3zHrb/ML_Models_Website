## importing classification machine learning models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
import xgboost as xgb

## importing regression machine learning models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor

## importing cross validation
from sklearn.model_selection import cross_val_score, KFold



def models(modelType: str):
    classificationModels = {
        "DecisionTreeClassifier": DecisionTreeClassifier(),
        "RandomForestClassifier": RandomForestClassifier(),
        "KNeighborsClassifier": KNeighborsClassifier(),
        "SVC": SVC(),
        "GaussianNB": GaussianNB(),
        "GradientBoostingClassifier": GradientBoostingClassifier(),
        "AdaBoostClassifier": AdaBoostClassifier(),
    }

    regressionModels = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "ElasticNet": ElasticNet(),
        "DecisionTreeRegressor": DecisionTreeRegressor(),
        "RandomForestRegressor": RandomForestRegressor(),
        "GradientBoostingRegressor": GradientBoostingRegressor(),
        "SVR": SVR(),
        "KNeighborsRegressor": KNeighborsRegressor(),
        "GaussianProcessRegressor": GaussianProcessRegressor(),
    }

    if modelType == "Classification":
        return classificationModels
    else:
        return regressionModels
