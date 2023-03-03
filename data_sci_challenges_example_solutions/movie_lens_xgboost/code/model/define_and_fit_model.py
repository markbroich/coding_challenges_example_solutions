'''define_and_fit_model'''

from xgboost import XGBRanker


def define_and_fit_model(X_train, y_train, query_list_train, X_test, y_test, query_list_test, n_estimators=100, learning_rate=0.1):
    model = XGBRanker(objective='rank:ndcg', eval_metric='ndcg', n_estimators=n_estimators, random_state=0, learning_rate=learning_rate)
    model.fit(
        X_train,
        y_train,
        group=query_list_train,
        eval_set=[(X_test, y_test)],
        eval_group=[list(query_list_test)],
        verbose=True
    )
    return model

# background on 'ndcg'
# https://towardsdatascience.com/how-to-evaluate-learning-to-rank-models-d12cadb99d47