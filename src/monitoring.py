import pandas_profiling


def export(df, path):

    profile = pandas_profiling.ProfileReport(df, title="Pandas Profiling Report")

    profile.to_file(path)

    pass
