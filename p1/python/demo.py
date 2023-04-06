import datetime as dt
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style

def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Data Analysis 1")
    print("\nProgram Requirements:"
          + "\n1. Run demo.py."
          + "\n2. If errors, more than likely missing installations."
          + "\n3. Test Python Package Installer: pip freeze."
          + "\n4. Research how to do the following installations: "
          + "\n\ta. pandas (only if missing)."
          + "\n\tb. pandas-datareader (only if missing)."
          + "\n\tc. matplotlib (only if missing)."
          + "\n5. Create at least three functions that are called by the program:"
          + "\n\ta. main(): calls at least two other functions."
          + "\n\tb. get_requirements(): displays the program requirements."
          + "\n\tc. data_analysis_1(): displays the following data.")
        
def data_analysis_1():
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()

    df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)

    print("\nPrint number of records: ")
    print(len(df.index))
    
    print("\nPrint columns: ")
    print(df.columns)

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first five lines:")
    print(df[:5])

    print("\nPrint last five lines: ")
    print(df[-5:])

    print("\nPrint first 2 lines: ")
    print(df[:2])

    print("\nPrint last 2 lines")
    print(df[-2:])

    style.use('ggplot')

    df['DJIA'].plot()
    df['SP500'].plot()
    plt.legend()
    plt.show()