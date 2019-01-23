import subprocess
from distutils.version import LooseVersion


def reverse_complement(sequence):
    """
    Arguments:
        sequence (str): DNA sequence, can have non ATGC nucleotide will remain untouched
    Returns:
       reversed_string.translate(_rc_trans) (str): reverse complement of input sequence
    """
    assert isinstance(sequence, str), 'Sequence Provided Not String'
    # reverse string
    reversed_string = sequence[::-1]
    # replace base with complement
    _rc_trans = str.maketrans('ACGTNacgtn', 'TGCANtgcan')
    return reversed_string.translate(_rc_trans)


def retrieve_iupac(nucleotide):
    """
    Arguments:
        nucleotide (str): single character
    Returns:
        iupac_tuple (tuple): tuple of strings with possible bases
    """
    iupac_key = {'R': ('A', 'G'), 'Y': ('C', 'T'), 'S': ('G', 'C'), 'W': ('A', 'T'), 'K': ('G', 'T'), 'M': ('A', 'C'),
                 'B': ('C', 'G', 'T'), 'D': ('A', 'G', 'T'), 'H': ('A', 'C', 'T'), 'V': ('A', 'C', 'G'),
                 'N': ('A', 'C', 'G', 'T')}
    try:
        iupac_tuple = iupac_key[nucleotide]
    except KeyError:
        iupac_tuple = tuple(nucleotide)
    return iupac_tuple


def check_bowtie2_path(bowtie2_path='bowtie2'):
    """Simple function to check bowti2 path. If path is valid and version >= 2.3.4.2 function exits normally. If path
    not valid raise FileNotFoundError. If version < 2.3.4.2 raise RuntimeWarning.
    Keyword Arguments:
        bowtie2_path (str): path to bowtie executable, default = bowtie2, default assumes bowtie2 is in system path
    """
    # external command
    bowtie2_version_command = [bowtie2_path, '--version']
    try:
        bowtie2_check = subprocess.Popen(bowtie2_version_command, stdout=subprocess.PIPE, universal_newlines=True)
    except FileNotFoundError:
        raise FileNotFoundError('Bowtie2 not in system path or Bowtie2 Executable Path Incorrect')
    else:
        # get first line of stdout
        version_line = next(iter(bowtie2_check.stdout.readline, ''))
        bowtie2_version = version_line.replace('\n', '').split(' ')[-1]
        if LooseVersion(bowtie2_version) < LooseVersion('2.2.9'):
            raise RuntimeWarning('BSeeker-R Performance not evaluated on Bowtie2 Versions < 2.2.9')