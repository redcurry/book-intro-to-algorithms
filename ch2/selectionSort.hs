-- Adapted from rosettacode:
selectionSort :: (Ord a) => [a] -> [a]
selectionSort [] = []
selectionSort xs = let x = minimum xs in x : selectionSort (remove x xs)
    where remove _ [] = []
          remove a (x:xs)
            | a == x = xs
            | otherwise = x : remove a xs
