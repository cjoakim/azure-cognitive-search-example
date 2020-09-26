#!/bin/bash

# Chris Joakim, Microsoft, 2020/09/26

source bin/activate

echo '=========='
python search-client.py create_synmap synmap synonym_map_v1
python search-client.py update_synmap synmap synonym_map_v1
sleep 5

echo '=========='
python storage-client.py create_upload_list
sleep 5

echo '=========='
python storage-client.py upload_files 999
sleep 5

echo '=========='
python search-client.py delete_indexer documents
sleep 5

echo '=========='
python search-client.py delete_skillset skillset
sleep 5

echo '=========='
python search-client.py delete_index documents
sleep 5



echo '=========='
python search-client.py create_index documents documents_index_v1
sleep 5

echo '=========='
python search-client.py create_skillset skillset skillset_v1
sleep 5

echo '=========='
python search-client.py create_indexer documents documents_indexer_v1
sleep 2

echo 'wait for the indexer to complete, then:'
echo 'python search-client.py search_index documents all'
