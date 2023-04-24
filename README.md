All commands must be executed in the project directory (``gen_query_red_made``):

### Create container:
``docker build -t db_red .``

### Run container and upload data:
``docker run -it -v /path_to_project/gen_query_red_made/volume:/volume -v /path_to_project/gen_query_red_made/data:/data db_red ./db_init.sh``

### Iterator usage:
``python iterator.py table_name batch_size``

Iterator's response:
```
[
  [(row_1),(row_2),(row_3)...(row_BS)],
  .....,
  [(row_1),(row_2),(row_3)...(row_BS)]
]```
