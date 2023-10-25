import xgboost as xgb
from hyperopt import fmin, tpe, hp, Trials, STATUS_OK, space_eval
from sklearn.metrics import mean_absolute_error

class BayesianOptimization:
    def __init__(self, x_train, y_train, x_valid, y_valid, space):
        self.x_train = x_train
        self.y_train = y_train
        self.x_valid = x_valid
        self.y_valid = y_valid
        self.space = space
        self.trials = Trials()

    def objective(self, params):
        model = xgb.XGBRegressor(**params)
        model.fit(self.x_train, self.y_train, eval_set=[(self.x_valid, self.y_valid)], early_stopping_rounds=50, verbose=False)
        pred = model.predict(self.x_valid)
        mae = mean_absolute_error(self.y_valid, pred)
        return {'loss': mae, 'status': STATUS_OK}

    def optimize(self, n_evals=100):
        best = fmin(fn=self.objective,
                    space=self.space,
                    algo=tpe.suggest,
                    max_evals=n_evals,
                    trials=self.trials)
        return best

    def get_best_params(self):
        return space_eval(self.space, self.trials.argmin)
