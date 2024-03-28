# Databricks notebook source
PRINT('TEST')

# COMMAND ----------

def test(a, b):
    c = a + b
    print(c)

# COMMAND ----------

c = dbutils.widgets.get('c')

# COMMAND ----------

d = dbutils.widgets.get('d')

# COMMAND ----------

test(c, d)

# COMMAND ----------

dbutils.notebook.exit('completed')

# COMMAND ----------


