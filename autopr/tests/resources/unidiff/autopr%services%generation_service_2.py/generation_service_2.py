import tempfile
from typing import Callable

import git
import pydantic
import transformers
from git import Tree



















































































































































































































































































































        repo_tree = repo.head.commit.tree
        files = self._repo_to_file_descriptors(repo_tree)

        # Get the filepaths to look at
        filepaths = self.get_initial_filepaths(files, issue_text)

        if filepaths: