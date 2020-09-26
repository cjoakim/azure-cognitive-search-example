#!/bin/bash

# Chris Joakim, Microsoft, 2020/09/26

source bin/activate

echo '=========='
python cosmos.py load_airports dev airports no-duplicates
sleep 5

echo '=========='
python search-client.py delete_indexer airports
sleep 5

echo '=========='
python search-client.py delete_index airports
sleep 5

echo '=========='
python search-client.py create_index airports airports_index_v1
sleep 5

echo '=========='
python search-client.py create_cosmos_datasource dev airports
sleep 5

echo '=========='
python search-client.py create_indexer airports airports_indexer_v1
sleep 5

echo 'wait for the indexer to complete, then:'
echo 'python search-client.py search_index airports all'
