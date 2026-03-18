import dagster as dg
from adventureworks_orchestration.resources.mysql_resource import MySQLResource
from adventureworks_orchestration.constants import *
from pyspark.sql import DataFrame
from typing import Iterator
from .setup import clean_bronze_layer

aw_tables = ["Shift","EmployeeDepartmentHistory","EmployeePayHistory"]

def get_bronze_aw_table_asset(table: str):
    @dg.asset(
        ins={
            "source" : dg.AssetIn(key=[ASSET_GROUP_LANDING, AW_HR_FILES_PREFIX, table.lower()]) 
        },
        io_manager_key="s3_iceberg_io_manager",
        deps=[clean_bronze_layer],
        key=[ASSET_GROUP_BRONZE, f"hr_{table.lower()}"],
        group_name=ASSET_GROUP_BRONZE,
    )
    def _asset(context: dg.AssetExecutionContext, source: DataFrame):
        return dg.Output(value=source)

    return _asset

def get_bronze_aw_assets():
    activos = []
    for tabla in aw_tables:
        activo = get_bronze_aw_table_asset(tabla)
        activos.append(activo)
    return activos


ASSETS = get_bronze_aw_assets()