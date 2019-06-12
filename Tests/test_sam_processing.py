from BSB.BSB_Align.ProcessSamReads import ProcessSamAlignment
import os
import pickle
import unittest

# get current directory

test_directory = os.path.dirname(os.path.realpath(__file__))
bsb_directory = '/'.join(test_directory.split('/')[:-1]) + '/'
bsbolt = f'{bsb_directory}BSBolt.py'
with open(f'{bsb_directory}Tests/TestData/BSB_Test_DB_S/genome_index.pkl', 'rb') as lo:
    contig_lens = pickle.load(lo)

test_read_1 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'})]
test_read_2 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP', 'XM:i:1'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP', 'XM:i:1'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'})]
test_read_3 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '666', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'})]
test_read_4 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:5', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'})]
test_read_5 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '121M4I1D', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAG', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGG', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'})]
test_read_6 = [({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'}), ({'QNAME': 'chr10-65374', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'G2A', 'mapping_reference': 'W_G2A'}, {'QNAME': 'chr10-65374', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': 'AB<CCGGGGGGG1GG>GB=C1@1GGGGGGGGGGGGFGGGGGFG@GGGGGGGGEFGGGGGGGGFGGFGFGGGGGG1GGGGG1GBGGGGGGGGFGGGGG.GGG8GGGGG>GGGBGBGDGGGGGEGG0', 'SAM_TAGS': ['YT:Z:UP'], 'read_group': '2', 'conversion_bases': 'C2T', 'mapping_reference': 'W_G2A'}), ({'QNAME': 'chr10-65374', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '118997', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '119227', 'TLEN': '355', 'SEQ': 'CTGGGTCAAAGTAAAGGGATAGTAGCTATAGGTTGAGAGGTAGTTAGAAAAAAAAATTTTTTTTTTATAGTTTGTTGTTGGTGGTGGTGGTGGTGGTTTTTTTGAGGCTCTGTGTGATCTAGTTC', 'QUAL': 'CCABCGGGGGGGGGGFGGGGGGGFGGG<EGGGGGGGGGGFGGGGGGGGGGGG=GGGGGEGGGCGGGGBGGEGG:GGGGGG0GAGGGGGGG0GGGGGGG0GGGGGGGGGB8G1GGGGGGGGGGGG<', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:-3', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'C2T', 'mapping_reference': 'C_C2T'}, {'QNAME': 'chr10-65374', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '119227', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '118997', 'TLEN': '-355', 'SEQ': 'TTATATAAACTGATCTTACCTCAAAACAAATTATAACAAAAAAAAAAATAACTATAATATTAATACACACATTACATATCAATTTCCTAAAAAGCTTCTTTATCATATTACATTAAAACCCACCC', 'QUAL': '0GGEGGGGGDGBGBGGG>GGGGG8GGG.GGGGGFGGGGGGGGBG1GGGGG1GGGGGGFGFGGFGGGGGGGGFEGGGGGGGG@GFGGGGGFGGGGGGGGGGGG1@1C=BG>GG1GGGGGGGCC<BA', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:112A12', 'YS:i:0', 'YT:Z:CP', 'XO:Z:C_C2T'], 'read_group': '1', 'conversion_bases': 'G2A', 'mapping_reference': 'C_C2T'})]

test_reads = [test_read_1, test_read_2, test_read_3, test_read_4, test_read_5, test_read_6]

processed_output = []

for reads in test_reads:
    processed_output.append(ProcessSamAlignment(sam_reads=reads, contig_lens=contig_lens).output_reads)


class TestSamReadProcessing(unittest.TestCase):

    def setUp(self):
        pass

    def test_crick_start_conversion(self):
        mapping_number_1, processed_reads1 = processed_output[0]
        self.assertEqual(1, mapping_number_1)
        # assert flags have been switch relative to watson reference
        self.assertEqual(processed_reads1[0][0]['FLAG'], '115')
        self.assertEqual(processed_reads1[0][1]['FLAG'], '179')
        # assert positions are correct, based on simulation sam
        self.assertEqual(processed_reads1[0][0]['POS'], '304380')
        self.assertEqual(processed_reads1[0][1]['POS'], '304150')
        # check template length is calculated correctly for each read
        self.assertEqual(processed_reads1[0][0]['TLEN'], '-355')
        self.assertEqual(processed_reads1[0][1]['TLEN'], '355')
        # check proper location of mapped read
        self.assertEqual(processed_reads1[0][0]['PNEXT'], processed_reads1[0][1]['POS'])
        self.assertEqual(processed_reads1[0][1]['PNEXT'], processed_reads1[0][0]['POS'])

    def test_multi_reference(self):
        mapping_number_2, processed_reads2 = processed_output[1]
        # check number of mapped reference is equal to 2
        self.assertEqual(mapping_number_2, 2)
        mapping_strands = processed_reads2[0][0]['SAM_TAGS'][1].split(':')[-1].split(',')
        # check mapping references are C_C2T and W_G2A
        self.assertIn('C_C2T', mapping_strands)
        self.assertIn('W_G2A', mapping_strands)

    def test_flag_mismatch(self):
        # check mismatched flags with fail
        mapping_number_3 = processed_output[2][0]
        self.assertEqual(0, mapping_number_3)

    def test_mismatch(self):
        # test paired mismatch will fail
        mapping_number_4 = processed_output[3][0]
        self.assertEqual(0, mapping_number_4)

    def test_deletion(self):
        processed_reads_5 = processed_output[4][1]
        # a deletion relative to the reference will change the mapping location
        self.assertEqual(processed_reads_5[0][0]['POS'], '304383')

    def test_multimapping(self):
        processed_read_number = len(processed_output[5][1])
        self.assertEqual(processed_read_number, 2)


if __name__ == '__main__':
    unittest.main()
