#!/bin/bash
set -e

cp *.qmd notebooks/
cp -r misc notebooks/
cd notebooks

for f in *.qmd; do
    echo "Rendering $f ..."
    quarto render "$f" --to ipynb
done
rm *.qmd
rm -rf misc
cd ..

# The notebooks are generated here in post-render, i.e. *after* Quarto has
# already copied the `resources:` into the output dir. Since the .ipynb are no
# longer checked in (built by the GitHub Action), they don't exist at that
# point, so the download links would 404. Copy them into the rendered site now.
OUT="${QUARTO_PROJECT_OUTPUT_DIR:-docs}"
mkdir -p "$OUT/notebooks"
cp notebooks/*.ipynb "$OUT/notebooks/"

echo "Done."
