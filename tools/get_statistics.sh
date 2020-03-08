txtfile=$1
savedir=$2
lang=$3

mkdir $savedir >> log/mkdir.log
python3 statistics.py $txtfile --savedir $savedir --lang $lang >> $savedir/output.txt
bash generate_wordcloud.sh $txtfile $savedir $lang
