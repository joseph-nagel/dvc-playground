'''Dummy data creation.'''

from argparse import ArgumentParser
from pathlib import Path

import numpy as np


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('-o', '--out-file', type=Path, required=True, help='output file')
    parser.add_argument('-n', '--num-samples', type=int, default=1, help='number of samples')
    parser.add_argument('-d', '--num-dim', type=int, default=1, help='number of dimensions')
    parser.add_argument('-s', '--seed', type=int, required=False, help='random seed')

    parser.add_argument('--overwrite', dest='overwrite', action='store_true', help='overwrite existing file')
    parser.add_argument('--no-overwrite', dest='overwrite', action='store_false', help='do not overwrite')
    parser.set_defaults(overwrite=False)

    args = parser.parse_args()
    return args


def main(args):

    # set random seed
    if args.seed is not None:
        np.random.seed(args.seed)

    # sample data
    x = np.random.randn(args.num_samples, args.num_dim)

    # create output dir
    out_file = args.out_file

    out_dir = args.out_file.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # save file
    file_ext = out_file.suffix.lower()

    if args.overwrite or not out_file.exists():
        if file_ext == '.npy':
            np.save(out_file, x)
        elif file_ext in ('.csv', '.txt'):
            np.savetxt(out_file, x, fmt='%.8f', delimiter=',')
        else:
            raise ValueError(f'File extension not supported: {file_ext}')
    else:
        raise FileExistsError(f'File already exists: {out_file}')


if __name__ == '__main__':

    args = parse_args()
    main(args)
