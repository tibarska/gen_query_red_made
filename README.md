download files and extract them to ```raw``` directory:
https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-queries.tsv.gz
https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-top100.gz
https://msmarco.blob.core.windows.net/msmarcoranking/msmarco-docdev-qrels.tsv.gz

generate csv files for db:
``python generate_csv.py``

create container:
``docker build -t db_red .``

run container and upload data:
``docker run -it -v /home/lolvista/MADE/sem2/project/gen_query_red_made/volume:/volume -v /home/lolvista/MADE/sem2/project/gen_query_red_made/data:/data db_red ./db_init.sh``
``docker run -it -v /home/lolvista/MADE/sem2/project/gen_query_red_made/volume:/volume db_red ./db_init.sh``
docker run -it -v /home/lolvista/MADE/sem2/project/gen_query_red_made/volume:/volume -v /home/lolvista/MADE/sem2/project/gen_query_red_made/data:/data db_red ./db_init.sh
