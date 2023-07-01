print("""
                                                Welcome To Triangle Indicator
    Note: It will only indicate a triangle as Isosceles, Equilateral, Scalene, or Right Angled triangle, not more than that!
                                    The programme will not stop until you won't quit the terminal!
""")
i = 0
while i < 4:
    try:
        sides = [float(input("Length of {}No side of the triangle (Unit): ".format(i))) for i in range(1, 4)]
        squares = [round(side ** 2, 4) for side in sides]

        print("Your result is generating.....")

        if any(x + y == z for x, y, z in zip(squares, squares[1:] + squares[:1], squares[2:] + squares[:2])):
            if len(set(sides)) == 2:
                print("""
                                        It is a Right Angled Triangle and also an Isosceles Triangle
                """)
            elif len(set(sides)) == 1:
                print("""
                                     It is a Right Angled Triangle and also an Equilateral Triangle
                """)
            else:
                print("""
                                    It is a Right Angled Triangle
                """)
        elif len(set(sides)) == 2:
            print("""
                                    It is an Isosceles Triangle
            """)
        elif len(set(sides)) == 1:
            print("""
                                    It is an Equilateral Triangle
            """)
        else:
            print("""
                                    It is a Scalene Triangle
            """)

    except ValueError:
        print("Value error occurred.Please give the accurate input!")
    print("""
        Copyright© 2023 All rights reserved
                Made by The Miraz Mahin
    """)
