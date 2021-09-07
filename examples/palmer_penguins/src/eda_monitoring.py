import pandas_profiling


def export_eda_report(df, path, preffix, suffix):

    profile = pandas_profiling.ProfileReport(df, title="Pandas Profiling Report")

    path = "{}/{}_ead_monitoring_{}.html".format(path, preffix, suffix)

    profile.to_file(path)

    pass
