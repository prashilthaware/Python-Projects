char=input("Enter a character:")

match char:
    case 'a'|'e'|'i'|'o'|'u':
        print("It is a vowel")
    case 'A'|'E'|'I'|'O'|'U':
        print("It is a vowel")
    case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
        print("It is a consonant")
    case 'B' | 'C' | 'D' | 'F' | 'G' | 'H' | 'J' | 'K' | 'L' | 'M' | 'N' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'V' | 'W' | 'X' | 'Y' | 'Z':
        print("It is a consonant")