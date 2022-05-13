#!/bin/bash
venv="$1"

#./sparse-clone-vizzu-lib.sh

docsDir=../../docs
examplesDir=${docsDir}/examples
testDir=vizzu-lib/test/integration
testcaseDir=${testDir}/test_cases/web_content
thumbUrl=https://github.com/vizzuhq/vizzu-lib-doc/raw/main/docs/latest/content/examples

n="\n"
t="  "


printf '%b\n' "---${n}jupytext:${n}${t}formats: md:myst${n}${t}text_representation:${n}${t}${t}extension: .md${n}${t}${t}format_name: myst${n}kernelspec:${n}${t}display_name: .venv${n}${t}language: python${n}${t}name: .venv${n}title: ipyvizzu${n}---${n}" > ${docsDir}/index.md

cat ../../README.md >> ${docsDir}/index.md

${venv}/bin/jupytext --to notebook ${docsDir}/index.md

rm ${docsDir}/index.md


staticExamples=$( find ${testcaseDir}/sample_static/ -name "*.mjs" )

read -r -d '' animatedExamples <<- EOM
  ${testcaseDir}/templates/composition_percentage_area_stream_3dis_1con.mjs 
  ${testcaseDir}/templates/composition_comparison_pie_coxcomb_column_2dis_2con.mjs 
  ${testcaseDir}/templates/composition_percentage_column_stream_3dis_1con.mjs 
  ${testcaseDir}/templates/merge_split_area_stream_3dis_1con.mjs 
  ${testcaseDir}/templates/total_element_bubble_2_bar.mjs 
  ${testcaseDir}/templates/merge_split_bar.mjs 
  ${testcaseDir}/templates/merge_split_radial_stacked_rectangle_2dis_1con.mjs 
  ${testcaseDir}/templates/orientation_circle.mjs 
  ${testcaseDir}/templates/orientation_marimekko_rectangle_2dis_2con.mjs 
  ${testcaseDir}/templates/pie_donut2_rectangle_1dis_1con.mjs 
  ${testcaseDir}/templates/relationship_comparison_circle_2_bubble_plot.mjs 
  ${testcaseDir}/templates/relationship_total_bubble_plot_column.mjs 
  ${testcaseDir}/templates/stack_group_area_line.mjs 
  ${testcaseDir}/templates/stack_group_circle.mjs 
  ${testcaseDir}/templates/stack_group_treemap.mjs 
  ${testcaseDir}/templates/total_element_bubble_column.mjs 
  ${testcaseDir}/templates/total_time_area_column.mjs 
  ${testcaseDir}/templates/treemap_radial.mjs 
  ${testcaseDir}/templates/zoom_area.mjs 
  ${testcaseDir}/templates/composition_percentage_column_3dis_1con.mjs 
  ${testcaseDir}/templates/total_time_bar_line.mjs
EOM

read -r -d '' storyExamples <<- EOM
  musicformats
EOM

datafiles="chart_types_eu.mjs infinite_data.mjs music_industry_history_1.mjs tutorial.mjs"

mkdir -p ${docsDir}/data
mkdir -p ${examplesDir}/static
mkdir -p ${examplesDir}/animated

for datafile in $datafiles; do
  echo "Processing $datafile"
  node vizzu-lib/tools/js2csv/js2csv.js "../../test/integration/test_data/${datafile}" ${docsDir}/data/$(basename ${datafile%.mjs}.csv)
done

printf '%b\n' "---${n}jupytext:${n}${t}formats: md:myst${n}${t}text_representation:${n}${t}${t}extension: .md${n}${t}${t}format_name: myst${n}kernelspec:${n}${t}display_name: .venv${n}${t}language: python${n}${t}name: .venv${n}title: ipyvizzu - Examples${n}---" > ${examplesDir}/examples.md

echo -e "\n# ipyvizzu examples" >> ${examplesDir}/examples.md

echo -e "\n## Static charts" >> ${examplesDir}/examples.md

echo "<div>" >> ${examplesDir}/examples.md
for example in $staticExamples; do
  echo -n "<div style=\"float:left\">" >> ${examplesDir}/examples.md
  echo -n "<a href=\"static/$(basename ${example%.mjs}.html)\">" >> ${examplesDir}/examples.md
  echo -n "<img src=\"${thumbUrl}/static/$(basename ${example%.mjs}.png)\">" >> ${examplesDir}/examples.md
  echo -n "</a>" >> ${examplesDir}/examples.md
  echo "</div>" >> ${examplesDir}/examples.md
  ./mjs2ipynb.sh ${venv} $example ${examplesDir}/static/$(basename ${example%.mjs}.ipynb)
done
echo "</div>" >> ${examplesDir}/examples.md
echo "<div style=\"clear:both\"></div>" >> ${examplesDir}/examples.md

echo -e "\n## Animated charts" >> ${examplesDir}/examples.md

echo "<div>" >> ${examplesDir}/examples.md
for example in $animatedExamples; do
  echo -n "<div style=\"float:left\">" >> ${examplesDir}/examples.md
  echo -n "<a href=\"animated/$(basename ${example%.mjs}.html)\">" >> ${examplesDir}/examples.md
  echo -n "<video nocontrols autoplay muted loop src=\"${thumbUrl}/animated/$(basename ${example%.mjs}.mp4)\" type=\"video/mp4\"></video>" >> ${examplesDir}/examples.md
  echo -n "</a>" >> ${examplesDir}/examples.md
  echo "</div>" >> ${examplesDir}/examples.md
  ./mjs2ipynb.sh ${venv} $example ${examplesDir}/animated/$(basename ${example%.mjs}.ipynb)
done
echo "</div>" >> ${examplesDir}/examples.md
echo "<div style=\"clear:both\"></div>" >> ${examplesDir}/examples.md

echo -e "\n## Data stories" >> ${examplesDir}/examples.md

echo "<div>" >> ${examplesDir}/examples.md
for example in $storyExamples; do
  echo -n "<div style=\"float:left\">" >> ${examplesDir}/examples.md
  echo -n "<a href=\"stories/${example}/${example}.html\">" >> ${examplesDir}/examples.md
  echo -n "<video nocontrols autoplay muted loop src=\"${thumbUrl}/stories/$(basename ${example}.mp4)\" type=\"video/mp4\"></video>" >> ${examplesDir}/examples.md
  echo -n "</a>" >> ${examplesDir}/examples.md
  echo "</div>" >> ${examplesDir}/examples.md
done
echo "</div>" >> ${examplesDir}/examples.md
echo "<div style=\"clear:both\"></div>" >> ${examplesDir}/examples.md

echo -e "\nBack to the [Table of contents](../doc.html#tutorial)" >> ${examplesDir}/examples.md

${venv}/bin/jupytext --to notebook ${examplesDir}/examples.md

rm ${examplesDir}/examples.md
