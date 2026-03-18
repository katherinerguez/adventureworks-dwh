import dagster as dg
from .assets import sample,landing
from dagster_pyspark import pyspark_resource
from .resources.csv_io_manager import S3PartitionedCsvIOManager
import os
from .jobs import jobs, schedules
from .resources.mysql_resource import PySparkMySQLResource

@dg.definitions
def defs():
    sample_assets = dg.load_assets_from_package_module(sample)
    sample2 = dg.load_assets_from_package_module(landing)

    configured_pyspark = pyspark_resource.configured(
        {
            "spark_conf": {
                "spark.hadoop.fs.s3.impl": "org.apache.hadoop.fs.s3native.NativeS3FileSystem",
                "fs.s3a.access.key": os.getenv("AWS_ACCESS_KEY_ID"),
                "fs.s3a.secret.key": os.getenv("AWS_SECRET_ACCESS_KEY"),
                "fs.s3a.endpoint": os.getenv("AWS_ENDPOINT"),
                "fs.s3a.region": os.getenv("AWS_REGION")
            }
        }
    )



    return dg.Definitions(
        assets=[*sample_assets,*sample2],
        jobs=jobs,
        schedules=schedules,
        resources={
            
            "spark_s3_rsc" : configured_pyspark,
            
            "s3_test_io_manager": S3PartitionedCsvIOManager(
                pyspark=configured_pyspark,
                s3_bucket="test"
                
            ),
            "s3_datalake_io_manager": S3PartitionedCsvIOManager(
                pyspark=configured_pyspark,
                s3_bucket="lake"
                
            ),
            "conection_mysql" : PySparkMySQLResource(pyspark=configured_pyspark, host=dg.EnvVar("AW_CORE_HOST")
                                                     ,port=dg.EnvVar("AW_CORE_PORT")
                                                     ,database=dg.EnvVar("AW_CORE_DATABASE")
                                                     ,user=dg.EnvVar("AW_CORE_USER")
                                                     ,password=dg.EnvVar("AW_CORE_PASSWORD"))  ,
            
            # register the AdventureWorks MySQL resource here
        },
    )
