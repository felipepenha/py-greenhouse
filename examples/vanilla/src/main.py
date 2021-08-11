import greenhouse_clock
import data_sourcing
import data_splitting
import data_preprocessing
import feature_engineering
from modeling import model
import performance_monitoring

start_time = greenhouse_clock.get_time()

if __name__ == "__main__":

    # Run prefect flow
    df = data_sourcing.get()
    df = data_preprocessing.clean(df)
    df = data_preprocessing.normalize(df)

    train, valid, test = data_splitting.split(df)

    (
        train["x"],
        valid["x"],
        test["x"],
    ) = feature_engineering.numerical_missing_imputation(
        train=train, valid=valid, test=test, cols=["x"], imputation_method="median"
    )

    m = model().fit(train=train, y_col="y", x_col="x")

    train["pred"], valid["pred"], test["pred"] = m.transform_sets(train, valid, test)

    performance_monitoring.report_performance(
        y_true=valid["y"],
        y_score=valid["pred"],
        path="/usr/app/monitor/",
        suffix="_valid",
    )
