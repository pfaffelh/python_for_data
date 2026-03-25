#!/bin/bash

cp *.qmd notebooks/
cp -r misc notebooks/
cd notebooks

for f in *.qmd; do
    echo "Rendering $f ..."
    quarto render "$f" --to ipynb
done
rm *.qmd
rm -rf misc

echo "Done."
