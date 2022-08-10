

class ChapterSorter:
    def sort(self, chapter_names: list) -> list:
        index_separator = '_'

        def chapters_indexes_as_integers(valid_filename):
            chapter_index = valid_filename.split(index_separator)[0]
            return int(chapter_index)

        return sorted(chapter_names, key=chapters_indexes_as_integers)
