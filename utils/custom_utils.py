from typing import List
from pyspark.sql import DataFrame
from pyspark.sql.window import Window
from pyspark.sql.functions import col, concat, row_number
from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable



class Transformations:

    def de_duplication(self, df, columns, order_by):
        window = Window.partitionBy(*columns).orderBy(col(order_by).desc())
        return (
            df.withColumn("rn", row_number().over(window))
              .filter(col("rn") == 1)
              .drop("rn")
        )

    def process_timestamp(self, df):
        return df.withColumn("process_timestamp", current_timestamp())

    def upsert(self, spark, df, key_cols, table, cdc):
        merge_condition = " AND ".join(
            [f"src.{c} = trg.{c}" for c in key_cols]
        )

        delta_table = DeltaTable.forName(
            spark,
            f"pyspark_dbt.silver.{table}"
        )

        (
            delta_table.alias("trg")
            .merge(df.alias("src"), merge_condition)
            .whenMatchedUpdateAll(condition=f"src.{cdc} > trg.{cdc}")
            .whenNotMatchedInsertAll()
            .execute()
        )


    









        