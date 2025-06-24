#!/bin/bash

# File: amfi_nav_extract.sh

URL="https://www.amfiindia.com/spages/NAVAll.txt"
OUTPUT="nav_data.tsv"

# Download the file
curl -s "$URL" -o nav.txt

# Extract header line index
HEADER_LINE=$(grep -n -m 1 'Scheme Code;ISIN' nav.txt | cut -d: -f1)

# Skip header lines and filter scheme name + nav value
tail -n +"$((HEADER_LINE + 1))" nav.txt | \
  awk -F ';' 'NF >= 5 { print $4 "\t" $5 }' > "$OUTPUT"

echo "✅ Extracted Scheme Name and NAV into $OUTPUT"
