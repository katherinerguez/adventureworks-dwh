
def clean_schema(spark, schema):
    if spark.catalog.databaseExists(schema):

        for t in spark.catalog.listTables(schema):
            spark.sql(f"DROP TABLE IF EXISTS {schema}.{t.name}")

        spark.sql(f"DROP DATABASE {schema}")

    spark.sql(f"CREATE DATABASE {schema}")