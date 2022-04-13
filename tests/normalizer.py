import re


class Normalizer:
    def __init__(self):
        self.id1_pattern = re.compile(r"'[a-f0-9]{7}'", flags=re.MULTILINE)
        self.id2_pattern = re.compile(r"\"[a-f0-9]{7}\"", flags=re.MULTILINE)

    def normalize_id(self, output):
        normalized_output = output
        normalized_output = self.id1_pattern.sub("id", normalized_output)
        normalized_output = self.id2_pattern.sub("id", normalized_output)
        return normalized_output
