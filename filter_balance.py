import base58
import binascii
import argparse
import bech32


def tocondensed(add_or_pk):
    return base58.b58decode(add_or_pk)[1:-4]


def process(csvfile):
    f2 = open("btc_balance.json", 'w')
    f2.write("{\n")
    
    with open(csvfile, 'r') as f:
        for i, row in enumerate(f):
            if i == 0:
                print(row[:-1] + ',ripemd')
                continue
            elif row.strip() == '':
                break
            address = str(row.split(',')[0])
            value = int(row.split(',')[1])
            if value > 1000000000:
                f2.write('"%s": %d,\n'%(address,  value) )
    f2.write("}\n")
    f2.close()

def input_args():
    parser = argparse.ArgumentParser(description='Read csv file with btc address as first column'\
                                     ' encodes it to ripemd160 binascii representation and writes to stdout'
                                       )
    parser.add_argument(
        'csvin',
        metavar='csv file',
        type=str,
        help='path to csv file with btc address in first column (usually output of btcposbal2csv)'
    )

    a = parser.parse_args()
    return a


if __name__ == '__main__':
    args = input_args()
    process(args.csvin)
