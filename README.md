This script is a cPanel List Filter, designed to process a list of URLs, clean and standardize their format, and extract valid cPanel login links. The script performs the following key tasks:

* Reads an input file – It prompts the user for a file containing raw URLs.

* Processes and transforms each line – It removes unnecessary spaces, standardizes the protocol to https://, replaces incorrect port numbers, and formats credentials properly.

* Filters valid cPanel login entries – It ensures each line matches the expected format (https://domain:2083|username|password).

* Writes the cleaned data to an output file – The filtered and formatted lines are saved into filtered_list.txt.

* Handles encoding issues – If the input file has decoding errors, it retries using a different encoding (latin-1).


![Alt text](https://raw.githubusercontent.com/cpkarma/img/main/cp-filter.jpg)
