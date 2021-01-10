import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


if __name__ == '__main__':
    mobile_specs = pd.read_csv('mobile_price_1.csv', index_col='id')  # explicitly define column as index
    # res_list = list()
    # dpi_list = list()
    # ratio_list = list()
    # for index, row in mobile_specs.iterrows():
    #     res_list.append(str(row["px_width"]) + ' X ' + str(row["px_height"]))
    #     if(row["sc_w"]!=0):
    #         tmp_dpi = (row["px_width"]/row["sc_w"]/2.54)
    #         dpi_list.append(tmp_dpi)
    #     else:
    #         dpi_list.append(0)
    #     ratio_list.append(row["battery_power"]/row["talk_time"])
    mobile_specs['resolution'] = mobile_specs["px_width"] * mobile_specs["px_height"]
    mobile_specs['DPI_w'] = (mobile_specs["px_width"] / mobile_specs["sc_w"]/ 2.54)
    mobile_specs['call_ratio'] = mobile_specs["battery_power"]/mobile_specs["talk_time"]
    mobile_specs['memory'] = mobile_specs['memory'] / 1024
    # mobile_specs["resolution"] = res_list
    # mobile_specs["DPI_w"] = dpi_list
    # mobile_specs["call_ratio"] = ratio_list
    # mobile_specs[["resolution", "px_height", "px_width","DPI_w"]]
    print(mobile_specs[["resolution","px_height", "px_width","sc_w","DPI_w","battery_power","talk_time","call_ratio"]])
    # print(mobile_specs[["memory"]])
    print(mobile_specs.describe())
    mobile_specs.hist(column="price")
    plt.show()