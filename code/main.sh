echo 'Pre-processing'
python pre_process.py
echo 'Calculating features'
python add_features.py
echo 'making word matrix'
python make_word_matrix.py
echo 'calculating principle components'
python pca.py $1
echo 'categorising'
python categorise.py