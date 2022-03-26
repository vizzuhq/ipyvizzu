#!/bin/bash

./sparse-clone-vizzu-lib.sh

outdir=../../docs/examples
staticExamples=$( find vizzu-lib/test/integration/test_cases/web_content/sample_static/ -name "*.mjs" )
animatedExamples=$( find vizzu-lib/test/integration/test_cases/web_content/templates/ -name "*.mjs" )

mkdir -p ${outdir}/static
mkdir -p ${outdir}/animated

for example in $staticExamples; do
  ./mjs2ipynb.sh $example ${outdir}/static/$(basename ${example%.mjs}.ipynb)
done

for example in $animatedExamples; do
  ./mjs2ipynb.sh $example ${outdir}/animated/$(basename ${example%.mjs}.ipynb)
done
