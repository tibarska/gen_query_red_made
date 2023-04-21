### Download data
download files and extract them to ```raw``` directory:

https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-queries.tsv.gz
https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-top100.gz
https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-qrels.tsv.gz

### Generate csv files for db:
``python generate_csv.py``

### Create container:
``docker build -t db_red .``

### Run container and upload data:
``docker run -it -v /path_to_project/project/gen_query_red_made/volume:/volume -v /path_to_project/project/gen_query_red_made/data:/data db_red ./db_init.sh``
