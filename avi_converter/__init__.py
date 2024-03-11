import ffmpeg
import argparse
import pathlib


def cli():

    parser = argparse.ArgumentParser(description='Convert avi to mp4')
    parser.add_argument('input', type=open)
    parser.parse_args()

    input_path = pathlib.Path(parser.parse_args().input.name).resolve()
    output_path = input_path.with_suffix('.mp4')

    print(f'Converting {input_path} to {output_path}')

    (
        ffmpeg
        .input(input_path.name)
        .output(output_path.name, **{'crf': 28})
        .run()
    )


if __name__ == '__main__':
    cli()
