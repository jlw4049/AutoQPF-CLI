from pathlib import Path

from auto_qpf.qpf import QpfGenerator


def create_stax_rip_directory(file_input: Path):
    # create staxrip temp directory if it doesn't exist
    output_dir = Path(
        Path(file_input).parent
        / Path(str(Path(file_input.name).with_suffix("")) + "_temp")
    )
    # print("printing output directory")
    # print(output_dir)
    output_dir.mkdir(exist_ok=True)

    # define file out for staxrip output
    file_output = output_dir / Path(file_input.name).with_suffix(".qpf")
    return file_output


def process_args(file_input, file_output, fps, auto_detect_fps):
    # print(file_input)
    # print(file_output)
    qpf = QpfGenerator().generate_qpf(file_input, file_output, fps, auto_detect_fps)
    return qpf
