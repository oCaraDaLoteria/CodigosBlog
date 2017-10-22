import sqlite3
import numpy as np
from psutil import virtual_memory

## NAO recomendado. Use a versao Matlab se possivel
 
def combinations(list, k):
    """Choose combinations of list, choosing k elements(no repeats)"""
    if len(list) < k:
        return []
    else:
        seq = [i for i in range(k)]
        while seq:
			jogo = [list[index] for index in seq]
			print(jogo)
			conn = sqlite3.connect('lotofacil.db')
			cur = conn.cursor()
			sql = ''' INSERT INTO todas_combinacoes(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15)
						  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
			cur.execute(sql, jogo)
			conn.commit()
			conn.close()
			seq = get_next_combination(len(list), k, seq)
 
def get_next_combination(num_elements, k, seq):
        index_to_move = find_index_to_move(num_elements, seq)
        if index_to_move == None:
            return None
        else:
            seq[index_to_move] += 1
 
            #for every element past this sequence, move it down
            for i, elem in enumerate(seq[(index_to_move+1):]):
                seq[i + 1 + index_to_move] = seq[index_to_move] + i + 1
 
            return seq
 
def find_index_to_move(num_elements, seq):
        """Tells which index should be moved"""
        for rev_index, elem in enumerate(reversed(seq)):
            if elem < (num_elements - rev_index - 1):
                return len(seq) - rev_index - 1
        return None
        
        
# ref: https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n?page=2&tab=votes#tab-top
intervalo_valores = range(1,26)
numero_dezenas = 15
combinations(intervalo_valores,numero_dezenas)
 
 
 
 
