-- name: 3475. dna pattern recognition
-- link: https://leetcode.com/problems/dna-pattern-recognition

-- solution --
select
	sample_id, dna_sequence, species,
	case when dna_sequence like 'ATG%' then 1 else 0 end as has_start,
	case when dna_sequence regexp '(TAA|TAG|TGA)$' then 1 else 0 end as has_stop,
	case when dna_sequence regexp 'ATAT' then 1 else 0 end as has_atat,
	case when dna_sequence regexp 'GGG' then 1 else 0 end as has_ggg
from Samples