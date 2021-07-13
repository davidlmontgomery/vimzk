"""
File system utilities.

"""
import glob
import os


ZKEXT_SCHEME = 'zkext:'


# FIXME Add tests for zkext_completions
def zkext_completions(external_files_base, completion_base):
    """
    Return list of 'zkext:' link completions for provided completion_base.

    """
    schemeless_completion_base = completion_base[len(ZKEXT_SCHEME):]
    path_prefix = external_files_base + schemeless_completion_base
    path_completions = glob.glob(path_prefix + '*')
    for ii, pc in enumerate(path_completions):
        pc = pc.replace(external_files_base, '')
        pc = pc.replace("'", "''")                 # Double single-quotes to escape for vim
        path_completions[ii] = ZKEXT_SCHEME + pc
    return path_completions


def subdirectory_basenames(parent_directory):
    """
    Return list of immediate subdirectories of provided parent_directory.

    """
    return [os.path.basename(sd.rstrip('/')) for sd in glob.glob(parent_directory + '*/')]

