import os
from PyPDF2 import PdfMerger

OUTPUT_FILENAME = "merged_output.pdf"


def merge_pdf(pdf_list: list, output_filename: str) -> None:
    merger = PdfMerger()

    for pdf in pdf_list:
        if os.path.exists(pdf) and os.path.isfile(pdf):
            merger.append(pdf)
            print(f"[INFO] Added {pdf}")
        else:
            print(f"[WARNING] {pdf} does not exist. Skipping.")

    with open(output_filename, "wb") as output_file:
        merger.write(output_file)

    merger.close()
    print(f"[INFO] Merged PDF saved as {output_filename}")


def main():
    pdf_files = [filename for filename in os.listdir() if filename[-4:] == ".pdf" and filename != OUTPUT_FILENAME]
    merge_pdf(pdf_files, OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
