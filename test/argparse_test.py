import argparse


def basic_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_mode', type=str, default= 'unaligned', help='chooses how datasets are loaded')
    parser.add_argument('--mode', type=str, default='test', help='test mode')
    parser.add_argument('--test', action='store_true')
    return parser

def data_options(parser):
    parser.add_argument('--lr', type=str, default='0.0001', help='learning rate')
    return parser

if __name__ == '__main__':
    parser = basic_options()
    opt, unparsed = parser.parse_known_args()
    print(opt)
    print(unparsed)
    parser = data_options(parser)
    opt = parser.parse_args()
    print(opt)