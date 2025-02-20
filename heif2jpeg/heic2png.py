import os
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener


def convert_heif(input_dir: str, output_dir: str, output_format: str = "JPEG") -> None:
    """
    Converts all HEIC images in the input directory to specified format and saves them in the output directory.

    :param input_dir: Path to the directory containing HEIC images.
    :param output_dir: Path to the directory where converted images will be saved.
    :param output_format: Requested format. Default JPEG.
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

    register_heif_opener()
    for heif_file in input_path.glob("*.HEIC"):
        try:
            image = Image.open(heif_file)
            output_file = output_path / f"{heif_file.stem}.{formats[output_format]}"
            icc_profile = image.info.get("icc_profile")
            dictionary=image.info
            exif_dict=dictionary["exif"]
            # image.save(output_file, output_format, icc_profile=icc_profile, exif=exif_dict)
            image.save(output_file, output_format, subsampling=0, quality=95, icc_profile=icc_profile, exif=exif_dict)
            print(f"Converted: {heif_file} -> {output_file}")
        except Exception as e:
            print(f"Failed to convert {heif_file}: {e}")


def main():
    print("HEIF to JPEG Converter")
    convert_heif(input_dir="./test", output_dir="./test")
    convert_heif(input_dir="./test", output_dir="./test", output_format="PNG")


if __name__ == "__main__":
    main()
