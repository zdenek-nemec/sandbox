import os
from pathlib import Path
from PIL import Image
import pyheif


def convert_heic(input_dir: str, output_dir: str, output_format: str = "PNG") -> None:
    """
    Converts all HEIC images in the input directory to specified format and saves them in the output directory.

    :param input_dir: Path to the directory containing HEIC images.
    :param output_dir: Path to the directory where converted images will be saved.
    :param output_format: Requested format.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.exists():
        print(f"Input directory {input_dir} does not exist.")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    formats = {
        "JPEG": "jpg",
        "PNG": "png"
    }
    if output_format not in formats:
        print(f"Unknown format {output_format}.")
        return

    for heic_file in list(input_path.glob("*.heic")) + list(input_path.glob("*.HEIC")):
        try:
            heif_file = pyheif.read(heic_file)
            image = Image.frombytes(
                mode=heif_file.mode,
                size=heif_file.size,
                data=heif_file.data
            )
            output_file = output_path / f"{heic_file.stem}.{formats[output_format]}"
            image.save(output_file, output_format)
            print(f"Converted: {heic_file} -> {output_file}")
        except Exception as e:
            print(f"Failed to convert {heic_file}: {e}")


def main():
    print("HEIC to PNG Converter")
    convert_heic(input_dir=".", output_dir=".")
    # convert_heic(input_dir=".", output_dir=".", output_format="JPEG")


if __name__ == "__main__":
    main()
