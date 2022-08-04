from infrastructure.ChapterValidator import ChapterValidator


class ChapterSorter:
    def sort(self, chapter_names: list) -> list:
        index_separator = '_'
        validator = ChapterValidator()
        valid_filenames = [filename for filename in chapter_names
                           if validator.is_valid_name(filename)]

        def chapters_indexes_as_integers(valid_filename):
            chapter_index = valid_filename.split(index_separator)[0]
            return int(chapter_index)

        return sorted(valid_filenames, key=chapters_indexes_as_integers)
