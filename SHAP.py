import shap

# 1. Initialize explainer (TreeExplainer is fast for tree-based models like XGBoost/RandomForest)
explainer = shap.TreeExplainer(model)

# 2. Compute SHAP values
shap_values = explainer(X_test)

# 3. Plot a single prediction (waterfall or force plot)
shap.plots.waterfall(shap_values[0])

# 4. Plot global feature importance (beeswarm plot)
shap.plots.beeswarm(shap_values)
