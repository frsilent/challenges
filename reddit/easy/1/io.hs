{-# OPTIONS_GHC -Wall #-}
{-|
create a program that will ask the users name, age, and reddit username.
have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.
-}


--Constructs a greeting based on passed arguments (format name, age, username)
greeting :: (String,String,String) -> String
greeting (name, age, username) = "Your name is " ++ name ++ ", you are "
    ++ age ++ " years old, and your username is " ++ username ++ "."


main = do
   putStrLn "What is your name? "
   name <- getLine
   putStrLn "What is your age? "
   age <- getLine
   putStrLn "What is your username? "
   username <- getLine

   let result = greeting(name, age, username)
   putStrLn result
