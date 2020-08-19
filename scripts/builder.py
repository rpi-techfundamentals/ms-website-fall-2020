import yaml
import pandas as pd
import subprocess
from tabulate import tabulate
DATE='Date'



def load_yaml_file(file):
    """
    Loads a yaml file from file system.
    @param file Path to file to be loaded.
    """
    try:
        with open( file ) as f:
            cf = yaml.safe_load(f)
        return cf
    except subprocess.CalledProcessError as e:
        print("error")
        return(e.output.decode("utf-8"))

def update_yaml_file(file, data):
    """
    Updates a yaml file.
    @param kwargs dictionary.
    """
    print("Updating the file: " + file)
    try:
        with open(file, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

    except subprocess.CalledProcessError as e:
        print("error: " + e)

def pandas_to_md(df, file, title):
    if DATE in df.columns:
        if pd.core.dtypes.common.is_datetime_or_timedelta_dtype(df[DATE]):
            print("Converting datetime to ")
            df[DATE]=df[DATE].dt.strftime('%m/%d')
    s = title
    separator = "\n============================\n\n"
    #table=df.to_markdown(tablefmt="grid")
    table=tabulate(df, tablefmt="pipe", headers="keys")
    output= s+separator+table
    print("Outputting file:", file)
    with open(file, "w") as text_file:
        text_file.write(output)
    return output

def write_md_file(filename, df):
    print("Updating the file: " + filename)
    df.to_csv(filename,  index=None, sep=' ',quoting = csv.QUOTE_NONE, escapechar = ' ')
