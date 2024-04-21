SELECT
    ANIMAL_TYPE
    , count (ANIMAL_TYPE) as count

from ANIMAL_INS 
group by ANIMAL_TYPE
order by 1