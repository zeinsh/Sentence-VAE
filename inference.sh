python inference.py -c bin/zero/E9.pytorch -n 10000 > output/zero.samples
python inference.py -c bin/constant/E9.pytorch -n 10000 > output/constant.samples
python inference.py -c bin/linear/E9.pytorch -n 10000 > output/linear.samples
python inference.py -c bin/cyclic/E9.pytorch -n 10000 > output/cyclic.samples 
