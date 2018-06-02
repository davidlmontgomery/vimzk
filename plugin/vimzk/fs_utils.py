"""
File system utilities.

"""
import glob


ZKEXT_SCHEME = 'zkext:'


# FIXME Add tests for zkext_completions
def zkext_completions(external_files_base, completion_base):
    """
    Return list of 'zkext:' link completions for provided completion_base.

    """
    schemeless_completion_base = completion_base[len(ZKEXT_SCHEME):]
    path_prefix = external_files_base + schemeless_completion_base
    path_completions = glob.glob(path_prefix + '*')
    return [ZKEXT_SCHEME + pc.replace(external_files_base, '') for pc in path_completions]
