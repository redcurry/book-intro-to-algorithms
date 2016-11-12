binarySearch :: Ord a => [a] -> a -> Int
binarySearch xs v = binarySearchRec xs v 0

binarySearchRec :: Ord a => [a] -> a -> Int -> Int
binarySearchRec [] _ _ = -1
binarySearchRec [x] v i
    | v == x = i
    | otherwise = -1
binarySearchRec xs v i
    | v  < (head $ rightHalf xs) = binarySearchRec (leftHalf xs) v i
    | otherwise = binarySearchRec (rightHalf xs) v (i + (length xs) `div` 2)

leftHalf :: [a] -> [a]
leftHalf xs = take ((length xs) `div` 2) xs

rightHalf :: [a] -> [a]
rightHalf xs = drop ((length xs) `div` 2) xs
