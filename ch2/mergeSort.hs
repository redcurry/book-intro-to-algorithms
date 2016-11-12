mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort $ leftHalf xs) (mergeSort $ rightHalf xs)

merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) = if x < y then x:(merge xs (y:ys)) else y:(merge (x:xs) ys)

leftHalf :: [a] -> [a]
leftHalf xs = take ((length xs) `div` 2) xs

rightHalf :: [a] -> [a]
rightHalf xs = drop ((length xs) `div` 2) xs
