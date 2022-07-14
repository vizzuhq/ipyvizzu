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

read -r -d '' presetExamples <<- EOM
  ${testcaseDir}/preset/02_C_R_column.mjs
  ${testcaseDir}/preset/03_C_R_grouped_column_negative.mjs
  ${testcaseDir}/preset/04_C_R_stacked_column.mjs
  ${testcaseDir}/preset/05_C_R_splitted_column.mjs
  ${testcaseDir}/preset/06_C_R_percentage_column.mjs
  ${testcaseDir}/preset/08_C_R_waterfall.mjs
  ${testcaseDir}/preset/09_C_R_stacked_mekko.mjs
  ${testcaseDir}/preset/10_C_R_marimekko.mjs
  ${testcaseDir}/preset/13_C_R_bar_negative.mjs
  ${testcaseDir}/preset/14_C_R_grouped_bar_negative.mjs
  ${testcaseDir}/preset/15_C_R_stacked_bar.mjs
  ${testcaseDir}/preset/16_C_R_splitted_bar.mjs
  ${testcaseDir}/preset/17_C_R_percentage_bar.mjs
  ${testcaseDir}/preset/20_C_C_lollipop chart.mjs
  ${testcaseDir}/preset/22_C_C_scatter.mjs
  ${testcaseDir}/preset/24_C_C_bubbleplot.mjs
  ${testcaseDir}/preset/27_C_A_area_negative.mjs
  ${testcaseDir}/preset/28_C_A_stacked_area.mjs
  ${testcaseDir}/preset/31_C_A_splitted_area.mjs
  ${testcaseDir}/preset/32_C_A_stream.mjs
  ${testcaseDir}/preset/33_C_A_vertical_stream.mjs
  ${testcaseDir}/preset/34_C_A_violin.mjs
  ${testcaseDir}/preset/35_C_A_vertical_violin.mjs
  ${testcaseDir}/preset/38_C_L_line.mjs
  ${testcaseDir}/preset/39_C_L_vertical_line.mjs
  ${testcaseDir}/preset/40_P_R_pie.mjs
  ${testcaseDir}/preset/42a_P_R_polar_stacked_column.mjs
  ${testcaseDir}/preset/42_P_R_polar_column.mjs
  ${testcaseDir}/preset/44_P_R_variable_radius_pie_chart.mjs
  ${testcaseDir}/preset/49_P_R_radial_bar.mjs
  ${testcaseDir}/preset/50_P_R_radial_stacked_bar.mjs
  ${testcaseDir}/preset/51_P_R_donut.mjs
  ${testcaseDir}/preset/52_P_R_nested_donut.mjs
  ${testcaseDir}/preset/53_P_C_polar_scatter.mjs
  ${testcaseDir}/preset/56_P_A_polar_line.mjs
  ${testcaseDir}/preset/58_W_R_treemap.mjs
  ${testcaseDir}/preset/59_W_R_stacked_treemap.mjs
  ${testcaseDir}/preset/60_W_R_heatmap.mjs
  ${testcaseDir}/preset/61_W_R_bubble_chart.mjs
  ${testcaseDir}/preset/62_W_R_stacked_bubble.mjs
EOM

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
mkdir -p ${examplesDir}/presets
mkdir -p ${examplesDir}/static
mkdir -p ${examplesDir}/animated

for datafile in $datafiles; do
  echo "Processing $datafile"
  node vizzu-lib/tools/js2csv/js2csv.js "../../test/integration/test_data/${datafile}" ${docsDir}/data/$(basename ${datafile%.mjs}.csv)
done

printf '%b\n' "---${n}jupytext:${n}${t}formats: md:myst${n}${t}text_representation:${n}${t}${t}extension: .md${n}${t}${t}format_name: myst${n}kernelspec:${n}${t}display_name: .venv${n}${t}language: python${n}${t}name: .venv${n}title: ipyvizzu - Examples${n}---" > ${examplesDir}/examples.md

echo -e "\n# ipyvizzu examples" >> ${examplesDir}/examples.md

echo -e "\n## Preset charts" >> ${examplesDir}/examples.md

echo "<div>" >> ${examplesDir}/examples.md
for example in $presetExamples; do
  echo -n "<div style=\"float:left\">" >> ${examplesDir}/examples.md
  echo -n "<a href=\"presets/$(basename ${example%.mjs}.html)\">" >> ${examplesDir}/examples.md
  echo -n "<img src=\"${thumbUrl}/presets/$(basename ${example%.mjs}.png)\">" >> ${examplesDir}/examples.md
  echo -n "</a>" >> ${examplesDir}/examples.md
  echo "</div>" >> ${examplesDir}/examples.md
  ./mjs2ipynb.sh ${venv} $example ${examplesDir}/presets/$(basename ${example%.mjs}.ipynb)
done
echo "</div>" >> ${examplesDir}/examples.md
echo "<div style=\"clear:both\"></div>" >> ${examplesDir}/examples.md

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


echo -n "ipyvizzu.vizzuhq.com" > ${docsDir}/CNAME