import json
import greenhouse_clock

meta = {}

# Timestamp for files
meta["timestr"] = greenhouse_clock.get_time()


def report_performance(y_true, y_score, path, suffix=""):
    """

    We suggest using `sklearn.metrics.classification_report`

    References
    ----------
    https://scikit-learn.org/stable/modules/generated/
    sklearn.metrics.classification_report.html
    """

    # Plug-in here your performance metrics as dictionary entries
    meta["performance_metric_name"] = 0

    filename = "{0}metadata{1}.json".format(path, suffix)

    # Export to JSON
    with open(filename, "w") as fp:
        json.dump(meta, fp, indent=4)

    pass
