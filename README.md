# ClassifiedScrapper

## Overview
ClassifiedScrapper is a Python program designed to automate the process of finding "situation wanted" posts in the local Gulf Times newspaper classified pages. As a student, I encountered the need to stay updated with job postings, especially those not readily available on online platforms. This project was initiated to address the challenge of discovering job opportunities advertised exclusively in print media, particularly in regions where online job portals were not widely utilized by companies. ClassifiedScrapper was developed to streamline the task of scanning through daily PDF releases of the Gulf Times newspaper and extracting relevant job listings efficiently.

## Features
- **Automated Download**: The program automatically downloads the local newspaper classified pages on a daily basis.
- **OCR (Optical Character Recognition)**: Utilizes Wand, Tesseract OCR, ImageMagick, and GhostScript to perform OCR on the downloaded PDF pages.
- **Keyword Filtering**: Identifies and collects all posts containing the specified keywords, such as "Situation Wanted".
- **Customizable Filters**: Additional word filters can be easily added to scrape even more specific posts.
- **Time-Saving**: Enables users to focus solely on relevant classified posts, saving time and effort in the job search process.

## Technical Details
- **Language**: Python
- **Dependencies**:
  - Wand
  - BeautifulSoup4
  - Wand

**Note**: In addition to Python dependencies, the following software must be installed separately:
- **ImageMagick**: Download and install from [here](https://imagemagick.org/index.php).
- **GhostScript**: Download and install from [here](https://ghostscript.com/releases/gsdnld.html).
- **Tesseract OCR**: Download and install from [here](https://tesseract-ocr.github.io/tessdoc/Installation.html). Ensure that Tesseract is added to the system PATH.

## Usage
1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in the requirements.txt file.
3. Run the main script to initiate the scraping process.
4. Customize filters and configurations as needed.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
Special thanks to the developers of Wand, Tesseract OCR, ImageMagick, and GhostScript for their invaluable contributions to this project.
