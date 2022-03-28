import re


class Normalizer:
    def __init__(self):
        self.display_pattern = re.compile(r"display_[a-f0-9]{7}", flags=re.MULTILINE)
        self.vizzu_pattern = re.compile(r"myVizzu_[a-f0-9]{7}", flags=re.MULTILINE)
        self.chart_pattern = re.compile(r"chart_[a-f0-9]{7}", flags=re.MULTILINE)
        self.snaphot_pattern = re.compile(r"snapshot_[a-f0-9]{7}", flags=re.MULTILINE)
        self.pre_run_pattern = re.compile(
            '<script id="myVizzu">\n    document.inhibitScroll = false;\n</script>\n',
            flags=re.MULTILINE,
        )

    def normalize_id(self, output):
        normalized_output = output
        normalized_output = self.display_pattern.sub("display", normalized_output)
        normalized_output = self.vizzu_pattern.sub("myVizzu", normalized_output)
        normalized_output = self.chart_pattern.sub("chart", normalized_output)
        normalized_output = self.snaphot_pattern.sub("snaphot", normalized_output)
        normalized_output = self.pre_run_pattern.sub("", normalized_output)
        return normalized_output
