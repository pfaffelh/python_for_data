#!/bin/bash

for file in *.qmd; do
    echo "Rendering $file ..."
    quarto render "$file"
done

echo "Done."
