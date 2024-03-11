import argparse
import pathlib

import ffmpeg


def get_absolute_path(path):
    """
    Converts a relative or absolute path to an absolute path.
    """

    if pathlib.Path(path).is_absolute():
        return pathlib.Path(path)
    else:
        return pathlib.Path(path).resolve()


def cli():
    parser = argparse.ArgumentParser(description='Convert avi to mp4')
    parser.add_argument('input', type=open)
    parser.parse_args()

    input_path = get_absolute_path(parser.parse_args().input.name)
    output_path = input_path.with_suffix('.mp4')
    print(f'Converting {input_path} to {output_path}')

    (
        ffmpeg
        .input(input_path)
        .output(str(output_path), **{'crf': 28})
        .run()
    )


if __name__ == '__main__':
    cli()
