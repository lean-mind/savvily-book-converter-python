

class ChapterSorter:
    def sort(self, chapter_names: list[str]) -> list[str]:
        index_separator = '_'

        def chapters_indexes_as_integers(valid_filename: str) -> int:
            chapter_index = valid_filename.split(index_separator)[0]
            return int(chapter_index)

        return sorted(chapter_names, key=chapters_indexes_as_integers)
