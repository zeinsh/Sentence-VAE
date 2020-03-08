# I had problems to use wordcloud with python3 
# and also problems to remove stopwords in python2.7
# so this script is mix between the two

lang=$3
savedir=$2
txtfile=$1

python3 clean_stopwords.py $txtfile --lang $lang
python wordcloud-lang.py tmp/clean_output.txt --lang $lang --savedir $savedir
