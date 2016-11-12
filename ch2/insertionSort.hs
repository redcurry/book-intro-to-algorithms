insertionSort :: (Ord a) => [a] -> [a]
insertionSort [] = []
insertionSort xs = insertionSortRec [] xs

insertionSortRec :: (Ord a) => [a] -> [a] -> [a]
insertionSortRec sorted [] = sorted
insertionSortRec sorted (x:xs) = insertionSortRec (insert sorted x) xs

insert :: (Ord a) => [a] -> a -> [a]
insert [] v = [v]
insert xs v = let splitted = split xs v
                  left = fst splitted
                  right = snd splitted
               in left ++ [v] ++ right

split :: (Ord a) => [a] -> a -> ([a], [a])
split xs v = splitRec ([], xs) v

splitRec :: (Ord a) => ([a], [a]) -> a -> ([a], [a])
splitRec (ys, [])   v = (ys, [])
splitRec (ys, x:xs) v = if v > x
                        then splitRec (ys ++ [x], xs) v
                        else (ys, x:xs)

-- From StackOverflow:
insertionSort2 :: Ord a => [a] -> [a]
insertionSort2 [] = []
insertionSort2 [x] = [x]
insertionSort2 (x:xs) = insert (insertionSort2 xs)
    where insert [] = [x]
          insert (y:ys)
            | x < y = x : y : ys
            | otherwise = y : insert ys
