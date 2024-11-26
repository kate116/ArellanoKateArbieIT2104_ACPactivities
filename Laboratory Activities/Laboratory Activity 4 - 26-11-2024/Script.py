from Capybara import Capybara

capybara1 = Capybara("Biscoff", "M", 5)
capybara2 = Capybara("Caramel", "F", 3)

testcases = {
    1: capybara1,
    2: capybara2
}

testcase = int(input("Enterthe test case number: "))
selectedcapybara = testcases.get(testcase, None)

print(f"Test Case {testcase}: Name:{selectedcapybara.name}, Gender: {selectedcapybara.gender} Age: {selectedcapybara.age} years old")