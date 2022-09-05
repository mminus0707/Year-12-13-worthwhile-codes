main = do
  putStrLn "I am illiterate"
  print (square 4)
  print (piApprox)
  print (twiceSum 3 2)
  print (sumThree 5 2 3)
  print (areaOfCircle 5)
  print (volumeOfCylinder 5 5)
  print (threeDifferent 1 1 1)
  print (divisibleBy 3 2)
  print (isEven 6)
  print (factorial 7)
  print (sumtorial 6)
  print (absolute (-6))
  print (sign (-2))

-- functionName of type Int with a result type of Int
square :: Int -> Int
square 0 = 0
square 1 = 1
square n = n * n

-- constantName of type Float with the value of 22/7 which gives us 3.142857
piApprox :: Float
piApprox = 22/7

-- exercises

-- here we have two Int parameters
-- We want to add them and then multiply by 2
twiceSum :: Int -> Int -> Int
twiceSum x y = (x + y)*2

timesTen :: Int -> Int
timesTen 0 = 0
timesTen 1 = 10
timesTen n = 0

sumThree :: Int -> Int -> Int -> Int
sumThree x y z = (x + y + z)

areaOfCircle :: Float -> Float
areaOfCircle r = (r*r)*(22/7)

volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder l r = ((r*r)*(22/7))*l

-- Use && for and 
-- Use || for or
threeDifferent :: Int -> Int -> Int -> Bool
threeDifferent x y z = if x == z && z == y then False else True

divisibleBy :: Int -> Int -> Bool
divisibleBy x y = if x `rem` y == 0 then True else False

absolute :: Int -> Int
absolute n = if n < 0 then (-n) else n

-- need to look up `mod`
isEven :: Integer -> Bool
isEven n = if n `mod` 2 == 0 then True else False

-- These questions need to use RECURSION!
factorial :: Int -> Int
factorial 1 = 1
factorial 0 = 0
factorial n = n * factorial(n-1)

sumtorial :: Int -> Int
sumtorial 1 = 1
sumtorial 0 = 0
sumtorial n = n + sumtorial(n-1)

sign :: Int -> String
sign n = if n == 0 then "None" else if n > 0 then "Positive" else "Negative"