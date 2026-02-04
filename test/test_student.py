from src.student import calculate_average, get_grade

# --- Testing the Average Calculation ---
def test_average_calculation():
    assert calculate_average([80, 80, 80, 80, 80]) == 80
    assert calculate_average([100, 50]) == 75
   

# --- Testing the Grade Logic ---
def test_grade_a_plus():
    assert get_grade(95) == "A+"
    assert get_grade(90) == "A+"

def test_grade_a():
    assert get_grade(85) == "A"
    assert get_grade(75) == "A"

def test_grade_b():
    assert get_grade(65) == "B"
    assert get_grade(60) == "B"

def test_grade_c():
    assert get_grade(55) == "C"
    assert get_grade(50) == "C"

def test_grade_fail():
    assert get_grade(49) == "Fail"
    assert get_grade(0) == "Fail"

def test_newAverage():
    assert calculate_average([20,40,50,60,30]) == 40

def tes_grade():
    assert get_grade(90)=='Fail'
