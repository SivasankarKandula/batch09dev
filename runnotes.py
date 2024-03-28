# Databricks notebook source
dbutils.notebook.help()

# COMMAND ----------

dbutils.notebook.help('run')

# COMMAND ----------

dbutils.notebook.run('/Workspace/Users/lalithapuranapu@gmail.com/class/runNotebook' , 10 , {"c":"4" , "d" :"10"})

# COMMAND ----------

x  = dbutils.notebook.run('/Workspace/Users/lalithapuranapu@gmail.com/class/runNotebook' , 10 , {"c":"4" , "d" :"10"})

# COMMAND ----------

print(x)

# COMMAND ----------


