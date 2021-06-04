import numpy as np
from sklearn import metrics
import json

import greenhouse_clock

meta = {}

# Timestamp for files
meta["timestr"] = greenhouse_clock.get_time()


def optimal_threshold(y_true, y_score):

    # Performance extracted from the "ROC curve"
    fpr, tpr, thr = metrics.roc_curve(
        y_true=y_true, y_score=y_score, pos_label=1, drop_intermediate=False
    )

    diff = np.abs(tpr - fpr)

    # Numpy index of the maximum separation between TPR and FPR
    diff_idx = np.argmax(diff)

    # Optimum threshold based on max diff criterium
    return thr[diff_idx]


def report_performance(
    y_true, y_score, best_hyperparams, path, opt_thr=0.5, suffix="_"
):
    """
    References
    ----------
    https://scikit-learn.org/stable/modules/generated/
    sklearn.metrics.classification_report.html
    """

    meta["optimal_hyperparameters"] = best_hyperparams

    meta["optimal_threshold"] = opt_thr

    # Performance extracted from the "ROC curve"
    fpr, tpr, thr = metrics.roc_curve(
        y_true=y_true, y_score=y_score, pos_label=1, drop_intermediate=False
    )

    meta["AUC"] = metrics.auc(fpr, tpr)

    diff = np.abs(tpr - fpr)

    # Maximum difference between TPR and FPR
    meta["max_diff_FPR_TPR"] = np.max(diff)

    # Numpy index of the maximum separation between TPR and FPR
    diff_idx = np.argmax(diff)

    # Update optimum threshold based on max diff criterium
    meta["threshold_from_max_diff"] = thr[diff_idx]

    # Predicted classes based on "optimal_threshold"
    y_pred = [int(k >= opt_thr) for k in y_score]

    meta["classification_report"] = metrics.classification_report(
        y_true=y_true, y_pred=y_pred, output_dict=True
    )

    filename = "{0}metadata{1}.json".format(path, suffix)

    # Export to JSON
    with open(filename, "w") as fp:
        json.dump(meta, fp, indent=4)

    pass
