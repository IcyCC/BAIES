# -*-coding:utf-8-*-
"""
对每个数据表类选择进行表的新建、删除、清空、重建功能的脚本
由于每次运行要处理的数据表都可能不同，所以本脚本经常发生变动
"""

import sys

from BAIES import app
from app.model.quantify.socioeconomic import CountryProfiles,PopulationProfiles
from uf.operation.table_operator import delete_db_tables, create_db_tables, empty_db_tables

def list2str(l):
    return "\n".join(l)

table_list = [CountryProfiles, PopulationProfiles]
OPERATION = {"-rb": "REBUILD",
             "-rebuild": "REBUILD",
             "-del": "DELETE",
             "-new": "CREATE",
             "-empty": "EMPTY"}


if __name__ == '__main__':
    print(app.config["CONFIG_NAME"])
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    ctx = app.app_context()
    ctx.push()

    if len(sys.argv) > 1:
        print("Tables below will be", OPERATION[sys.argv[1]] + "-ed:")
        print("\t", list2str(table_list))

        flag = input("Be sure to operate? (Y/N)")
        if flag != "Y" and flag != "y":
            print("Safety is the highest priority!")
            exit()
        else:
            print("Operate Now!")

        if '-rb' in sys.argv or '-rebuild' in sys.argv:
            delete_db_tables(table_list)
            create_db_tables(table_list)
            exit()

        if '-del' in sys.argv:
            delete_db_tables(table_list)
            exit()

        if '-new' in sys.argv:
            create_db_tables(table_list)
            exit()

        if '-empty' in sys.argv:
            empty_db_tables(table_list)
            exit()