#!/bin/bash

cp *.qmd notebooks/
cd notebooks

for f in *.qmd; do
    echo "Rendering $file ..."
    quarto render "$f" --to ipynb
done
rm *.qmd

echo "Done."
