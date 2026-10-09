import lime
import lime.lime_tabular

# 1. Initialize the explainer
explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_train.values,
    feature_names=feature_columns,
    class_names=['Class 0', 'Class 1'],
    mode='classification',
)

# 2. Explain a single instance
exp = explainer.explain_instance(
    data_row=X_test.iloc[0].values,
    predict_fn=model.predict_proba,
    num_features=5,
)
exp.show_in_notebook()